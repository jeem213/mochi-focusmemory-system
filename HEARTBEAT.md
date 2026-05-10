# HEARTBEAT.md - Periodic Tasks

```markdown
# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.
```

---

# Periodic Tasks

## Weekly Tasks (Every 7 days)

### Weekly Memory Backup
- **When:** Every 7 days (Weekly)
- **Trigger:** Run: `bash scripts/backup-memory.sh`
- **Action:** Creates timestamped backup of memory folder
- **Notes:** Keeps last 7 backups automatically

### Daily Memory Backup (OPTIONAL)
- **When:** Every 1 day (Daily) - OPTIONAL
- **Trigger:** Run: `bash scripts/backup-daily.sh`
- **Action:** Creates daily timestamped backup
- **Notes:** Keeps last 14 daily backups, more aggressive cleanup
- **Use instead of weekly for more frequent backups**

### Decision Auto-Promotion
- **When:** Every sync (automatic)
- **Trigger:** Run: `bash scripts/promote-decisions.sh`
- **Action:** Scans memory files for #decision tags, promotes to decisions/
- **Notes:** Called by sync skill automatically!

### Weekly Archive (Start of Month)
- **When:** 1st day of each month
- **Trigger:** Run: `bash scripts/weekly-archive.sh`
- **Action:** Moves files older than 30 days to memory/archive/
- **Notes:** Keeps memory folder clean

---

## Quarterly Tasks (Every 3 months)

### Rules Review
- **When:** Every 3 months (Quarterly)
- **Trigger:** Run `skills/rules-audit` 
- **Action:** Review SOUL.md + AGENTS.md for updates needed
- **Notes:** Check best practices, update rules if needed
- **Last Run:** 2026-05-07 (first run!)

---

*Last updated: 2026-05-10*
*Added: Weekly backup + monthly archive tasks*