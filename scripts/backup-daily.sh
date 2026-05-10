#!/bin/bash
# Daily Backup Script
# Creates a timestamped backup of the memory folder - RUNS DAILY!
# Run: bash scripts/backup-daily.sh
# Add to HEARTBEAT for daily automation!

DATE=$(date +%Y-%m-%d_%H%M)
BACKUP_DIR="memory/backups"

echo "📦 Starting daily backup..."

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Create memory backup (smaller - just recent files)
# Only back up the last 14 days of daily memory
find memory/ -name "*.md" -type f -mtime -14 ! -path "memory/people/*" ! -path "memory/decisions/*" ! -path "memory/mistakes/*" ! -path "memory/improvements/*" ! -path "memory/backups/*" ! -path "memory/archive/*" ! -name "auto-learned.md" ! -name "permanent.md" -print0 | tar -czf "$BACKUP_DIR/memory_backup_$DATE.tar.gz" --null -T - 2>/dev/null

# Backup core folders (people, decisions, mistakes, improvements) - FULL
tar -czf "$BACKUP_DIR/core_folders_$DATE.tar.gz" memory/people/ memory/decisions/ memory/mistakes/ memory/improvements/ 2>/dev/null

# Also backup skills
mkdir -p "$BACKUP_DIR/skills_backup_$DATE"
cp -r skills/ "$BACKUP_DIR/skills_backup_$DATE/" 2>/dev/null

echo "✅ Daily backup created: $BACKUP_DIR/memory_backup_$DATE.tar.gz"
echo "✅ Core folders backed up: $BACKUP_DIR/core_folders_$DATE.tar.gz"
echo "✅ Skills backed up: $BACKUP_DIR/skills_backup_$DATE/"

# Keep only last 14 daily backups (cleanup old ones)
cd $BACKUP_DIR
ls -t memory_backup_*.tar.gz 2>/dev/null | tail -n +15 | xargs -r rm -f
ls -t core_folders_*.tar.gz 2>/dev/null | tail -n +15 | xargs -r rm -f
ls -td skills_backup_*/ 2>/dev/null | tail -n +15 | xargs -r rm -rf

echo "🧹 Cleanup complete - kept last 14 daily backups"

# Show backup count
BACKUP_COUNT=$(ls -1 memory_backup_*.tar.gz 2>/dev/null | wc -l)
echo "📊 Total daily backups: $BACKUP_COUNT"

exit 0