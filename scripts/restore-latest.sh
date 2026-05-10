#!/bin/bash
# Restore from Backup Script
# Restores memory from the latest backup
# Run: bash scripts/restore-latest.sh

BACKUP_DIR="memory/backups"

# Check if backups exist
if [ ! -d "$BACKUP_DIR" ]; then
    echo "❌ No backup directory found!"
    exit 1
fi

# Find the latest backup
LATEST=$(ls -t $BACKUP_DIR/memory_backup_*.tar.gz 2>/dev/null | head -1)

if [ -z "$LATEST" ]; then
    echo "❌ No backups found!"
    exit 1
fi

echo "📦 Found latest backup: $LATEST"
echo "⚠️  This will restore files to memory/ - continue? (y/n)"
read -r CONFIRM

if [ "$CONFIRM" = "y" ]; then
    # Extract the backup
    tar -xzf "$LATEST" -C .
    echo "✅ Restore complete!"
    echo "📁 Files restored to: memory/"
else
    echo "❌ Restore cancelled"
    exit 0
fi

exit 0