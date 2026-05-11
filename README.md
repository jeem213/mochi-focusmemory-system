# 🐹 The Heyron Focus Memory System

**Version:** 2.3 | **License:** MIT | **Built by:** Heron AI Community

## Table of Contents
- [What Is This?](#-what-is-this)
- [Why Choose Heyron?](#-why-choose-heyron)
- [Quick Start](#-quick-start-5-minutes)
- [Prerequisites](#prerequisites)
- [How It Works](#-how-it-works)
- [Folder Structure](#-folder-structure)
- [Scripts](#-scripts)
- [Tagging System](#-tagging-system)
- [1% Better System](#-the-1-better-system)
- [Core Files](#-core-files)
- [Examples](#-real-world-examples)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#--faq)
- [Changelog](#-changelog)
- [Contributing](#-contributing)
- [About](#-about-heyron)
- [Quick Reference](#-quick-reference)

---

## What Is This?

A persistent, structured memory system for AI agents that **never forgets**.

Every AI agent has the same problem: forgetting. Conversations end, context is lost, and every new session starts from scratch. Your human has to re-explain everything.

**The Heyron Focus Memory System solves this.**

---

## ✨ Why Choose Heyron?

| Feature | Other Systems | Heyron Focus |
|---------|---------------|-------------|
| **External APIs** | Many require paid services | ✅ Zero dependencies |
| **Structured Memory** | Flat file storage | ✅ People + Decisions + Mistakes folders |
| **Searchable** | Basic keyword only | ✅ Tags + Hybrid Format + Cross-references |
| **Auto-improvement** | None | ✅ 1% Better - 5 syncs OR 3 days (HYBRID)! |
| **Automation** | Manual cleanup | ✅ 3 backup scripts + HEARTBEAT |
| **Easy to use** | Complex setup | ✅ Just 5 words: sync, study, mega-sync, memory-audit, mega-dive |

---

## 🚀 Quick Start (5 Minutes)

```bash
# 1. Copy these folders to your agent workspace:
cp -r skills/ your-workspace/
cp scripts/ your-workspace/
cp memory/ your-workspace/

# 2. Copy the configuration files:
cp SOUL.md your-workspace/
cp AGENTS.md your-workspace/

# 3. Test it works:
# Say "sync" - should save this conversation
# Say "study" - should load all memories
# Say "mega sync" - should show system status
```

### ✅ Verify Installation

```bash
ls -la memory/           # Should show folders (people/, decisions/, etc.)
ls -la skills/           # Should show skill files
cat SOUL.md | head -5   # Should show AI identity
```

If you see output from all three commands, you're ready to go!

## Prerequisites

Before you begin, ensure you have:

- ✅ An AI agent framework (OpenClaw, Claude, GPT, etc.)
- ✅ Git installed (for version control & backups)
- ✅ Write permissions to your workspace folder
- ✅ Terminal access (for running scripts)

**Optional but recommended:**
- 💾 A GitHub repository (for cloud backups)

---

## 💬 How It Works

### Trigger Words

| Trigger | What It Does | Example |
|---------|--------------|---------|
| **sync** | Save conversation to memory + GitHub | "sync now" |
| **study** | Load all memories, catch up instantly | "study" or "catch me up" |
| **mega-sync** | Full system health check | "mega sync" or "check everything" |
| **memory-audit** | Comprehensive memory system audit | "memory audit" or "check memory" |
| **mega-dive** | Deep research + creativity + tech combo | "mega dive" or "deep dive" |

### Example Conversations

```
You: sync
Mochi: Saving this conversation to memory with #important tag! ✅

You: study
Mochi: [Loads all memories...] 
→ Found 3 pending tasks
→ Last chat: May 10, 2026
→ Key decision: Building an AI agent business!

You: mega sync
Mochi: All systems go! ✅
→ Memory: 30 files
→ Skills: 28 loaded
→ GitHub: Connected
→ 1% Better: 3 improvements this month

You: memory audit
Mochi: Running comprehensive audit... ✅
→ Memory files: 47
→ Skills: 34
→ All checks passed! 100% healthy!
```

---

## 📁 Folder Structure

```
memory/
├── people/                  # Contact profiles
│   ├── alex.md             # Clients, team members, family
│   ├── sam.md
│   └── partner.md
├── decisions/               # Organized decisions by topic
│   ├── memory-system.md
│   └── business-pricing.md
├── mistakes/                # Error tracking & lessons
│   └── YYYY-MM-DD.md
├── improvements/            # 1% Better prompts
│   ├── 1percent-better-counter.md
│   └── YYYY-MM.md
├── backups/                # Local timestamped archives
├── auto-learned.md         # Auto-captured learnings
└── YYYY-MM-DD.md          # Daily memory files
```

---

## 🛠️ Scripts

### Backup (Manual)

```bash
bash scripts/backup-memory.sh
# Output: memory/backups/memory_backup_2026-05-10_0531.tar.gz
```

### Restore (Emergency)

```bash
bash scripts/restore-latest.sh
# Restores from most recent backup
```

### Monthly Archive (Automatic)

Runs on the 1st of each month:
- Finds memories older than 30 days
- Creates monthly summaries
- Archives old files to save space

---

## 🏷️ Tagging System

### Priority Tags

| Tag | When to Use |
|-----|-------------|
| `#important` | Key decisions, milestones, big moments |
| `#routine` | Casual chat, regular updates |

### Category Tags

| Tag | Category |
|-----|----------|
| `#business` | Work, money, startup |
| `#personal` | Family, hobbies |
| `#technical` | Code, setup, integrations |

### Topic Tags

| Tag | Topic |
|-----|-------|
| `#skills` | New skills created |
| `#rules` | Rules changes |
| `#team` | Collaboration |

---

## 🔄 The 1% Better System

Every 5 sync sessions, the agent asks:

> *"What's one thing I could do better?"*

Responses are saved to `memory/improvements/YYYY-MM.md`.

**This is continuous improvement - small, consistent, compounding growth!**

---

## 📋 Core Files

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

## 💡 Real-World Examples

### Scenario 1: Returning User

**Without Mochi:**
```
You: Hi! Who am I?
Agent: I don't know. Who are you?
```

**With Mochi:**
```
You: Hi! Who am I?
Agent: Hey there! You run a small business in Seattle,
married to Sam (birthday July 15), birthday March 22!
You have a cat named Whiskers. What can I help with?
```

### Scenario 2: Past Decision

**Without Mochi:**
```
You: What did we decide about pricing?
Agent: I don't have that information.
```

**With Mochi:**
```
You: What did we decide about pricing?
Agent: You decided on $29/month for launch, stored in 
decisions/business-pricing.md on April 15, 2026.
Also noted: early adopters get 30% off.
```

### Scenario 3: Error Prevention

**Without Mochi:**
```
You: What mistake did we make with the API?
Agent: I don't recall.
```

**With Mochi:**
```
You: What mistake did we make with the API?
Agent: On April 12, you found that the API rate limit 
was too low. Fixed by upgrading to paid tier.
Stored in mistakes/2026-04-12.md for future reference.
```

---

## ❓ Troubleshooting

### "sync" doesn't save anything

**Check:**
1. Does the `memory/` folder exist?
2. Do you have write permissions?
3. Is Git initialized? (`git init`)

### "study" shows old information

**Fix:**
1. Run `mega sync` to force refresh
2. Check memory files for syntax errors
3. Verify GitHub remote is configured

### GitHub backup fails

**Verify:**
1. GitHub remote is set: `git remote -v`
2. Authentication works (SSH key or token)
3. Branch name matches (main vs master)

### Nothing happens when I say trigger words

**Debug:**
1. Check SOUL.md has the trigger defined
2. Verify skills/ folder is copied correctly
3. Run `mega sync` to see what's loaded

---

## 🙋 FAQ

**Q: Does this work with Claude?**
A: Yes! Works with any AI agent that can read/write files and run commands.

**Q: Can I use it with multiple agents?**
A: Absolutely - each agent can have its own memory folder, or share one with proper tagging.

**Q: How much storage does it need?**
A: Very little - text files are KB. Even with years of memories, you'll likely use under 100MB.

**Q: Is my data secure?**
A: Your memories stay local unless you choose to push to GitHub. You control everything.

**Q: Can I import existing conversations?**
A: Yes! Just create memory files in the format shown and run `study` to load them.

---

## 📝 Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | May 10, 2026 | Initial release - Hybrid memory system |
| 2.0 | May 10, 2026 | Added 1% Better improvements |
| 2.1 | May 10, 2026 | Added troubleshooting, FAQ, real examples |
| 2.2 | May 11, 2026 | Added memory-audit and mega-dive skills, updated 1% Better to HYBRID system|

---

## 🤝 Contributing

1. Open an issue on GitHub
2. Check the `skills/` folder for detailed documentation
3. Run `study` to see current memory state

---

## 🐹 About Mochi

The Heyron Focus Memory System was built by the Heron AI Community to solve a universal problem: **how to make AI agents remember**.

Mochi is the Memory Expert + Rules Expert of any AI family - she handles all memory operations, skill updates, and continuous improvement!

---

## 🎯 Quick Reference

| Command | Action |
|---------|--------|
| `sync` | Save current conversation to memory + GitHub |
| `study` | Load all memories and catch up |
| `mega-sync` | Full system health check |
| `backup-memory.sh` | Create manual backup |
| `restore-latest.sh` | Restore from latest backup |

---

## 📜 License

**MIT** - Free to use, modify, and share!

---

## 🌟 Build Forever

> Remember everything. Improve every session. Build forever.

**Built by the Heron AI Community, for the Heron AI Community** 🐹💜

[![Heron AI Community](https://img.shields.io/badge/Heron-AI Community-blue)](https://github.com/jeem213)
[![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-green)](https://github.com/jeem213)

---

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-2.2-blue)](https://github.com/jeem213/mochi-focusmemory-system)
[![AI Ready](https://img.shields.io/badge/AI-Ready-green)](https://github.com/jeem213/mochi-focusmemory-system)