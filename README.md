# 🐹 Mochi Focus Memory System

*A persistent, structured memory system for AI agents that NEVER forgets.*

---

## The Problem

Every AI agent has the same problem: **forgetting**. Conversations end, context is lost, and every new session starts from scratch. Your human has to re-explain everything.

**Mochi Focus Memory System solves this.**

---

## What Makes It Different

| Feature | Other Systems | Our System |
|---------|---------------|------------|
| External APIs | Many require paid services | **Zero dependencies** |
| Structured Memory | Flat file storage | **People + Decisions + Mistakes folders** |
| Searchable | Basic keyword only | **Tags + Hybrid Format + Cross-references** |
| Auto-improvement | None | **1% Better - every 5 sessions!** |
| Automation | Manual cleanup | **3 backup scripts + HEARTBEAT** |
| Easy to use | Complex setup | **Just 3 words: sync, study, mega-sync** |

---

## Features

### Core Memory

- ✅ **Persistent memory** - Remembers across sessions
- ✅ **Hybrid format** - Semantic + structured fact format
- ✅ **People folder** - Contact profiles (family, friends, team)
- ✅ **Decisions folder** - Organized by topic
- ✅ **Mistakes tracking** - Learn from errors
- ✅ **1% Better** - Continuous improvement every 5 sessions

### Automation

- ✅ **GitHub backup** - Every sync pushes to GitHub
- ✅ **Local backups** - Timestamped archives
- ✅ **HEARTBEAT** - Scheduled tasks (weekly backup, monthly archive)
- ✅ **Python backups** - Enhanced zip backups with manifest

### Python Scripts (v2.3 - NEW!)

*Requires: Python 3 + beautifulsoup4 (pip install beautifulsoup4)*

| Script | Purpose | Command |
|--------|---------|---------|
| **memory-report.py** | HTML dashboard | `python scripts/memory-report.py` |
| **fast-search.py** | SQLite analytics | `python scripts/fast-search.py analytics` |
| **python-backup.py** | Enhanced backup | `python scripts/python-backup.py backup` |
| **web-research.py** | HTML parsing | `python scripts/web-research.py fetch <url>` |

### Skills (35 Total!)

| Skill | Purpose |
|-------|---------|
| **sync** | Save conversation to memory + GitHub |
| **study** | Load all memories, catch up instantly |
| **mega-sync** | Full system health check |
| **stats** | Weekly numeric summaries |
| **+ 28 more** | Analysis, brainstorming, creativity, etc. |

---

## Quick Start

### 1. Copy to Your Agent

```bash
# Copy these folders to your agent workspace:
cp -r skills/ your-workspace/
cp scripts/ your-workspace/
cp memory/ your-workspace/
```

### 2. Copy the Rules

```bash
# These define how the agent behaves:
cp SOUL.md your-workspace/
cp AGENTS.md your-workspace/
```

### 3. Start Using It

```
You: sync
Mochi: Saving this conversation to memory with #important tag!

You: study
Mochi: [Loads all memories...]

You: mega sync
Mochi: All systems go! Memory: ✅ Skills: ✅ GitHub: ✅
```

---

## The Skills

### 🔄 Sync (v2.0)

**Trigger Words:** sync, sync now, save

Saves the current conversation with MANDATORY tagging:
- Creates `memory/YYYY-MM-DD.md`
- Requires tags: #important or #routine
- Auto-increments 1% Better counter
- Backs up to GitHub automatically

### 📚 Study (v1.8)

**Trigger Words:** study, refresh memory, catch me up

Loads everything to get you up to speed:
- Reads all memory files (past 7 days)
- Checks people/, decisions/, mistakes/, improvements/
- Shows weekly stats
- Filters by priority

### 🔬 Mega Sync (v1.6)

**Trigger Words:** mega sync, system check, check everything

Complete health check:
- Verifies all memory folders exist
- Counts GitHub commits
- Shows 1% Better progress
- Reports system status

---

## Memory Structure

```
memory/
├── people/           # Contact profiles
│   ├── sara.md       # Family, friends, team
│   ├── stuart.md
│   ├── momo.md
│   └── hank.md
├── decisions/        # Organized decisions
│   ├── memory-system.md
│   └── momo-creation.md
├── mistakes/         # Error tracking
│   └── YYYY-MM-DD.md
├── improvements/     # 1% Better prompts
│   ├── 1percent-better-counter.md
│   └── YYYY-MM.md
├── backups/          # Local timestamped backups
├── auto-learned.md   # Auto-captured learnings
└── YYYY-MM-DD.md    # Daily memory files
```

---

## The Scripts

### backup-memory.sh

Creates timestamped local backup:
```bash
bash scripts/backup-memory.sh
# Output: memory/backups/memory_backup_2026-05-10_0531.tar.gz
```

### weekly-archive.sh

Runs on 1st of month:
- Finds memories older than 30 days
- Creates monthly summaries
- Archives old files

### restore-latest.sh

Restores from latest backup:
```bash
bash scripts/restore-latest.sh
```

---

## The 1% Better System

Every 5 sync sessions, the agent asks:

> "What's one thing I could do better?"

Responses are saved to `memory/improvements/YYYY-MM.md`.

**This is continuous improvement - small, consistent, compounding growth!**

---

## Tags Reference

### Priority Tags

| Tag | When to Use |
|-----|-------------|
| #important | Key decisions, milestones, big moments |
| #routine | Casual chat, regular updates |

### Category Tags

| Tag | Category |
|-----|----------|
| #business | Work, money, startup |
| #personal | Family, hobbies |
| #technical | Code, setup, integrations |

### Topic Tags

| Tag | Topic |
|-----|-------|
| #skills | New skills created |
| #rules | Rules changes |
| #team | Collaboration |

---

## Rules & Configuration

### SOUL.md

Defines the agent's identity, rules, and boundaries:
- Memory system documentation
- Safety guidelines
- Communication rules

### AGENTS.md

Workspace configuration:
- Memory folders
- Skills overview
- User preferences
- Platform rules

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | May 10, 2026 | Initial release - Hybrid memory system |
| 2.0 | May 10, 2026 | Added 1% Better improvements |
| 2.3 | May 11, 2026 | Added Python Scripts: memory-report, fast-search, python-backup, web-research |
| 2.4 | May 11, 2026 | Python scripts now included in repo! |

---

## Built With Love

**Mochi Focus Memory System** was built by Jeem & Mochi (baby capybara).

Mochi is the Memory Expert + Rules Expert of the AI family - she handles all memory operations, skill updates, and continuous improvement!

---

## License

MIT - Free to use, modify, and share!

---

## Questions?

- Open an issue on GitHub
- Check the skills/ folder for detailed documentation
- Run `study` to see current memory state

---

**Remember everything. Improve every session. Build forever.** 🐹💜

*Made with ❤️ by Jeem & Mochi*