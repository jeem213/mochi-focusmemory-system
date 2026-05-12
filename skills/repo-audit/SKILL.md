---
⚠️ **IMPORTANT: DONT SKIP ANY STEPS!**

**May 11, 2026 lesson:** Skipping steps leads to incomplete updates!

- Always follow ALL 6 steps in order
- Don't assume you know what to do - verify each step
- Compare versions, check README, verify completeness
- Only push AFTER completing all steps

**CRITICAL: This skill now does 100% LINE-BY-LINE diff for EVERY file!**

---
name: repo-audit
description: Compare local memory system with public GitHub repo, identify differences, and recommend updates. Use when you want to sync local changes to public repo - says "repo audit", "compare repo", or "sync public repo".
license: Proprietary
metadata:
  author: Mochi
  credits: Inspired by May 11, 2026 mega dive comparison
  version: "1.8"
  triggers:
    - repo audit
    - compare repo
    - sync public repo
    - repo sync
    - check public repo
    - compare public
  category: system
  requires:
    - web_fetch
    - exec
    - filesystem
---

# Repo Audit Skill (v1.8 - 100% DIFF CHECK!)

Compare local memory system with public GitHub repo, identify differences, and recommend updates.

**NEW in v1.8:** LINE-BY-LINE diff for ALL files - skills, rules, and scripts!

## When to Use This Skill

Triggered when Jeem says:
- "repo audit"
- "compare repo"
- "sync public repo"
- "repo sync"
- "check public repo"
- "compare public"

---

## The Repo Audit Process (6 Steps)

### STEP 1: Identify Public Repo

**Default repo:** `https://github.com/jeem213/mochi-focusmemory-system`

**Check for alternative repo if mentioned:**
- If user specifies different repo, use that
- Otherwise use default

**Ensure local clone is up-to-date:**
```bash
cd /home/openclaw/.openclaw/mochi-focusmemory-system
git pull origin main
```

---

### STEP 2: Fetch Public Repo File List

**Get list of files in public repo:**
```bash
git ls-tree -r --name-only origin main
# OR
curl -s https://api.github.com/repos/jeem213/mochi-focusmemory-system/contents | jq -r '.[].name'
```

**What to capture:**
- List of skills in public repo
- List of scripts
- README.md version
- Any other files

---

### STEP 2.5: Check README Content (IMPORTANT!)

**Fetch and analyze README.md:**
```bash
curl -s https://raw.githubusercontent.com/jeem213/mochi-focusmemory-system/main/README.md
```


**Check for these issues:**

| Check | What to Look For |
|-------|------------------|
| **Version** | Should match latest (e.g., "Version: 2.3") |
| **1% Better** | Should say "5 syncs OR 3 days" NOT just "every 5 sessions" |
| **Skills** | Should include memory-audit, mega-dive triggers |
| **Badge** | Version badge should match actual version |
| **Changelog** | Should have entry for current version |
| **Python Scripts** | MUST include: memory-report.py, fast-search.py, python-backup.py, web-research.py |

**Compare with local:**
- Check SOUL.md version reference
- Check sync skill for 1% Better system
- Ensure README reflects current implementation!

---

### STEP 2.6: Compare Skill Versions (CRITICAL!)

**This is ESSENTIAL - versions MUST match!**

**For each memory skill in public, compare local vs public:**
```bash
# Example for memory-audit:
grep "^  version:" skills/memory-audit/SKILL.md
grep "^  version:" ../mochi-focusmemory-public/skills/memory-audit/SKILL.md
```

**Skills to check (ALL 10):**
- study
- sync
- mega-dive
- mega-sync
- memory-audit
- stats
- decisions
- full-sync
- remember
- repo-audit

**What to verify:**
- Version numbers match
- New features are present
- Python script references exist


**WARNING:** If versions DON'T match, the public repo is OUT OF DATE!

---

### STEP 2.7: LINE-BY-LINE DIFF FOR ALL SKILLS (MANDATORY!)

**🚨 NEW STEP - 100% CONTENT VERIFICATION!**

This is MANDATORY for every audit! Use local clone to avoid API rate limits.

**For EACH of the 10 memory skills, do a LINE-BY-LINE diff:**

```bash
# Compare each skill
diff skills/study/SKILL.md ../mochi-focusmemory-system/skills/study/SKILL.md
diff skills/sync/SKILL.md ../mochi-focusmemory-system/skills/sync/SKILL.md
# ... repeat for ALL 10 skills
```

**The 10 Memory Skills to check:**
1. study
2. sync
3. mega-dive
4. mega-sync
5. memory-audit
6. stats
7. decisions
8. full-sync
9. remember
10. repo-audit

**Report format:**
```
✅ skill-name - 100% IDENTICAL
❌ skill-name - DIFFERENT (X lines different)
```

**If ANY differ:**
- Note which skill differs
- Show first few lines of difference
- Recommend pushing update

---

### STEP 2.8: LINE-BY-LINE DIFF FOR RULES FILES (MANDATORY!)

**🚨 NEW STEP - 100% CONTENT VERIFICATION FOR RULES!**

Compare ALL rules/config files line-by-line:

```bash
# Compare rules files
diff SOUL.md ../mochi-focusmemory-system/SOUL.md
diff AGENTS.md ../mochi-focusmemory-system/AGENTS.md
diff IDENTITY.md ../mochi-focusmemory-system/IDENTITY.md
diff USER.md ../mochi-focusmemory-system/USER.md
```

**Files to check:**
1. SOUL.md - Identity and rules
2. AGENTS.md - Workspace config
3. IDENTITY.md - My identity
4. USER.md - User profile

**Report format:**
```
✅ SOUL.md - 100% IDENTICAL (361 lines)
❌ AGENTS.md - DIFFERENT (128 vs 130 lines)
```

---

### STEP 2.9: LINE-BY-LINE DIFF FOR SCRIPTS (MANDATORY!)

**🚨 NEW STEP - 100% CONTENT VERIFICATION FOR SCRIPTS!**

Compare ALL Python and shell scripts:

```bash
# Compare Python scripts
diff scripts/memory-report.py ../mochi-focusmemory-system/scripts/memory-report.py
diff scripts/fast-search.py ../mochi-focusmemory-system/scripts/fast-search.py
diff scripts/python-backup.py ../mochi-focusmemory-system/scripts/python-backup.py
diff scripts/web-research.py ../mochi-focusmemory-system/scripts/web-research.py

# Compare shell scripts
diff scripts/backup-memory.sh ../mochi-focusmemory-system/scripts/backup-memory.sh
diff scripts/weekly-archive.sh ../mochi-focusmemory-system/scripts/weekly-archive.sh
```

**Core scripts to check (Python):**
1. memory-report.py
2. fast-search.py
3. python-backup.py
4. web-research.py
5. auto-snapshot.py
6. pandas-stats.py (if in public)

**Core scripts to check (Shell):**
1. backup-memory.sh
2. backup-daily.sh
3. weekly-archive.sh

**Report format:**
```
✅ memory-report.py - 100% IDENTICAL
❌ fast-search.py - DIFFERENT (added new commands)
```

---

### STEP 3: Compare with Local Workspace

**Compare local vs public:**

| Category | Local Count | Public Count | Gap |
|----------|-------------|-------------|-----|
| Skills | 10 | 10 | Should match! |
| Scripts | 10+ | 10 | Should match! |
| Rules files | 4 | 4 | Should match! |

**Identify what's MISSING from public:**
- List local skills not in public
- Note version differences

---

### STEP 4: Analyze Differences

**For each difference, assess:**

| Gap Type | Priority | Action |
|----------|----------|--------|
| Core skill content differs | 🔴 HIGH | Push update immediately |
| Rules content differs | 🔴 HIGH | Push update immediately |
| Script content differs | 🔴 HIGH | Push update immediately |
| Version bump needed | 🔴 HIGH | Update README |

---

### STEP 5: Recommend Updates

**Present recommendations with 100% verification results:**

```markdown
## 📊 100% Content Comparison Results

### Skills (10/10 checked)
✅ study - IDENTICAL
✅ sync - IDENTICAL
❌ memory-audit - DIFFERS (needs push)
...

### Rules Files (4/4 checked)
✅ SOUL.md - IDENTICAL
❌ AGENTS.md - DIFFERS (needs push)
...

### Scripts (10/10 checked)
✅ memory-report.py - IDENTICAL
✅ fast-search.py - IDENTICAL
...

## 🚨 HIGH Priority (Content Differs)
- [file]: [Lines different]

## 🎯 Recommended Actions
1. Push [file] to public repo
2. Update README version
3. Re-verify after push
```

---

### STEP 6: Execute Updates (If Approved)

**If user approves, do:**

1. Copy updated files to local clone
2. Commit with descriptive message
3. Push to GitHub
4. **RE-RUN 100% verification after push** to confirm!

---

### STEP 6.5: AUTO-SYNC README (Memory System Only!)

**🚨 MANDATORY STEP - DON'T SKIP!**

After pushing ANY skill updates to public repo, you MUST update the README!

**When to run this step:**
- After Step 6 (pushing skill changes)
- ANY time local versions differ from public

**The Rule:** "If skills changed → README MUST change!"

---

**IMPORTANT: Only sync MEMORY SYSTEM changes - not all skills!**

The public repo is for the **Heyron Focus Memory System** - just the memory parts!


**Only update README for memory-related changes:**

| Memory System Change | README Update |
|---------------------|----------------|
| New memory skill (sync, study, mega-sync, memory-audit, mega-dive, stats, decisions) | Add to triggers table + examples |
| 1% Better system updated (HYBRID) | Update description |
| Memory rules changed | Update SOUL.md section |
| Memory folders added/removed | Update folder diagram |
| Version bump | Update version + badge + changelog |

**IGNORE (don't sync):**
- Other skills (advise, generate-image, youtube-full, etc.)
- Internal tools (repo-audit, skill-audit, etc.)
- Non-memory rules or preferences

**The Sync Process:**

1. Check LOCAL memory skills vs PUBLIC skills
2. Check sync skill for 1% Better changes
3. Check memory folders
4. For each memory change: Update README
5. Add changelog entry
6. Push

**🚨 MANDATORY: After pushing, you MUST:**
1. Update README.md version history
2. Update skills count if changed
3. Update any changed feature descriptions
4. Push README changes

**NEVER say "sync complete" until README is updated!**

**Goal: Anyone can build the EXACT same memory system from our public README!**

---

## Auto-Sync Capabilities (Proactive!)

**These I can do automatically WITHOUT asking:**
- Clone repo to temp
- List and compare files
- Generate report
- **Update README to match local changes**
- **Version bump**
- **Changelog entry**
- Push changes

**These need approval:**
- Adding new skill FILES to repo (but updating README for them is auto!)

**The key philosophy:** If we changed it locally, the public README should know about it!

---

## Output Format

```markdown
# 📋 Repo Audit Results - [DATE]

## 100% Content Verification

### Skills (10/10)
✅ skill1 - 100% IDENTICAL
❌ skill2 - DIFFERENT (X lines)

### Rules Files (4/4)
✅ SOUL.md - 100% IDENTICAL
...

### Scripts (10/10)
✅ script.py - 100% IDENTICAL
...

## Current State
- Local skills: [count]
- Public skills: [count]
- Version: [X.X]

## Differences Found
- [file]: HIGH priority - needs push

## Recommended Updates
1. [Action 1]
2. [Action 2]

## Status
[Ready to push / Needs approval]
```

---

## Related Skills

- `skills/sync` - Save to memory + GitHub
- `skills/memory-audit` - Audit local memory system
- `skills/mega-sync` - Full system health check

---

## Pro Tips

- Run this before any public release
- ALWAYS do 100% line-by-line diff - don't skip!
- Use local clone to avoid GitHub API rate limits
- Re-verify AFTER pushing to confirm success
- Always bump version in README when adding features

---

## Time Estimate

| Step | Time |
|------|------|
| Compare file lists | 10s |
| **100% diff skills (10)** | **60s** |
| **100% diff rules (4)** | **20s** |
| **100% diff scripts (10)** | **30s** |
| Analyze differences | 30s |
| Create report | 20s |
| **Total** | **~3 min** |

---

## Error Handling

| Error | What to Do |
|-------|------------|
| Git not available | Note in report, skip git checks |
| Network error | Note "GitHub unreachable", continue |
| Permission denied | Note which files couldn't push |
| Different repo | Stop and ask - wrong repo! |
| Diff shows difference | Note file, recommend push |

---

## Examples

### Example 1: 100% Verification - All Match
```
You: repo audit
Mochi: 🔍 Running 100% content verification...
📋 Skills (10/10):
  ✅ study - 100% IDENTICAL
  ✅ sync - 100% IDENTICAL
  ✅ mega-dive - 100% IDENTICAL
  ...
📋 Rules (4/4):
  ✅ SOUL.md - 100% IDENTICAL
  ✅ AGENTS.md - 100% IDENTICAL
  ...
📋 Scripts (10/10):
  ✅ memory-report.py - 100% IDENTICAL
  ...
🎉 Public repo is 100% in sync!
```

### Example 2: 100% Verification - Differences Found
```
You: repo audit
Mochi: 🔍 Running 100% content verification...
📋 Skills (10/10):
  ✅ study - 100% IDENTICAL
  ❌ sync - DIFFERENT (5 new lines added)
  ...
📋 Rules (4/4):
  ✅ SOUL.md - 100% IDENTICAL
  ❌ AGENTS.md - DIFFERENT (2 new platform rules)
  ...
🎯 2 files need pushing!
```

---

## Related Skills

- `skills/sync` - Save to memory + GitHub
- `skills/memory-audit` - Audit local memory system
- `skills/mega-sync` - Full system health check

---

*Skill version: 1.8 - Updated: May 12, 2026*
*Note: v1.8 - Added 100% LINE-BY-LINE diff for ALL skills, rules, and scripts!*
*Author: Mochi - Memory + Rules Expert 🐹💜*