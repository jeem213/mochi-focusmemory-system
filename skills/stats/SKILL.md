---
name: stats
description: Show weekly numeric summaries from memory - gym sessions, miles, work hours, and more. Use when you want to see your stats - says "show my stats", "weekly summary", or "what are my numbers".
license: Proprietary
metadata:
  author: Mochi
  credits: Hybrid memory system inspired by session-context-extractor-v2
  version: "1.1"
  triggers:
    - show my stats
    - weekly summary
    - what are my numbers
    - stats
    - my numbers
  category: memory
  requires:
    - memory
    - filesystem
---

# Stats - Weekly Numeric Summary

This skill shows your weekly numeric summaries from memory - gym sessions, miles run, work hours, and more!

## When to Use This Skill

Triggered when you say:
- "show my stats"
- "weekly summary"
- "what are my numbers"
- "stats"
- "my numbers this week"

---

## The Stats Process

### Step 1: Read Recent Memory Files

Read the last 7 days of memory files from `memory/YYYY-MM-DD.md`

### Step 2: Extract Numeric Data

Look for:
- `* Information:` lines with numbers
- Gym mentions: "gym", "worked out", "exercise"
- Running: "miles", "ran", "run"
- Work: "work hours", "worked X hours"
- Any other numeric data

### Step 3: Aggregate

Count/fold the numeric data:
- Gym sessions = days with gym mention
- Miles = sum of all mile numbers
- Work hours = sum of all hour numbers

### Step 4: SQLITE ANALYTICS (NEW!)

**Use the new SQLite database for instant analytics!**

Run the analytics script:
```bash
/home/openclaw/.venv/bin/python scripts/fast-search.py analytics
```

**This shows:**
- Total memories, decisions, mistakes, improvements
- People mention counts (who we talk about most)
- Tag frequency (what topics dominate)
- Recent decisions

**Add this to your report for POWER analytics!**

---

### Step 5: Format Output

Present in a clean table format with:
- This week's totals
- Comparison to last week (if available)
- Any notable patterns

---

## Example Output

```
📊 Your Weekly Stats (May 4-10, 2026)
=====================================

🏋️ Gym: 3 sessions
   (Last week: 2)

🏃 Miles: 12.5 miles
   (Last week: 8 miles)

💼 Work: 32 hours
   (Last week: 40 hours)

📈 Summary: Great week! More gym and running than last week!
```

---

## What Data Can Be Tracked

Currently supported:
- Gym/workout sessions
- Miles run/walked
- Work hours
- Calories (future)
- Sleep hours (future)

**Just tell me naturally!** "I went to the gym" or "ran 3 miles" and I'll capture it!

---

## Related Skills

- `skills/study` - Full memory refresh
- `skills/sync` - Save session to memory
- `skills/full-sync` - Full system check

---

## Error Handling

| Scenario | What to Do |
|----------|------------|
| No numeric data found | Show \"No data logged yet - just tell me your numbers!\" |
| Only some data found | Show what's available, mark others as TBD |
| Memory files missing | Show partial data, note limitation |

---

## Time Estimate

| Step | Time |
|------|------|
| Read memory files | 10s |
| Extract/aggregate | 5s |
| Format output | 5s |
| **Total** | **~20 seconds** |

---

*Skill version: 1.1 - Updated: May 11, 2026*
*Note: v1.1 - Added SQLite Analytics Step!*
*Part of hybrid memory system - combines semantic memory with structured numeric tracking!*