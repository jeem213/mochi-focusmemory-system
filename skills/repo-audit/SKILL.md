---
⚠️ **IMPORTANT: DONT SKIP ANY STEPS!**

**May 11, 2026 lesson:** Skipping steps leads to incomplete updates!

- Always follow ALL 6 steps in order
- Don't assume you know what to do - verify each step
- Compare versions, check README, verify completeness
- Only push AFTER completing all steps

---
name: repo-audit
description: Compare local memory system with public GitHub repo, identify differences, and recommend updates. Use when you want to sync local changes to public repo - says "repo audit", "compare repo", or "sync public repo".
license: Proprietary
metadata:
  author: Mochi
  credits: Inspired by May 11, 2026 mega dive comparison
  version: "1.7"
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

# Repo Audit Skill

Compare local memory system with public GitHub repo, identify differences, and recommend updates.

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

---

### STEP 2: Fetch Public Repo File List

**Get list of files in public repo:**
```bash
git ls-tree -r --name-only public/main
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

**Skills to check:**
- memory-audit
- mega-dive
- stats
- study
- sync

**What to verify:**
- Version numbers match
- New features are present
- Python script references exist


**WARNING:** If versions DON'T match, the public repo is OUT OF DATE!

---

### STEP 2.7: LINE-BY-LINE DIFF (Advanced)

**For complete accuracy, do a diff:**
```bash
diff skills/memory-audit/SKILL.md ../mochi-focusmemory-public/skills/memory-audit/SKILL.md
```

This catches:
- Missing new steps
- Different version numbers
- Content differences

**Critical for ensuring perfection!**

---

### STEP 3: Compare with Local Workspace

**Compare local vs public:**

| Category | Local Count | Public Count | Gap |
|----------|-------------|-------------|-----|
| Skills | 34 | 7 | What missing? |
| Scripts | 5 | 5 | ✅ Match |
| Memory folders | 5 | 5 | ✅ Match |

**Identify what's MISSING from public:**
- List local skills not in public
- Note version differences

---

### STEP 4: Analyze Differences

**For each difference, assess:**

| Gap Type | Priority | Action |
|----------|----------|--------|
| Core skill missing (sync, study, mega-sync) | 🔴 HIGH | Add immediately |
| New skill created locally | 🟡 MEDIUM | Recommend adding |
| Documentation update | 🟡 MEDIUM | Recommend updating |
| Version bump needed | 🔴 HIGH | Update README |

---

### STEP 5: Recommend Updates

**Present recommendations:**

```markdown
## 📊 Comparison Results

| Category | Local | Public | Gap |
|----------|-------|--------|-----|
| Skills | 34 | 7 | 27 missing |

## 🚨 HIGH Priority
- [Skill]: [Reason]

## 🟡 MEDIUM Priority  
- [Skill]: [Reason]

## 🎯 Recommended Actions
1. Add [skill] to public repo
2. Bump version to X.X
3. Update README with new triggers
```

---

### STEP 6: Execute Updates (If Approved)

**If user approves, do:**

1. Clone public repo to temp location
2. Copy missing skill files
3. Update README version
4. Add new triggers to README
5. Commit and push
6. Clean up temp files
7. Verify on GitHub

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

## Current State
- Local skills: [count]
- Public skills: [count]
- Version: [X.X]

## Differences Found
- [Missing skill]: HIGH/MEDIUM priority

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
- Always bump version in README when adding features
- Test new skills locally before pushing to public
- Keep public repo as "stable" - local can have experimental skills

---

## Time Estimate

| Step | Time |
|------|------|
| Compare file lists | 30s |
| Check content differences | 30s |
| Analyze each difference | 60s |
| Create report | 20s |
| **Total** | **~2-3 min** |

---

## Error Handling

| Error | What to Do |
|-------|------------|
| Git not available | Note in report, skip git checks |
| Network error | Note "GitHub unreachable", continue |
| Permission denied | Note which files couldn't push |
| Different repo | Stop and ask - wrong repo! |

---

## Examples

### Example 1: Compare Local vs Public
```
You: repo audit
Mochi: 🔍 Comparing local vs public repo...
📁 Local: 45 files | Public: 42 files
📋 Difference: 3 new skills in local
✅ All differences safe to push
```

### Example 2: Check Before Release
```
You: repo audit
Mochi: 🔍 Running pre-release audit...
✅ No private data found
✅ README in sync
✅ Skills all compliant
✅ Ready for public release!
```

---

## Related Skills

- `skills/sync` - Save to memory + GitHub
- `skills/memory-audit` - Audit local memory system
- `skills/mega-sync` - Full system health check

---

*Skill version: 1.5 - Updated: May 11, 2026*
*Note: v1.5 - Added Step 2.6: Skill Version Comparison + Python Scripts check!*
*Note: v1.4 - README sync only for MEMORY SYSTEM changes (not all skills!)*
*Author: Mochi - Memory + Rules Expert 🐹💜*