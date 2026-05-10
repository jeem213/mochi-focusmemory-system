---
name: decisions
description: Auto-promote decisions from memory files to organized decisions folder. Runs automatically on sync or manually. Use when you want to organize decisions - says "promote decisions", "organize decisions", or "decisions".
license: Proprietary
metadata:
  author: Jeem & Mochi
  credits: "Created by Jeem & Mochi"
  version: "1.0"
  triggers:
    - promote decisions
    - organize decisions
    - decisions
    - decision check
  category: memory
  requires:
    - filesystem
    - bash
---

# Decisions Skill - Auto-Promote Decisions

This skill automatically scans memory files for #decision tags and promotes them to the organized decisions folder. It makes decisions findable and searchable!

## When to Use This Skill

Triggered when the user says:
- "promote decisions"
- "organize decisions"
- "decisions"
- "decision check"

Or runs automatically after every sync!

---

## What It Does

1. **Scans** recent memory files (last 30 days)
2. **Finds** all #decision tags
3. **Extracts** decision text
4. **Promotes** to memory/decisions/ folder
5. **Deduplicates** - won't add same decision twice
6. **Reports** what was promoted

---

## The Decision Promotion Process (4 Steps)

### Step 1: SCAN MEMORY FILES

Scan recent memory files for #decision tags:
```bash
grep -r "#decision" memory/*.md
```

Also check for inline Decision: patterns:
```bash
grep "^[\*•] Decision:\|^\*\*Decision:" memory/*.md
```

### Step 2: EXTRACT DECISIONS

For each #decision found:
- Extract the decision text
- Note which file it came from
- Note the date (from filename)

### Step 3: PROMOTE TO DECISIONS FOLDER

For each new decision:
1. Check if it already exists in memory/decisions/
2. If not, add to appropriate topic file
3. Create new topic file if needed

### Step 4: REPORT

Report to user:
- Total decisions found
- Total new decisions promoted
- Total duplicates skipped

---

## Decision Topics

The skill organizes decisions by topic:

| Topic File | Contains |
|------------|-----------|
| memory-system.md | Memory system decisions |
| momo-creation.md | Momo-related decisions |
| *(others)* | Created as needed |

---

## Auto-Promotion

This skill is called automatically by sync v2.1+ after saving memory!

Every time you sync, decisions are automatically organized.

---

## Manual Trigger

You can also run manually:

```
You: promote decisions
Mochi: 🔍 Scanning memory files...
📋 Found 5 decisions in today's session
✅ Promoted 3 new decisions
⏭️ Skipped 2 duplicates
📁 Updated: memory/decisions/memory-system.md
```

---

## Example Output

```
🔍 Starting decision auto-promotion...
📋 Found decisions in 2026-05-10
PROMOTED: : Published memory system to public repo
PROMOTED: : Added 1% Better improvement feature

🔍 Checking for Decision: patterns...

✅ Decision promotion complete!
📋 Total decisions promoted: 2
📁 Updated: memory/decisions/memory-system.md
```

---

## Notes

- Only scans last 30 days of memory
- Won't duplicate existing decisions
- Creates topic files automatically
- Runs silently on sync (no extra output)
- Can be run manually anytime

---

*Skill version: 1.0 - Created: May 10, 2026*
*Part of Mochi Focus Memory System v2.1*