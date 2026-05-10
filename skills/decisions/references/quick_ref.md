# Decisions Skill - Quick Reference

## Trigger Words

- `promote decisions` - Run decision promotion
- `organize decisions` - Same as above
- `decisions` - Check decisions folder
- `decision check` - Show recent decisions

## What It Does

1. Scans memory files for #decision tags
2. Extracts and deduplicates
3. Promotes to memory/decisions/
4. Reports results

## Usage

```
# Manual:
You: promote decisions

# Automatic (after sync):
- Runs automatically with sync v2.1+
```

## Output Example

```
🔍 Scanning memory files...
📋 Found 5 decisions
✅ Promoted 3 new decisions
⏭️ Skipped 2 duplicates
```

## Files Modified

- `memory/decisions/memory-system.md`
- `memory/decisions/*.md` (topic files)

---

*Part of Mochi Focus Memory System*