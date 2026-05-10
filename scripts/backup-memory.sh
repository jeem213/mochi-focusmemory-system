#!/bin/bash
# Backup Memory Script
# Creates a timestamped backup of the memory folder
# Run: bash scripts/backup-memory.sh

DATE=$(date +%Y-%m-%d_%H%M)
BACKUP_DIR="memory/backups"

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Create the backup
tar -czf "$BACKUP_DIR/memory_backup_$DATE.tar.gz" memory/*.md memory/people/ memory/decisions/ memory/mistakes/ 2>/dev/null

# Also backup skills
mkdir -p "$BACKUP_DIR/skills_backup_$DATE"
cp -r skills/ "$BACKUP_DIR/skills_backup_$DATE/" 2>/dev/null

echo "✅ Backup created: $BACKUP_DIR/memory_backup_$DATE.tar.gz"
echo "✅ Skills backed up: $BACKUP_DIR/skills_backup_$DATE/"

# Keep only last 7 backups (cleanup old ones)
cd $BACKUP_DIR
ls -t memory_backup_*.tar.gz 2>/dev/null | tail -n +8 | xargs -r rm -f
ls -td skills_backup_*/ 2>/dev/null | tail -n +8 | xargs -r rm -rf

echo "🧹 Cleanup complete - kept last 7 backups"

exit 0