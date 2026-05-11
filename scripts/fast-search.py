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

def search(query):
    """Fast search through memories."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    
    results = c.execute(
        "SELECT date, substr(content, 1, 200) FROM memories WHERE content LIKE ? LIMIT 5",
        (f'%{query}%',)
    ).fetchall()
    
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

def run_full_index():
    """Run the full indexing process."""
    print("🚀 Building Memory Search Index...")
    conn = init_database()
    stats = index_memories(conn)
    conn.close()
    
    print("\n✅ Index built successfully!")
    print_analytics(get_analytics())
    
    return stats

# Command line interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "search":
            query = " ".join(sys.argv[2:])
            results = search(query)
            print(f"\n🔍 Search results for '{query}':\n")
            for date, content in results:
                print(f"📅 {date}: {content}...")
        elif sys.argv[1] == "analytics":
            stats = get_analytics()
            print_analytics(stats)
        elif sys.argv[1] == "rebuild":
            run_full_index()
        else:
            print("Usage:")
            print("  python3 fast-search.py rebuild   # Build/update index")
            print("  python3 fast-search.py analytics # Show analytics")
            print("  python3 fast-search.py search [query] # Search memories")
    else:
        run_full_index()