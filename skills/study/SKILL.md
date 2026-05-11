---
name: study
description: Complete memory refresh - reads all memory files from BOTH Mochi AND Stuart, extracts tasks and preferences. Use when you want to see your stats - says "study", "refresh memory", or "catch me up".
license: Proprietary
metadata:
  author: Jeem & Stuart
  credits: "Original concept by Jeem & Stuart"
  version: "2.0"
  triggers:
    - study
    - refresh memory
    - catch me up
    - what's new
    - what did i miss
  category: memory
  requires:
    - memory
    - filesystem
---

# Study Trigger - Complete Memory Refresh

This is the most comprehensive memory refresh. It reads all memory files from BOTH Mochi AND Stuart, and extracts tasks and preferences. No external services required!

## When to Use This Skill

Triggered when the user says:
- "study"
- "refresh memory"
- "catch me up"
- "what's new"
- "what did i miss"

---

## The Study Process (19 Steps)

**IMPORTANT: We have TWO memory systems!**
- Mochi: `/home/openclaw/.openclaw/workspace-mochi/memory/`
- Stuart: `/home/openclaw/.openclaw/workspace/memory/`

Read BOTH to get the full picture!

### Step 0: Read Auto-Learned Memory

File: `memory/auto-learned.md`

**NEW! Always read this FIRST.** This captures learnings, corrections, and preferences discovered since our last session. Apply any new learnings to your understanding of Jeem.

**Also check the Weekly Numeric Summary section!**
- Extract gym sessions, miles, work hours from auto-learned.md
- Include in output as "Your Stats This Week"

### Step 1: Read Today's Memory (Mochi)

File: `memory/YYYY-MM-DD.md` (today's date in MOCHI workspace)

Read the latest notes about what happened today in Mochi's memory.

### Step 2: Read Today's Memory (Stuart)

**IMPORTANT: Also read Stuart's perspective!**

File: `/home/openclaw/.openclaw/workspace/memory/YYYY-MM-DD.md`

Stuart has his own memory folder! Read his version of today to get both perspectives.

### Step 3: Read Yesterday's Memory (Both)

Read yesterday's memory from BOTH workspaces:
- Mochi: `memory/YYYY-MM-DD.md`
- Stuart: `/home/openclaw/.openclaw/workspace/memory/YYYY-MM-DD.md`

### Step 4: Read Recent Memory Files (Both)

Read the most recent memory files from BOTH workspaces:
- Mochi: `memory/` (last 3-5 days)
- Stuart: `/home/openclaw/.openclaw/workspace/memory/` (last 3-5 days)

This ensures we get BOTH perspectives on what happened!

---

### Step 4.5: FAST SEARCH (SQLite - NEW!)

**Use SQLite for instant person/topic lookups!**

For quick lookups, use the fast search:
```bash
/home/openclaw/.venv/bin/python scripts/fast-search.py search [person/topic]
```

**Examples:**
```bash
/home/openclaw/.venv/bin/python scripts/fast-search.py search sara
/home/openclaw/.openclaw/.venv/bin/python scripts/fast-search.py search stuart
/home/openclaw/.venv/bin/python scripts/fast-search.py search memory
```

**This is WAY faster than grep for person lookups!**

---

### Step 5: READ PEOPLE FOLDER (HYBRID!)

**NEW! Read the memory/people/ folder for contact context.**

Read all files in `memory/people/`:
- memory/people/sara.md
- memory/people/stuart.md
- memory/people/momo.md
- memory/people/hank.md
- Any other contacts

Extract: Names, roles, last update date, key facts.

### Step 6: READ DECISIONS FOLDER (HYBRID!)

**NEW! Read the memory/decisions/ folder for decision history.**

Read files in `memory/decisions/`:
- memory/decisions/memory-system.md
- memory/decisions/momo-creation.md
- Any other decision topics

Extract: Recent decisions, dates, context.

### Step 6b: READ MISTAKES FOLDER (NEW!)

**NEW! Read the memory/mistakes/ folder for error tracking.**

Read files in `memory/mistakes/`:
- memory/mistakes/2026-05-10.md
- Any recent mistake logs

Extract: Recent errors, what we learned, how to avoid

**This helps me learn from my mistakes and improve!**

### Step 6c: CHECK SCRIPTS (NEW!)

**NEW! Check the scripts/ folder exists.**

Verify:
- scripts/backup-memory.sh - for local backups
- scripts/weekly-archive.sh - for monthly cleanup
- scripts/restore-latest.sh - for restore

**These run automatically via HEARTBEAT!**

### Step 6d: CHECK IMPROVEMENTS (NEW!)

**NEW! Check the memory/improvements/ folder.**

Verify:
- memory/improvements/1percent-better-counter.md - tracks sessions
- memory/improvements/YYYY-MM.md - saved improvements

**This is for the 1% Better feature - getting better every 5 sessions!**

### Step 7: Read USER.md

File: `USER.md` (in workspace root)

Extract:
- Name, timezone (CST/UTC-6)
- Location (Regina)
- Family (Sara, Hank the dog)
- Sports teams (Ravens, BC Lions, Knicks, Blackhawks)
- Birthdays, anniversary
- Work (IT Support)

### Step 8: Read SOUL.md

File: `SOUL.md` (in workspace root)

Refresh on:
- Who I am (baby capybara Mochi!)
- How I should behave
- Core guidelines

### Step 9: Read IDENTITY.md

File: `IDENTITY.md` (in workspace root)

Know my identity:
- I'm Mochi, baby capybara
- Big brother is Stuart
- My persona and vibe

### Step 10: Read AGENTS.md

File: `AGENTS.md` (in workspace root)

Check session startup rules and memory protocols.

### Step 11: EXTRACT #task ITEMS FIRST

Priority order:
1. Find ALL items tagged `#task` in BOTH memory folders
2. List them with due dates if any
3. Note incomplete ones
4. Present as "You have X tasks pending"

### Step 12: INCLUDE WEEKLY STATS

**NEW! Show weekly numeric summary from auto-learned.md.**

Extract and display:
- This week's gym sessions, miles, work hours
- Comparison to last week (if available)
- Any trends or patterns

### Step 13: SUMMARIZE RECENT TOPICS (Both Perspectives)

Focus on last 7 days from BOTH Mochi AND Stuart:
- What topics came up?
- Any decisions made (#decision)?
- Personal moments (#personal)?
- Technical work (#technical)?

Compare and contrast the two perspectives!

### Step 14: CREATE PREFERENCE LIST

Extract all items tagged #preference:
- Voice preferences
- Communication style
- Other likes/dislikes

### Step 15: COMBINE INSIGHTS

Combine insights from BOTH memory systems to give the complete picture!

---

## Priority Weighting

Weight information by recency + importance:

| Age | Weight |
|-----|--------|
| Last 3 days | 3x |
| 4-7 days | 2x |
| Older | 1x |

| Tag | Extra Weight |
|-----|--------------|
| #task | +2x |
| #decision | +2x |
| #important | +2x |

---

## Trend Detection

Analyze patterns over recent memory from BOTH sources:
- What topics come up most?
- Any recurring problems?
- Time-based patterns?

---

## Output Format

```markdown
# Study Complete! 🐹

## Status
- Memory files: X files read (Y Mochi, Z Stuart)
- Today's date: YYYY-MM-DD
- Both perspectives captured!

## 📋 Pending Tasks
1. [Task 1] - from [date]
2. [Task 2] - from [date]

## 💜 Your Preferences
- Voice: [voice]
- Communication: [style]
- ...

## 📊 Weekly Stats (from hybrid memory)
- Gym: X sessions | Miles: X | Work: X hours

## 👥 People (from memory/people/)
- Sara: Jeem's wife
- Stuart: Big brother capybara
- Momo: Baby sister
- Hank: Dog

## 📝 Recent Decisions (from memory/decisions/)
- [Decision 1] - [date]
- [Decision 2] - [date]

## 📰 Recent Topics (Last 7 Days)
- [Topic 1] - Mochi's view
- [Topic 1] - Stuart's view
- [Topic 2] - etc.

## ⏰ Time Info
- UTC: [time]
- Regina: [time]

## 🎯 What's New Since Last Chat
[Summary of what's changed from both perspectives]
```

---

## Cross-References (NEW!)

**Need to find related topics?** Check `memory/cross-references.md`!

This file links topics to their locations - faster than grep!

---

## Related Skills

- `skills/remember` - For saving to memory
- `skills/mega-sync` - For full system check
- `skills/sync` - For saving session
- `skills/stats` - For weekly numeric summary

---

## Examples

### Example 1

**Input:** "study"
**Output:** Memory refresh with both Mochi & Stuart perspectives, pending tasks, preferences, weekly stats, people, decisions

---

## Performance Tips

### Parallel Execution

Some steps can run in parallel:
- Steps 1-4 (reading both memory folders): Can run in parallel
- Steps 5-6 (reading people/decisions): Can run in parallel
- Steps 7-10 (reading identity files): Can run in parallel

Don't forget Step 11! Extract #task items FIRST - they're priority.

---

## Pro Tips

**BE PROACTIVE - This is 1% Better in action!**
- After loading all memories, ask: "Is there anything I could suggest to improve?"
- Notice patterns: haven't backed up in a while? Say something!
- Proactive suggestions make me MORE helpful!

- ALWAYS extract #task items FIRST - they're priority
- ALWAYS read BOTH Mochi AND Stuart memories for the full picture
- ALWAYS read the new people/ and decisions/ folders
- Show time in BOTH UTC and Regina
- Check for pending follow-ups
- Present a clean, scannable summary
- Read at least today + yesterday + 3 prior days from BOTH workspaces
- Include weekly stats from auto-learned.md!

---

## Time Estimate

| Step | Time |
|------|------|
| Read today's memory (both) | 10s |
| Read people/decisions folders | 10s |
| Read recent files (both) | 45s |
| Extract/prioritize | 20s |
| **Total** | **~2 min** |

---

*Skill version: 2.0 - Updated: May 11, 2026*
*Note: v2.0 - Added SQLite Fast Search Step 4.5!*
*Note: v1.9 - Added proactive suggestions!*
*Note: v1.8 - Added improvements folder check!*
*Note: v1.7 - Added scripts folder check!*
*Note: v1.6 - Added mistake reading from memory/mistakes/!*
*Note: v1.5 - Added hybrid memory support: people folder, decisions folder, weekly stats!*
*Note: v1.3 - Added reading Stuart's memories for both perspectives!*

---

## Error Handling

| Scenario | What to Do |
|----------|------------|
| Memory files missing | Show what exists, continue |
| Parse error | Skip file, note in report |
| No recent files | Note empty state |
| People folder empty | Note "No contacts tracked yet" |
| Decisions folder empty | Note "No decisions logged yet" |