---
name: memory-audit
description: Comprehensive memory system audit - checks all memory files, skills, backups, and configurations for issues. Use when you need to verify your memory system is healthy.
license: Proprietary
metadata:
  author: Mochi
  credits: Inspired by 2026-05-11 mega dive audit
  version: "1.1"
  triggers:
    - memory audit
    - audit memory
    - check memory
    - memory system check
    - memory health
  category: memory
  requires:
    - filesystem
    - exec
    - memory_search
---

# Memory Audit Skill (v1.1)

Comprehensive audit of the memory system to ensure everything is working perfectly.

## When to Use This Skill

Triggered when Jeem says:
- "memory audit"
- "audit memory"  
- "check memory"
- "memory system check"
- "memory health"

Also runs automatically during:
- `full-sync` skill
- `mega-sync` skill

---

## The Audit Process (6 Steps)

### STEP 1: Check for Stray/Typo Files

**What to check:**
- Find all `*.used` files (my old typo issue!)
- Find duplicate files (e.g., auto-learned.md in both root and memory/)
- Check for any .md files in wrong locations

**Commands:**
```bash
find ~/.openclaw/workspace-mochi -name "*.used" 2>/dev/null
ls -la ~/.openclaw/workspace-mochi/*.md
```

**Fix if found:**
- Merge content into proper location
- Delete stray files

---

### STEP 2: Verify Memory Folders Exist

**Required folders:**
- `memory/people/` - Contact profiles
- `memory/decisions/` - Decision logs
- `memory/mistakes/` - Error tracking
- `memory/improvements/` - 1% Better prompts
- `memory/backups/` - Local backups

**Commands:**
```bash
ls -la memory/people/
ls -la memory/decisions/
ls -la memory/mistakes/
ls -la memory/improvements/
ls -la memory/backups/
```

**Fix if missing:**
- Create missing folders
- Add README.md explaining purpose

---

### STEP 2.5: Verify Key Memory Files Exist

**Critical files that MUST exist:**
- `memory/permanent.md` - Long-term curated memory
- `memory/auto-learned.md` - Auto-captured learnings

**Commands:**
```bash
ls -la memory/permanent.md
ls -la memory/auto-learned.md
```

**Fix if missing:**
- If permanent.md missing: Create with template
- If auto-learned.md missing: Create with template

---

### STEP 2.6: Verify People Files Exist

**Required people files (all 4):**
- `memory/people/sara.md` - Jeem's wife
- `memory/people/stuart.md` - Big brother capybara
- `memory/people/momo.md` - Baby sister capybara
- `memory/people/hank.md` - Doggo

**Commands:**
```bash
ls memory/people/
```

**Checklist:**
- [ ] sara.md exists
- [ ] stuart.md exists
- [ ] momo.md exists
- [ ] hank.md exists

**Fix if missing:**
- Create missing person file with template

---

### STEP 3: Check Configuration Files

**Files to verify:**
- `SOUL.md` - Identity and rules
- `USER.md` - User profile
- `AGENTS.md` - Workspace config
- `IDENTITY.md` - My identity

**Check AGENTS.md specifically:**
- Verify it points to `memory/permanent.md` (NOT MEMORY.md which doesn't exist)
- Verify session startup instructions are correct

**Command:**
```bash
grep -n "memory/permanent.md" AGENTS.md
```

---

### STEP 4: Verify Today's Memory Exists

**What to check:**
- Today's memory file exists (memory/YYYY-MM-DD.md)
- If not, create it

**Commands:**
```bash
date +%Y-%m-%d  # Get current date
ls memory/YYYY-MM-DD.md  # Check if exists
```

---

### STEP 5: Test Memory Functionality

**Tests to run:**
1. **Memory Search Test:**
   ```bash
   memory_search(query="test")
   ```
   Should return results

2. **Skill Count Check:**
   ```bash
   ls skills/ | wc -l
   ```
   Should have 25+ skills

3. **Backup Scripts Check:**
   ```bash
   ls scripts/backup*.sh
   ls scripts/weekly-archive.sh
   ```
   Scripts should exist

4. **Model Check:**
   ```bash
   session_status
   ```
   Verify MiniMax M2.5 (or configured preference)

---

### STEP 5.5: Verify Skills Have SKILL.md

**What to check:**
- Every skill folder should have a SKILL.md file
- This ensures all skills are properly configured

**Command:**
```bash
ls skills/*/SKILL.md | wc -l
```

**Expected:**
- Skill count should equal SKILL.md count
- If mismatch: Some skills are missing documentation!

**Fix if mismatch:**
- Identify which skills are missing SKILL.md
- Note for manual review

---

### STEP 5.6: Verify Backups Exist

**What to check:**
- Backup scripts exist (already checked in Step 5)
- Backup FILES actually exist in memory/backups/

**Command:**
```bash
ls memory/backups/*.tar.gz 2>/dev/null | wc -l
ls memory/backups/ | grep -E "skills_backup|memory_backup" | wc -l
```

**Expected:**
- At least 1 recent backup file
- Should have both memory and skills backups

**Fix if missing:**
- Note that backups may not have run yet
- Reminder: Run `bash scripts/backup-memory.sh`

---

### STEP 6: Summary Report

Compile all results into a clean report.

---

## Output Format

Present audit results in this format:

```markdown
# 📋 Memory System Audit - [DATE]

## ✅ PASSED Checks
- [Check 1]: PASSED
- [Check 2]: PASSED
- ...

## ⚠️ Issues Found
- [Issue 1]: [Description]
  - **Fix**: [What to do]
- [Issue 2]: [Description]
  - **Fix**: [What to do]

## 🔧 Fixes Applied
- [Fix 1]: DONE
- [Fix 2]: DONE

## 📊 System Status
| Component | Status |
|-----------|--------|
| Memory Files | [count] files |
| Skills | [count] skills |
| Skills with SKILL.md | [count] |
| Model | [model name] |
| Backups | [count] files |
| People | [count]/4 complete |
```

---

## Auto-Fixes (Things I Can Fix Automatically)

These issues I can fix WITHOUT asking:

1. **Missing today's memory** - Create immediately
2. **Stray .used files** - Merge and delete
3. **Duplicate auto-learned.md** - Merge and delete

## Issues That Require Confirmation

Ask Jeem before fixing:

1. **Missing memory folders** - Need approval to create
2. **Missing people files** - Need approval to create
3. **Configuration errors** - Need approval to change rules
4. **Backup failures** - Need approval to reconfigure

---

## Related Skills

- `skills/study` - Load memory at session start
- `skills/sync` - Save session with auto-tagging
- `skills/full-sync` - Comprehensive sync
- `skills/stats` - Show weekly numeric summary
- `skills/mega-sync` - Full system health check

---

## Pro Tips

- Run this skill weekly or after any memory system changes
- Check immediately after creating new agents (like Momo)
- Run before any major updates or upgrades
- Keep this skill updated as my memory system evolves

---

*Skill version: 1.1 - Updated: May 11, 2026*
*Author: Mochi - Memory + Rules Expert 🐹💜*
*Changes in v1.1:*
*- Added Step 2.5: Key memory files check (permanent.md, auto-learned.md)*
*- Added Step 2.6: People files check (all 4 people)*
*- Added Step 5.5: Skills SKILL.md validation*
*- Added Step 5.6: Backup files existence check*