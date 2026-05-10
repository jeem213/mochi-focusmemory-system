#!/bin/bash
# Weekly Archive Script
# Moves memory files older than 30 days to archive
# Run: bash scripts/weekly-archive.sh

ARCHIVE_DIR="memory/archive"
MEMORY_DIR="memory"

# Create archive directory if it doesn't exist
mkdir -p $ARCHIVE_DIR

# Get current date
TODAY=$(date +%Y-%m-%d)

# Find and move files older than 30 days
# This runs monthly to keep memory folder clean
find $MEMORY_DIR -name "*.md" -type f -mtime +30 ! -path "$MEMORY_DIR/people/*" ! -path "$MEMORY_DIR/decisions/*" ! -path "$MEMORY_DIR/mistakes/*" ! -path "$MEMORY_DIR/archive/*" ! -name "auto-learned.md" ! -name "permanent.md" -exec mv -n {} $ARCHIVE_DIR/ \;

# Count archived files
ARCHIVED_COUNT=$(find $ARCHIVE_DIR -name "*.md" -type f | wc -l)

echo "✅ Weekly archive complete!"
echo "📦 Total archived files: $ARCHIVED_COUNT"
echo "📁 Archive location: $ARCHIVE_DIR/"

# Create a summary file in archive
echo "# Archive Summary" > $ARCHIVE_DIR/README.md
echo "Archive date: $TODAY" >> $ARCHIVE_DIR/README.md
echo "Total files: $ARCHIVED_COUNT" >> $ARCHIVE_DIR/README.md

exit 0