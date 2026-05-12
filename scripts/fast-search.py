#!/usr/bin/env python3
"""
Memory System SQLite Database + Analytics
Fast search + insights for our memory system!
"""

import sqlite3
import os
import re
from datetime import datetime
from pathlib import Path
from collections import Counter

# Use the venv Python for sqlite3 (built-in)
PYTHON = "/home/openclaw/.venv/bin/python"

BASE = Path("/home/openclaw/.openclaw/workspace-mochi")
DB_PATH = BASE / "memory" / "memory-search.db"

def init_database():
    """Initialize the SQLite database with tables."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    
    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS memories
                 (id INTEGER PRIMARY KEY, date TEXT, content TEXT, file_path TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS decisions
                 (id INTEGER PRIMARY KEY, date TEXT, topic TEXT, content TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS people
                 (id INTEGER PRIMARY KEY, name TEXT, mention_count INTEGER DEFAULT 0)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS tags
                 (id INTEGER PRIMARY KEY, name TEXT, usage_count INTEGER DEFAULT 0)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS mistakes
                 (id INTEGER PRIMARY KEY, date TEXT, error TEXT, lesson TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS improvements
                 (id INTEGER PRIMARY KEY, date TEXT, feedback TEXT)''')
    
    conn.commit()
    return conn

def extract_date_from_filename(filename):
    """Extract YYYY-MM-DD from filename like 2026-05-11.md"""
    match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
    return match.group(1) if match else None

def extract_tags(content):
    """Extract all #tags from content."""
    return re.findall(r'#(\w+)', content)

def extract_people(content):
    """Extract known people from content."""
    known_people = ['sara', 'stuart', 'momo', 'hank', 'jeem', 'jim']
    found = []
    content_lower = content.lower()
    for person in known_people:
        if person in content_lower:
            found.append(person)
    return found

def extract_decisions(content):
    """Extract decisions from content."""
    decisions = []
    in_decision = False
    current_decision = []
    
    for line in content.split('\n'):
        if '* Decision:' in line or '**Decision:**' in line:
            in_decision = True
            current_decision = [line]
        elif in_decision:
            if line.strip().startswith('* ') or line.strip().startswith('- '):
                current_decision.append(line)
            else:
                if current_decision:
                    decisions.append(' '.join(current_decision))
                in_decision = False
    
    if current_decision:
        decisions.append(' '.join(current_decision))
    
    return decisions

def index_memories(conn):
    """Index all memory files into the database."""
    c = conn.cursor()
    memory_dir = BASE / "memory"
    
    # Clear existing data
    c.execute("DELETE FROM memories")
    c.execute("DELETE FROM decisions")
    c.execute("DELETE FROM people")
    c.execute("DELETE FROM tags")
    c.execute("DELETE FROM mistakes")
    c.execute("DELETE FROM improvements")
    
    print("🐹 Indexing memory files...")
    
    # Track counts
    people_counts = Counter()
    tag_counts = Counter()
    
    # Index each memory file
    for md_file in memory_dir.glob("*.md"):
        if md_file.name == "memory-report.html":
            continue
            
        date = extract_date_from_filename(md_file.name)
        content = md_file.read_text()
        
        # Insert memory
        c.execute("INSERT INTO memories (date, content, file_path) VALUES (?, ?, ?)",
                  (date, content, str(md_file)))
        
        # Extract and count people
        people = extract_people(content)
        for person in people:
            people_counts[person] += 1
        
        # Extract and count tags
        tags = extract_tags(content)
        for tag in tags:
            tag_counts[tag] += 1
        
        # Extract decisions
        decisions = extract_decisions(content)
        for decision in decisions:
            topic = decision[:50] + "..." if len(decision) > 50 else decision
            c.execute("INSERT INTO decisions (date, topic, content) VALUES (?, ?, ?)",
                      (date, topic, decision))
    
    # Insert people counts
    for name, count in people_counts.items():
        c.execute("INSERT INTO people (name, mention_count) VALUES (?, ?)", (name, count))
    
    # Insert tag counts
    for name, count in tag_counts.items():
        c.execute("INSERT INTO tags (name, usage_count) VALUES (?, ?)", (name, count))
    
    conn.commit()
    
    print(f"   ✅ Indexed {len(list(memory_dir.glob('*.md')))} memory files")
    print(f"   ✅ Found {len(people_counts)} people")
    print(f"   ✅ Found {len(tag_counts)} unique tags")
    print(f"   ✅ Found {len(decisions)} decisions")
    
    return {
        'memories': len(list(memory_dir.glob("*.md"))),
        'people': len(people_counts),
        'tags': len(tag_counts),
        'decisions': len(decisions)
    }

def search(query, date_from=None, date_to=None):
    """Fast search through memories with optional date filtering."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    
    base_query = "SELECT date, substr(content, 1, 200) FROM memories WHERE content LIKE ?"
    params = [f'%{query}%']
    
    # Add date filtering
    if date_from and date_to:
        base_query += " AND date BETWEEN ? AND ?"
        params.extend([date_from, date_to])
    elif date_from:
        base_query += " AND date >= ?"
        params.append(date_from)
    elif date_to:
        base_query += " AND date <= ?"
        params.append(date_to)
    
    base_query += " LIMIT 10"
    
    results = c.execute(base_query, params).fetchall()
    
    conn.close()
    return results

def get_analytics():
    """Get all analytics from the database."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    
    stats = {}
    
    # Total memories
    stats['total_memories'] = c.execute("SELECT COUNT(*) FROM memories").fetchone()[0]
    
    # Decisions
    stats['total_decisions'] = c.execute("SELECT COUNT(*) FROM decisions").fetchone()[0]
    stats['decisions'] = c.execute("SELECT date, topic FROM decisions").fetchall()
    
    # People
    stats['people'] = c.execute("SELECT name, mention_count FROM people ORDER BY mention_count DESC").fetchall()
    
    # Tags
    stats['tags'] = c.execute("SELECT name, usage_count FROM tags ORDER BY usage_count DESC LIMIT 10").fetchall()
    
    # Mistakes
    stats['total_mistakes'] = c.execute("SELECT COUNT(*) FROM mistakes").fetchone()[0]
    
    # Improvements  
    stats['total_improvements'] = c.execute("SELECT COUNT(*) FROM improvements").fetchone()[0]
    
    conn.close()
    return stats

def print_analytics(stats):
    """Print analytics in a nice format."""
    print("\n" + "="*50)
    print("📊 MEMORY SYSTEM ANALYTICS")
    print("="*50)
    
    print(f"\n📁 Total Memories: {stats['total_memories']}")
    print(f"📋 Total Decisions: {stats['total_decisions']}")
    print(f"❌ Total Mistakes: {stats['total_mistakes']}")
    print(f"📈 Total Improvements: {stats['total_improvements']}")
    
    print("\n👥 People Mentioned (most to least):")
    for name, count in stats['people'][:5]:
        print(f"   - {name}: {count} mentions")
    
    print("\n🏷️ Top Tags:")
    for name, count in stats['tags'][:10]:
        print(f"   - #{name}: {count}")
    
    print("\n📋 Recent Decisions:")
    for date, topic in stats['decisions'][:5]:
        print(f"   - {date}: {topic}")
    
    print("\n" + "="*50)

# ============ WEEKLY STATS FUNCTIONS ============

def log_weekly_stat(stat_type, value, notes=""):
    """Log a weekly stat (gym, miles, work)."""
    from datetime import datetime
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Check if there's an entry for today
    c.execute("SELECT id, gym_sessions, miles, work_hours FROM weekly_stats WHERE date = ?", (today,))
    row = c.fetchone()
    
    if row:
        # Update existing entry
        if stat_type == "gym":
            c.execute("UPDATE weekly_stats SET gym_sessions = gym_sessions + ?, notes = ? WHERE date = ?", 
                      (value, notes, today))
        elif stat_type == "miles":
            c.execute("UPDATE weekly_stats SET miles = miles + ?, notes = ? WHERE date = ?", 
                      (value, notes, today))
        elif stat_type == "work":
            c.execute("UPDATE weekly_stats SET work_hours = work_hours + ?, notes = ? WHERE date = ?", 
                      (value, notes, today))
    else:
        # Create new entry
        gym_val = value if stat_type == "gym" else 0
        miles_val = value if stat_type == "miles" else 0
        work_val = value if stat_type == "work" else 0
        c.execute("INSERT INTO weekly_stats (date, gym_sessions, miles, work_hours, notes) VALUES (?, ?, ?, ?, ?)",
                  (today, gym_val, miles_val, work_val, notes))
    
    conn.commit()
    conn.close()
    print(f"✅ Logged: {stat_type} +{value}")

def get_weekly_stats(days=7):
    """Get stats for the last N days."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    
    stats = c.execute("""
        SELECT date, gym_sessions, miles, work_hours, notes 
        FROM weekly_stats 
        ORDER BY date DESC 
        LIMIT ?
    """, (days,)).fetchall()
    
    conn.close()
    return stats

def print_weekly_stats(days=7):
    """Print weekly stats summary."""
    stats = get_weekly_stats(days)
    
    print("\n" + "="*50)
    print(f"📊 WEEKLY STATS (Last {days} days)")
    print("="*50)
    
    total_gym = 0
    total_miles = 0
    total_work = 0
    
    for date, gym, miles, work, notes in stats:
        print(f"📅 {date}: 🏋️ {gym} | 🏃 {miles} mi | 💼 {work}h")
        total_gym += gym
        total_miles += miles
        total_work += work
    
    print("-" * 50)
    print(f"📈 TOTALS: 🏋️ {total_gym} sessions | 🏃 {total_miles} miles | 💼 {total_work} hours")
    print("="*50)

def get_weekly_totals():
    """Get just the totals for current week."""
    stats = get_weekly_stats(7)
    total_gym = sum(s[1] for s in stats)
    total_miles = sum(s[2] for s in stats)
    total_work = sum(s[3] for s in stats)
    return total_gym, total_miles, total_work

# ============ IMPROVEMENTS AUTO-INDEX FUNCTIONS ============

def index_improvements(conn):
    """Auto-index improvements from memory/improvements/ folder."""
    c = conn.cursor()
    improvements_dir = BASE / "memory" / "improvements"
    
    # Clear existing improvements
    c.execute("DELETE FROM improvements")
    
    print("🐹 Indexing improvements...")
    
    for md_file in improvements_dir.glob("*.md"):
        if md_file.name == "1percent-better-counter.md":
            continue  # Skip the counter file
            
        content = md_file.read_text()
        
        # Extract date from first ## heading
        import re
        date_match = re.search(r'##\s+(\d{4}-\d{2}-\d{2})', content)
        if date_match:
            date = date_match.group(1)
        else:
            continue
        
        # Extract improvement content (between ## and next ## or ***)
        improvement_match = re.search(r'##\s+\d{4}-\d{2}-\d{2}.*?\*\*Improvement:\*\*\s*(.+?)(?=\*\*|$)', content, re.DOTALL)
        if improvement_match:
            feedback = improvement_match.group(1).strip()[:200]
        else:
            feedback = md_file.name
        
        # Determine category from content
        category = "general"
        if "1percent" in content.lower():
            category = "1percent-better"
        elif "proactive" in content.lower():
            category = "proactive"
        elif "hybrid" in content.lower():
            category = "system"
        
        c.execute("INSERT INTO improvements (date, feedback, category) VALUES (?, ?, ?)",
                  (date, feedback, category))
    
    count = c.execute("SELECT COUNT(*) FROM improvements").fetchone()[0]
    conn.commit()
    print(f"   ✅ Indexed {count} improvements")
    return count

def get_improvements():
    """Get all improvements from database."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    improvements = c.execute("SELECT date, feedback, category FROM improvements ORDER BY date DESC").fetchall()
    conn.close()
    return improvements

def print_improvements():
    """Print all improvements."""
    improvements = get_improvements()
    
    print("\n" + "="*50)
    print("📈 IMPROVEMENTS LOG")
    print("="*50)
    
    for date, feedback, category in improvements:
        print(f"\n📅 {date} [{category}]")
        print(f"   {feedback[:100]}...")
    
    print("\n" + "="*50)

# ============ MISTAKES AUTO-INDEX FUNCTIONS ============

def index_mistakes(conn):
    """Auto-index mistakes from memory/mistakes/ folder."""
    c = conn.cursor()
    mistakes_dir = BASE / "memory" / "mistakes"
    
    # Clear existing mistakes
    c.execute("DELETE FROM mistakes")
    
    print("🐹 Indexing mistakes...")
    
    for md_file in mistakes_dir.glob("*.md"):
        content = md_file.read_text()
        
        # Extract all mistake entries
        mistake_entries = re.findall(
            r'##\s+(\d{4}-\d{2}-\d{2})\s+-\s+(.+?)\n\*\*What happened:\*\*\s*(.+?)(?:\*\*|$)',
            content, re.DOTALL
        )
        
        for date, title, what_happened in mistake_entries:
            lesson_match = re.search(r'\*\*Lesson learned:\*\*\s*(.+?)(?:\*\*|$)', content, re.DOTALL)
            lesson = lesson_match.group(1).strip() if lesson_match else "No lesson recorded"
            c.execute("INSERT INTO mistakes (date, error, lesson) VALUES (?, ?, ?)",
                      (date, f"{title}: {what_happened[:100]}", lesson[:200]))
    
    count = c.execute("SELECT COUNT(*) FROM mistakes").fetchone()[0]
    conn.commit()
    print(f"   ✅ Indexed {count} mistakes")
    return count

def get_mistakes():
    """Get all mistakes from database."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    mistakes = c.execute("SELECT date, error, lesson FROM mistakes ORDER BY date DESC").fetchall()
    conn.close()
    return mistakes

def print_mistakes():
    """Print all mistakes."""
    mistakes = get_mistakes()
    
    print("\n" + "="*50)
    print("❌ MISTAKES LOG")
    print("="*50)
    
    if not mistakes:
        print("\n   No mistakes logged yet!")
    
    for date, error, lesson in mistakes:
        print(f"\n📅 {date}")
        print(f"   Error: {error[:80]}...")
        print(f"   Lesson: {lesson[:80]}...")
    
    print("\n" + "="*50)

# ============ TAG TRENDS FUNCTIONS ============

def index_tag_history(conn, days=30):
    """Index tag usage over time for trend analysis."""
    c = conn.cursor()
    
    # Get date range
    from datetime import datetime, timedelta
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    # Clear old tag history
    c.execute("DELETE FROM tag_history")
    
    print("🐹 Indexing tag trends...")
    
    # For each day, count tags from memory files
    memory_dir = BASE / "memory"
    import re
    
    for md_file in memory_dir.glob("*.md"):
        if md_file.name == "memory-report.html":
            continue
        
        # Extract date from filename
        date_match = re.match(r'(\d{4}-\d{2}-\d{2})', md_file.name)
        if not date_match:
            continue
        
        file_date = date_match.group(1)
        
        # Skip if outside range
        file_date_dt = datetime.strptime(file_date, "%Y-%m-%d")
        if file_date_dt < start_date or file_date_dt > end_date:
            continue
        
        # Extract tags from file
        content = md_file.read_text()
        tags = re.findall(r'#(\w+)', content)
        
        # Count each tag
        from collections import Counter
        tag_counts = Counter(tags)
        
        for tag, count in tag_counts.items():
            c.execute("INSERT INTO tag_history (date, tag_name, count) VALUES (?, ?, ?)",
                      (file_date, tag, count))
    
    count = c.execute("SELECT COUNT(*) FROM tag_history").fetchone()[0]
    conn.commit()
    print(f"   ✅ Indexed {count} tag entries")
    return count

def get_tag_trends(days=30):
    """Get tag trends over time."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    
    # Get recent tags
    c.execute("SELECT tag_name, SUM(count) as total FROM tag_history GROUP BY tag_name ORDER BY total DESC LIMIT 10")
    recent = c.fetchall()
    
    # Get week-over-week comparison
    from datetime import datetime, timedelta
    now = datetime.now()
    week_ago = (now - timedelta(days=7)).strftime("%Y-%m-%d")
    two_weeks_ago = (now - timedelta(days=14)).strftime("%Y-%m-%d")
    
    c.execute("SELECT tag_name, SUM(count) as total FROM tag_history WHERE date >= ? GROUP BY tag_name", (week_ago,))
    this_week = c.fetchall()
    
    c.execute("SELECT tag_name, SUM(count) as total FROM tag_history WHERE date >= ? AND date < ? GROUP BY tag_name", (two_weeks_ago, week_ago))
    last_week = c.fetchall()
    
    conn.close()
    
    # Build trend dict
    trends = {}
    for tag, count in this_week:
        trends[tag] = {"this_week": count, "last_week": 0}
    for tag, count in last_week:
        if tag in trends:
            trends[tag]["last_week"] = count
        else:
            trends[tag] = {"this_week": 0, "last_week": count}
    
    return recent, trends

def print_tag_trends(days=30):
    """Print tag trends analysis."""
    recent, trends = get_tag_trends(days)
    
    print("\n" + "="*50)
    print(f"🏷️ TAG TRENDS (Last {days} days)")
    print("="*50)
    
    print("\n📊 Most Used Tags:")
    for tag, count in recent[:10]:
        print(f"   #{tag}: {count} uses")
    
    print("\n📈 Week-over-Week Changes:")
    
    # Calculate changes
    changes = []
    for tag, data in trends.items():
        this_w = data["this_week"]
        last_w = data["last_week"]
        if last_w > 0:
            change = ((this_w - last_w) / last_w) * 100
            changes.append((tag, this_w, last_w, change))
        elif this_w > 0:
            changes.append((tag, this_w, 0, 100))  # New tag
    
    # Sort by change
    changes.sort(key=lambda x: x[3], reverse=True)
    
    for tag, this_w, last_w, change in changes[:5]:
        emoji = "📈" if change > 0 else "📉" if change < 0 else "➡️"
        print(f"   {emoji} #{tag}: {last_w} → {this_w} ({change:+.0f}%)")
    
    print("\n" + "="*50)

def run_full_index():
    """Run the full indexing process."""
    print("🚀 Building Memory Search Index...")
    conn = init_database()
    stats = index_memories(conn)
    
    # Also index improvements
    index_improvements(conn)
    
    # Also index mistakes
    index_mistakes(conn)
    
    # Also index tag trends
    index_tag_history(conn)
    
    conn.close()
    
    print("\n✅ Index built successfully!")
    print_analytics(get_analytics())
    
    return stats

# ============ NEW FUNCTIONS v2.0 ============

def show_people_mentions(person=None):
    """Show people mentions from memories."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    
    if person:
        c.execute("""SELECT name, mention_count FROM people 
                       WHERE name LIKE ? ORDER BY mention_count DESC""", (f"%{person}%",))
    else:
        c.execute("SELECT name, mention_count FROM people ORDER BY mention_count DESC")
    
    results = c.fetchall()
    conn.close()
    
    print("\n" + "="*50)
    print("👥 PEOPLE MENTIONS")
    print("="*50)
    
    if person:
        print(f"\nSearching for: {person}")
    
    for name, count in results:
        print(f"   {name}: {count} mentions")
    
    print("\n" + "="*50)

def show_recent_decisions(limit=10):
    """Show recent decisions."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    
    c.execute("SELECT date, topic, content FROM decisions ORDER BY date DESC LIMIT ?", (limit,))
    results = c.fetchall()
    conn.close()
    
    print("\n" + "="*50)
    print("📝 RECENT DECISIONS")
    print("="*50)
    
    for date, topic, content in results:
        print(f"\n[{date}] {topic}")
        # Show first line of content
        first_line = content.split('\n')[0][:80]
        print(f"   {first_line}...")
    
    print("\n" + "="*50)

def show_timeline(days=7):
    """Show timeline of recent memories."""
    from datetime import datetime, timedelta
    
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    
    # Get memories from last N days
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    c.execute("SELECT date, content FROM memories WHERE date >= ? ORDER BY date DESC", (start_date,))
    results = c.fetchall()
    conn.close()
    
    print("\n" + "="*50)
    print(f"📅 TIMELINE (Last {days} days)")
    print("="*50)
    
    current_date = None
    for date, content in results:
        if date != current_date:
            print(f"\n📅 {date}")
            current_date = date
        # Show first line
        first_line = content.split('\n')[0][:60]
        print(f"   • {first_line}")
    
    print("\n" + "="*50)

def show_quick_summary(days=7):
    """Quick one-line summary of recent days."""
    from datetime import datetime, timedelta
    
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    c.execute("SELECT date, content FROM memories WHERE date >= ? ORDER BY date DESC", (start_date,))
    results = c.fetchall()
    conn.close()
    
    print("\n" + "="*50)
    print(f"⚡ QUICK SUMMARY (Last {days} days)")
    print("="*50)
    
    # Group by date
    by_date = {}
    for date, content in results:
        if date not in by_date:
            by_date[date] = []
        # Get first non-empty line
        for line in content.split('\n'):
            if line.strip():
                by_date[date].append(line.strip()[:50])
                break
    
    for date in sorted(by_date.keys(), reverse=True):
        items = by_date[date][:2]  # Max 2 items per day
        print(f"\n📅 {date}")
        for item in items:
            print(f"   • {item}")
    
    print("\n" + "="*50)

def filter_by_tag(tag, days=30):
    """Filter memories by specific tag."""
    from datetime import datetime, timedelta
    
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    c.execute("SELECT date, content FROM memories WHERE date >= ? ORDER BY date DESC", (start_date,))
    results = c.fetchall()
    conn.close()
    
    print("\n" + "="*50)
    print(f"🏷️ MEMORIES WITH #{tag} (Last {days} days)")
    print("="*50)
    
    found = False
    for date, content in results:
        if f"#{tag}" in content.lower():
            found = True
            print(f"\n📅 {date}")
            # Show relevant lines
            for line in content.split('\n'):
                if f"#{tag}" in line.lower():
                    print(f"   {line.strip()}")
    
    if not found:
        print(f"\nNo memories found with #{tag}")
    
    print("\n" + "="*50)

def export_memories(days=7, output_file="memory_export.md"):
    """Export memories to a markdown file."""
    from datetime import datetime, timedelta
    
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    c.execute("SELECT date, content FROM memories WHERE date >= ? ORDER BY date ASC", (start_date,))
    results = c.fetchall()
    conn.close()
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write(f"# Memory Export - Last {days} days\n\n")
        f.write(f"*Exported: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        
        current_date = None
        for date, content in results:
            if date != current_date:
                f.write(f"\n## {date}\n\n")
                current_date = date
            f.write(content + "\n\n")
    
    print(f"\n✅ Exported {len(results)} memories to {output_file}")

# ============================================

# Command line interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "search":
            # Parse search with optional date filters
            # Usage: search "query" --from 2026-05-01 --to 2026-05-12
            #        search "query" --this-week
            #        search "query" --this-month
            
            args = sys.argv[2:]
            query_parts = []
            date_from = None
            date_to = None
            
            i = 0
            while i < len(args):
                if args[i] == "--from":
                    date_from = args[i+1]
                    i += 2
                elif args[i] == "--to":
                    date_to = args[i+1]
                    i += 2
                elif args[i] == "--this-week":
                    from datetime import timedelta
                    today = datetime.now()
                    date_to = today.strftime("%Y-%m-%d")
                    date_from = (today - timedelta(days=7)).strftime("%Y-%m-%d")
                    i += 1
                elif args[i] == "--this-month":
                    from datetime import datetime
                    today = datetime.now()
                    date_to = today.strftime("%Y-%m-%d")
                    date_from = f"{today.year}-{today.month:02d}-01"
                    i += 1
                else:
                    query_parts.append(args[i])
                    i += 1
            
            query = " ".join(query_parts)
            results = search(query, date_from, date_to)
            
            print(f"\n🔍 Search results for '{query}':")
            if date_from or date_to:
                print(f"   📅 Date range: {date_from or 'start'} to {date_to or 'today'}")
            print()
            for date, content in results:
                print(f"📅 {date}: {content}...")
        
        elif command == "analytics":
            stats = get_analytics()
            print_analytics(stats)
        
        elif command == "rebuild":
            run_full_index()
        
        # Weekly stats commands
        elif command == "stats":
            days = int(sys.argv[2]) if len(sys.argv) > 2 else 7
            print_weekly_stats(days)
        
        elif command == "log":
            # Usage: python3 fast-search.py log gym 1
            #        python3 fast-search.py log miles 3.5
            #        python3 fast-search.py log work 8
            if len(sys.argv) < 4:
                print("Usage: python3 fast-search.py log [gym|miles|work] <value>")
            else:
                stat_type = sys.argv[2]
                try:
                    value = float(sys.argv[3])
                    notes = sys.argv[4] if len(sys.argv) > 4 else ""
                    log_weekly_stat(stat_type, value, notes)
                except ValueError:
                    print("Error: Value must be a number")
        
        elif command == "total":
            gym, miles, work = get_weekly_totals()
            print(f"\n📈 This Week's Totals:")
            print(f"   🏋️ Gym: {gym} sessions")
            print(f"   🏃 Miles: {miles}")
            print(f"   💼 Work: {work} hours")
        
        elif command == "improvements":
            print_improvements()
        
        elif command == "mistakes":
            print_mistakes()
        
        elif command == "trends" or command == "tag-trends":
            days = int(sys.argv[2]) if len(sys.argv) > 2 else 30
            print_tag_trends(days)
        
        # NEW COMMANDS (v2.0)
        elif command == "people":
            # Search for person mentions
            person = sys.argv[2] if len(sys.argv) > 2 else None
            show_people_mentions(person)
        
        elif command == "decisions":
            # Show recent decisions
            limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
            show_recent_decisions(limit)
        
        elif command == "timeline":
            # Show timeline of recent memories
            days = int(sys.argv[2]) if len(sys.argv) > 2 else 7
            show_timeline(days)
        
        elif command == "summary":
            # Quick one-line summary
            days = int(sys.argv[2]) if len(sys.argv) > 2 else 7
            show_quick_summary(days)
        
        elif command == "tags":
            # Filter by specific tag
            tag = sys.argv[2] if len(sys.argv) > 2 else None
            days = int(sys.argv[3]) if len(sys.argv) > 3 else 30
            if tag:
                filter_by_tag(tag, days)
            else:
                print("Usage: fast-search.py tags <tag> [days]")
        
        elif command == "export":
            # Export memories to file
            days = int(sys.argv[2]) if len(sys.argv) > 2 else 7
            output_file = sys.argv[3] if len(sys.argv) > 3 else "memory_export.md"
            export_memories(days, output_file)

        else:
            print(f"Unknown command: {command}")
            print("Usage:")
            print("  python3 fast-search.py rebuild                  # Build/update index")
            print("  python3 fast-search.py analytics                # Show analytics")
            print("  python3 fast-search.py search <query>            # Search memories")
            print("  python3 fast-search.py search <query> --from YYYY-MM-DD")
            print("  python3 fast-search.py search <query> --to YYYY-MM-DD")
            print("  python3 fast-search.py search <query> --this-week")
            print("  python3 fast-search.py search <query> --this-month")
            print("  python3 fast-search.py stats [days]              # Show weekly stats")
            print("  python3 fast-search.py log [type] [val]          # Log a stat")
            print("  python3 fast-search.py total                     # Show this week's totals")
            print("  python3 fast-search.py improvements              # Show improvements log")
            print("  python3 fast-search.py mistakes                  # Show mistakes log")
            print("  python3 fast-search.py trends [days]             # Show tag trends")
            print("  python3 fast-search.py people [name]            # Show people mentions")
            print("  python3 fast-search.py decisions [limit]        # Show recent decisions")
            print("  python3 fast-search.py timeline [days]          # Show timeline view")
            print("  python3 fast-search.py summary [days]            # Quick one-line summary")
            print("  python3 fast-search.py tags <tag> [days]          # Filter by tag")
            print("  python3 fast-search.py export [days] [file]      # Export to file")
    else:
        run_full_index()