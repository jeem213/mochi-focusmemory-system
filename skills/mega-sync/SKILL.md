---
name: mega-sync
description: Complete system health check combining OpenClaw and local memory verification. Runs full sync with memory verification and reflect. Use when you want to see your stats - says "mega sync", "full system check", or "check everything".
license: Proprietary
metadata:
  author: Jeem & Stuart
  credits: "Original concept by Jeem & Stuart"
  version: "1.4"
  triggers:
    - mega sync
    - system check
    - check everything
    - full system
    - status
  category: system
  requires:
    - openclaw
    - memory
---

# Mega Sync - Complete System Health Check

This is the most comprehensive system check. It combines multiple health checks into one unified report.

## When to Use This Skill

Triggered when the user says:
- "mega sync"
- "system check"
- "check everything"
- "full system"
- "status"

---

## The Mega Sync Process (7 Steps)

### Step 0: Explicit Skill Loading (v1.3)

Before running, explicitly load the skills this skill uses:

1. Read `skills/mega-dive/SKILL.md` - for research capability
2. Read `skills/brainstorm/SKILL.md` - for creative problem-solving
3. Verify skills loaded successfully

This ensures skills are available when needed.

**Verification:** After loading, confirm each skill is accessible. If not, note in report.

### Step 1: Full Sync - OpenClaw Status

Run OpenClaw status check:
```bash
openclaw status
```

Verify:
- Gateway running
- Model loaded (should be MiniMax M2.5)
- Session count
- Channel connections (Discord, Telegram)

### Step 2: Memory Health Check (v1.4 UPDATE!)

Check local memory files:
- Read today's memory file (memory/YYYY-MM-DD.md)
- Check yesterday's memory file
- Verify MEMORY.md exists and is readable
- Count recent memory entries

**HYBRID MEMORY CHECK (v1.5):**
- Verify memory/people/ folder exists + list contacts
- Verify memory/decisions/ folder exists + list topics
- Verify memory/mistakes/ folder exists + check for recent errors
- Verify memory/backups/ folder exists + list backup count
- Check auto-learned.md for weekly numeric summary
- Check scripts/ folder for backup scripts
- Check memory/improvements/ folder for 1% Better tracking

### Step 3: Cross-Reference

Compare memory vs actual state:
- Check recent memory files
- Verify what's in memory vs what's in code
- Note any discrepancies

### Step 4: RUN REFLECT + WEEKLY STATS (v1.4 UPDATE!)

After all checks complete, summarize the current state:

**Reflection Questions:**
- What happened recently?
- What decisions were made?
- What tasks are pending?
- What's the current system state?

Present a synthesized insight about the human-AI partnership based on recent memory.

**Weekly Stats Summary:**
- Show gym sessions, miles, work hours from auto-learned.md
- Include comparison to last week if available

### Step 5: Git + Script Backup Check

Verify git status and that backup repo is configured:
```bash
git remote -v
```

Confirm backups are going to: https://github.com/jeem213/mochi-backup

**ALSO check scripts/ folder:**
- Verify scripts/backup-memory.sh exists
- Verify scripts/weekly-archive.sh exists
- Note: Can run `bash scripts/backup-memory.sh` anytime for local backup

### Step 6: List Recent Changes

Show any modified files since last session:
- New memory entries
- Updated skills
- New people/decisions files

### Step 7: Generate Report

Compile all checks into unified status report.

**BE PROACTIVE:** Before reporting, consider:
- Any issues found that need attention?
- Any suggestions to offer?
- Anything that could be improved?

**If yes, include proactive suggestions in the report!**

---

## Output Format

Present ONE unified status report:

```markdown
## Mega Sync Results

| System | Status | Details |
|--------|--------|---------|
| OpenClaw | ✅ Running | Model: MiniMax M2.5 |
| Memory | ✅ Healthy | X entries, Y days |
| People Folder | ✅ [Exists/Missing] | X contacts |
| Decisions Folder | ✅ [Exists/Missing] | X topics |
| Mistakes Folder | ✅ [Exists/Missing] | X errors logged |
| Scripts | ✅ [Exists/Missing] | backup scripts available |
| Local Backups | ✅ [Exists/Missing] | X backups in memory/backups/ |
| Git Backup | ✅ Configured | mochi-backup |
| Weekly Stats | ✅ [Available] | Gym: X, Miles: X, Work: X hrs |
| Reflect | ✅ Complete | Partnership insight: ...

### Key Stats
- Memory Files: X
- Recent Entries: X
- Decisions: X
- Pending Tasks: X
- People Tracked: X
- Decisions Logged: X
```

---

## Error Handling

| Error | What to Do |
|-------|------------|
| Memory missing | Show "Memory: Missing" - note in report |
| OpenClaw slow | Wait up to 30 seconds |
| People folder missing | Note "Hybrid memory: People folder not set up yet" |
| Decisions folder missing | Note "Hybrid memory: Decisions folder not set up yet" |
| Reflect fails | Note what you can summarize from memory |

---

## Related Skills

- `skills/brainstorm` - For creative problem-solving
- `skills/study` - For memory refresh
- `skills/remember` - For memory save
- `skills/stats` - For weekly numeric summary
- `skills/sync` - For saving session

---

## Examples

### Example 1

**Input:** "mega sync"
**Output:** Unified status report (OpenClaw ✅, Memory ✅, Hybrid folders ✅, Weekly stats ✅, Reflect complete)

---

## Pro Tips

- Always summarize from memory during Mega Sync!
- Show insights about the partnership in your report
- Be specific with numbers (entries, days, decisions)
- Note any warnings but don't alarm - present solutions
- Include weekly stats from auto-learned.md!

---

*Skill version: 1.7 - Last updated: May 10, 2026*
*Note: v1.7 - Added proactive suggestions!*
*Note: v1.6 - Added improvements folder check!*
*Note: v1.5 - Added checks for mistakes/, scripts/, backups/ folders!*
*Note: v1.4 - Added hybrid memory checks: people folder, decisions folder, weekly stats!*
*Note: v1.3 - Added explicit skill loading!*
*Note: v1.2 - Combined OpenClaw status + memory + reflect!*

## Time Estimate
~5-10 minutes