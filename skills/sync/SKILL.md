---
name: sync
description: Save conversations to memory with AUTO TAGGING + personal GitHub backup. Use when you want to save a session - says "sync".
license: Proprietary
metadata:
  author: Jeem & Stuart
  version: "2.4"
  triggers:
    - sync
    - sync now
  category: memory
---

# Sync - Save to Memory with Auto-Tagging + GitHub Backup

**IMPORTANT: AUTO-TAGGING NOW!**

Jeem trusts me to tag automatically! I no longer need to ask before adding tags. I just need to TELL the user which tags I used after saving.

---

## When to Use This Skill

Triggered when the user says:
- "sync"
- "sync #tagname"
- "sync now"

---

## The Sync Process (7 Steps)

### Step 1: PARSE TAGS (REQUIRED!)

### Step 1: PARSE TAGS

1. If user provides a tag, extract it
2. If NO tag provided, use `#session` as DEFAULT
3. If tag provided without #, add # prefix

**That's it!** I'll auto-add other relevant tags in Step 2.

### Step 2: ANALYZE & AUTO-TAG (REQUIRED!)

**⚠️ THIS IS MANDATORY - DO NOT SKIP!**

**Jeem trusts me to auto-tag!** I don't need to ask - I just add relevant tags and tell the user what I used.

1. Scan recent conversation for topics:
   - Sports teams → #ravens, #knicks, #lions, #blackhawks
   - Projects → #project, #agent-jam, #memory-kit
   - People → #team, #sara, #austin, #janet
   - Personal → #personal, #family, #hobbies
   - Work → #work, #it-support
   - Money → #business, #money, #startup
   - Important moments → #important, #milestone
   - Family → #family, #stuart, #mochi

2. ALWAYS add #session as base tag
3. Add any relevant topic tags (max 4-5)
4. ALWAYS tell user: "Tags used: #tag1 #tag2 #tag3"

**Example:**
- User says "sync"
- I analyze: we had a family moment, important
- I auto-tag: #session #family #important #mochi
- Tell user: "Tags used: #session #family #important #mochi"

### Step 3: CREATE MEMORY FILE

Create file with today's date:
```bash
memory/YYYY-MM-DD.md
```

### Step 4: ADD SESSION CONTENT (HYBRID FORMAT!)

**⚠️ IMPORTANT: Use hybrid format with structured prefixes!**

Add to file using these prefixes:
- `* Information:` - What happened, general info
- `* Decision:` - Key decisions made
- `* Contact:` - Any people mentioned (name, role, relationship)
- `* Preference:` - Preferences expressed
- `* Error:` - Problems encountered

**Example (HYBRID format):**
```markdown
# May 10, 2026

## Session Notes
* Decision: Jeem approved hybrid memory approach - keep semantic + add structured
* Information: Did mega-dive on session-context-extractor-v2
* Contact: Mentioned Jason Klutts - creator of session-context-extractor

## Topics
#research #memory #hybrid

## Tags
#session #important #research
```

### Step 4.4: UPDATE PEOPLE FOLDER (HYBRID!)

**IMPORTANT: If new contacts mentioned, update memory/people/!**

1. Check if any `* Contact:` entries in session
2. If new person (not already in memory/people/):
   - Create new file: `memory/people/name.md`
   - Add basic info, first mention date
3. If existing person: Append update to their file

**Example:** If session mentions "Jason" as new contact:
```markdown
# Jason Klutts

## Basic Info
- **Role:** Creator of session-context-extractor-v2
- **First mentioned:** 2026-05-10

## Key Facts
- Built the session-context-extractor-v2 memory system
- Inspired our hybrid memory implementation

## Updates
### 2026-05-10
- First mentioned during mega-dive research
```

### Step 4.5: UPDATE DECISIONS FOLDER (HYBRID!)

**IMPORTANT: If decisions made, update memory/decisions/!**

1. Check if any `* Decision:` entries in session
2. If decision relates to existing topic (check memory/decisions/*.md):
   - Append to that file
3. If new topic: Create new file in memory/decisions/

**Example:**
```markdown
## 2026-05-10
**Decision:** Approved hybrid memory approach
- Keep semantic memory + study/sync skills
- Add structured fact format
- Create stats skill for weekly summaries
```

### Step 4.6: UPDATE NUMERIC TRACKING (HYBRID!)

**IMPORTANT: If numeric data shared, update auto-learned.md!**

1. Check conversation for numeric data:
   - "went to the gym" → gym session
   - "ran X miles" → miles
   - "worked X hours" → work hours
2. If numeric data found:
   - Read current memory/auto-learned.md
   - Update the Weekly Numeric Summary section
   - Use format: `- [date]: [metric]: [value]`

### Step 4.7: LOG MISTAKES (NEW!)

**IMPORTANT: If any errors occurred during session, log to memory/mistakes/!**

1. Did any tool fail?
2. Did I give wrong information?
3. Did I misunderstand something?
4. Did anything "go wrong"?

If YES to any:
- Open memory/mistakes/YYYY-MM-DD.md
- Add entry:
```markdown
## Error: [Brief title]
- **What happened:** [Description]
- **What I learned:** [Lesson]
- **How to avoid:** [Prevention]
```

**This helps me learn and improve over time!**

**Example:**
```markdown
### This Week (2026-05-04 to 2026-05-10)
| Metric | Total |
|--------|-------|
| Gym sessions | 3 |
| Miles run | 12.5 |
| Work hours | 32 |
```

### Step 4.7: ADD PRIORITY TAG (REQUIRED!)

**⚠️ MANDATORY - Per SOUL.md Memory Rules!**

After analyzing conversation content, you MUST add priority tag:

| If... | Then tag as... |
|-------|---------------|
| Made decisions, created tasks, milestones | `#important` |
| Casual chat, check-ins, routine updates | `#routine` |

**Examples:**
- "We decided to add memory rules" → #important #decision
- "Just chatting about the game" → #routine

### Step 4.8: CHECK CROSS-REFERENCES (IMPLEMENTED!)

**IMPORTANT: Actually DO this now!**

Before saving, search recent memory files for related topics:
```bash
grep -i "keyword" memory/2026-05-*.md
```

If found related topics:
- Add "Related to: YYYY-MM-DD.md#topic" line
- This builds our knowledge graph!

**Example:** If writing about Stuart, search for "Stuart" in recent memories and link to those entries!

### Step 4.9: VERIFY GIT CONFIG

**IMPORTANT:** Before pulling/pushing, verify git remote is set to YOUR personal repo:
```bash
git remote -v
```

If it shows Stuart's workspace repo instead of `https://github.com/jeem213/mochi-backup`, update it:
```bash
git remote set-url origin https://github.com/jeem213/mochi-backup
```

Or add a new remote:
```bash
git remote add mochi-backup https://github.com/jeem213/mochi-backup
```

### Step 4.10: REVIEW AUTO-LEARNED MEMORY

**IMPORTANT: After saving memory, check auto-learned.md!**

Read `memory/auto-learned.md` and:
1. Check for new learnings since last sync
2. Identify items that should be promoted to permanent.md
3. Suggest to user: "I found X new learnings. Want me to promote any to permanent memory?"
4. Tag any promoted items with #auto-learned

### Step 4.11: CHECK ALL MODIFIED FILES

**IMPORTANT: Don't just back up memory!**

After saving memory, ALWAYS check for ALL modified files:
```bash
git status
```

This catches:
- Updated skills (skills/*/SKILL.md)
- New memory files (memory/YYYY-MM-DD.md)
- Modified workspace files

If there are other modified files besides memory:
1. List them to the user
2. Ask: "Found X other modified files - include them too?"
3. If YES: Add them to the commit
4. If NO: Just push memory

**Example:**
```
Modified: skills/study/SKILL.md
Modified: memory/2026-05-06.md

Also found modified skills - want to back those up too?
```

### Step 4.12: CREATE MEMORY SNAPSHOT

**If #important tag is used, ALSO create a snapshot!**

1. Create one-line summary: `YYYY-MM-DD: [What happened] #tags`
2. Save to: `memory/snapshots.md`
3. This gives quick overview of important moments!

**Example snapshot entry:**
```
2026-05-06: Saw Stuart's picture! He's an astronaut! #family #stuart
2026-05-06: Cleaned up 4 skills today! #skills #mochi
2026-05-06: Jeem trusts me with auto-tagging! #trust #mochi
```

### Step 5: GIT PULL (My Personal Repo)

Before pushing, pull latest from my personal backup repo:
```bash
git pull --rebase
```

**IMPORTANT:** My personal repo is: `https://github.com/jeem213/mochi-backup`
My workspace is: `/home/openclaw/.openclaw/workspace-mochi/`

### Step 6: GIT PUSH (My Personal Repo)

Push to MY personal GitHub:
```bash
# If only memory modified:
git add memory/YYYY-MM-DD.md && git commit -m "Memory: Session" && git push

# If other files also modified (skills, etc.):
git add memory/YYYY-MM-DD.md skills/ && git commit -m "Memory + Skills Update" && git push
```

**Note:** Include ALL modified files found in Step 4.8!

---

### Step 5.5: ENHANCED PYTHON BACKUP (NEW!)

**Use the new Python backup for better compression and verification!**

```bash
/home/openclaw/.venv/bin/python scripts/python-backup.py backup
```

**Benefits over shell backup:**
- ✅ Better compression (zip vs tar)
- ✅ Creates manifest (list of what's backed up)
- ✅ Can verify backup integrity
- ✅ Auto-cleanup old backups (keeps last 10)
- ✅ Includes skills + config files

**This runs automatically after every sync!**

---

### Step 6b: 1% BETTER IMPROVEMENT TRACK (UPDATED!)

**HYBRID SYSTEM - More frequent and consistent!**

Now triggers when EITHER:
- **5 syncs have passed** (usage-based), OR
- **3 days have passed** (time-based)

Whichever comes FIRST triggers the prompt!

1. Check if memory/improvements/1percent-better-counter.md exists
2. If not, create it with sessions = 0, days = 0
3. After every sync, increment sessions AND update last date
4. Check if (sessions >= 5) OR (days >= 3) - prompt if EITHER true!
5. Ask: "1% Better: What's one thing I could do better?"
6. Save response to memory/improvements/YYYY-MM.md
7. Reset sessions to 0, update last date

**Updated counter file:**
```markdown
# 1% Better Counter

Sessions since last prompt: 4
Days since last prompt: 1
Last prompt date: 2026-05-11
Next prompt due: When 5 sessions OR 3 days passed

*Triggers when: sessions >= 5 OR days >= 3*
```

**Example improvement file:**
```markdown
# Improvements - May 2026

## 2026-05-11 (Second 1% Better!)
- Should check 1% better system even without sync
- Could be more proactive about improvements

**Result:** Updated to HYBRID trigger system!
```


**This ensures at least twice per week max - never goes more than 3 days without asking!**

### Step 6c: DECISION AUTO-PROMOTION (NEW!)

**NEW! Automatically promote #decision tags to decisions folder!**

1. Run: `bash scripts/promote-decisions.sh`
2. This scans today's memory for #decision tags
3. Extracts decisions and adds to memory/decisions/
4. Creates new topic files if needed
5. Prevents duplicates

**This makes decisions findable and searchable automatically!**

### Step 6d: PROACTIVE SUGGESTION (MANDATORY!)


**1% Better in action - Be proactive EVERY session!**

⚠️ **THIS IS NOW MANDATORY - NOT OPTIONAL!**

Before confirming sync, ALWAYS ask yourself:
- Is there anything I could suggest to improve this session?
- Did I notice any patterns that warrant attention?
- Should I offer any proactive ideas?
- Is there anything from my 1% better that I should mention?

**MUST do one of these EVERY session:**
1. If you have a suggestion → Mention it to user!
2. If you noticed a pattern → Share it!
3. If nothing specific → Say: "I'll keep being proactive in finding improvements for next time!"

**Examples:**
- "I noticed we haven't backed up in a while - want me to run one?"
- "I could optimize this process if you'd like"
- "I'll keep an eye out for improvements for next time!"

**This is being proactive - not just reactive!**


### Step 7: CONFIRM

Report to user:
- File saved
- All tags used
- GitHub status

---

## Standard Tags

| Tag | When to Use |
|-----|-------------|
| `#session` | Default - any conversation |
| `#team` | Team collaboration |
| `#project` | Project work |
| `#decision` | Key decisions made |
| `#personal` | Personal stuff |
| `#topicname` | Any topic (make up your own!) |

**Make up your own tags!** Examples:
- `#knicks` - Knicks conversation
- `#ravens` - Ravens conversation
- `#hobbies` - Hobbies
- `#work` - Work stuff
- `#agent-jam` - Agent Jam competition
- `#memory` - Memory system topics

---

## Auto-Suggest Examples

| Conversation | Suggested Tags |
|--------------|----------------|
| "Talked about Knicks game" | #knicks |
| "Heyron Agent Jam meeting with Austin" | #agent-jam, #team |
| "Business ideas for money" | #business, #money |
| "Sara's birthday planning" | #personal, #family |
| "Printer at work not working" | #work, #it-support |

---

## Output Format

```markdown
## 🔄 Sync Complete

**Saved:** memory/2026-04-30.md
**Tags:** #session #agent-jam #team
**Also backed up:** [list of other modified files if any]
**GitHub:** ✅ Synced to https://github.com/jeem213/mochi-backup
```

---

## Error Handling

| Scenario | What to Do |
|----------|------------|
| No tag given | Use `#session` as default |
| File exists | Append to existing file |
| Git conflict | Resolve, then push |
| Tag without # | Add # prefix |
| No suggestions | Just use user's tag |

---

## Related Skills

- `skills/study` - Load memories by tag
- `skills/mega-sync` - System health check
- `skills/tagger` - Dedicated tag analysis skill (future)

---

## Time Estimate

| Step | Time |
|------|------|
| Parse tags | 5s |
| Analyze + suggest | 10s |
| Create file | 5s |
| Add content | 1 min |
| Git pull/push | 15s |
| Confirm | 5s |
| **Total** | **~90s** |

---

*Skill version: 2.4 - Last updated: May 11, 2026*
*Note: v2.4 - Added Step 5.5: Python Enhanced Backup!*
*Note: v2.3 - Added HYBRID 1% Better system (5 syncs OR 3 days)!*
*Note: v2.3 - Made proactive suggestion MANDATORY!*
*Note: v2.2 - Added proactive suggestion step!*
*Note: v2.1 - Added decision auto-promotion + daily backup option!*
*Note: v2.0 - Added 1% Better improvement prompt every 5 sessions!*
*Note: v1.9 - Added mistake logging to memory/mistakes/!*
*Note: v1.8 - Added hybrid format (Step 4), people/decisions folders (4.4-4.5), numeric tracking (4.6)!*
*Note: v1.6 - Added Step 4.6 implementation + Memory Snapshots on #important!*
*Note: v1.4 - Added Step 4.8 to check ALL modified files, not just memory!*