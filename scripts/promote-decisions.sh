#!/bin/bash
# Decision Auto-Promotion Script
# Scans memory files for #decision tags and promotes to memory/decisions/
# Run: bash scripts/promote-decisions.sh
# Called automatically by sync skill!

echo "🔍 Starting decision auto-promotion..."

DECISIONS_DIR="memory/decisions"
MEMORY_DIR="memory"

# Create decisions directory if it doesn't exist
mkdir -p $DECISIONS_DIR

# Get list of recent memory files (last 30 days)
MEMORY_FILES=$(find $MEMORY_DIR -name "*.md" -type f -mtime -30 ! -path "$MEMORY_DIR/people/*" ! -path "$MEMORY_DIR/decisions/*" ! -path "$MEMORY_DIR/mistakes/*" ! -path "$MEMORY_DIR/improvements/*" ! -path "$MEMORY_DIR/backups/*" ! -path "$MEMORY_DIR/archive/*" ! -name "auto-learned.md" ! -name "permanent.md")

PROMOTED_COUNT=0

# Function to extract decisions from a file
promote_decisions() {
    local file="$1"
    local filename=$(basename "$file" .md)
    local date=$(echo "$filename" | grep -oE "[0-9]{4}-[0-9]{2}-[0-9]{2}")
    
    # Find lines with #decision tag
    local decisions=$(grep -i "#decision" "$file" 2>/dev/null)
    
    if [ -n "$decisions" ]; then
        echo "📋 Found decisions in $filename"
        
        # Extract each decision line and add to general decisions file
        echo "$decisions" | while read -r line; do
            # Clean up the decision text (remove #tags)
            local decision_text=$(echo "$line" | sed 's/.*#decision//' | sed 's/#[^ ]*//g' | xargs)
            
            if [ -n "$decision_text" ]; then
                # Check if this decision already exists in memory-system.md
                if ! grep -q "$decision_text" "$DECISIONS_DIR/memory-system.md" 2>/dev/null; then
                    echo "" >> "$DECISIONS_DIR/memory-system.md"
                    echo "## $date" >> "$DECISIONS_DIR/memory-system.md"
                    echo "**Decision:** $decision_text" >> "$DECISIONS_DIR/memory-system.md"
                    echo "*(Promoted from: $filename)*" >> "$DECISIONS_DIR/memory-system.md"
                    echo "PROMOTED: $decision_text"
                    ((PROMOTED_COUNT++))
                fi
            fi
        done
    fi
}

# Process each memory file
for file in $MEMORY_FILES; do
    promote_decisions "$file"
done

# Also check for inline decision patterns like "Decision:" or "* Decision:"
echo ""
echo "🔍 Checking for Decision: patterns..."

find $MEMORY_DIR -name "*.md" -type f -mtime -30 ! -path "$MEMORY_DIR/people/*" ! -path "$MEMORY_DIR/decisions/*" ! -path "$MEMORY_DIR/mistakes/*" ! -path "$MEMORY_DIR/improvements/*" ! -path "$MEMORY_DIR/backups/*" ! -path "$MEMORY_DIR/archive/*" ! -name "auto-learned.md" ! -name "permanent.md" -exec grep -l "^[\*•] Decision:\|^\*\*Decision:" {} \; 2>/dev/null | while read -r file; do
    filename=$(basename "$file" .md)
    
    grep "^[\*•] Decision:\|^\*\*Decision:" "$file" 2>/dev/null | while read -r line; do
        # Extract decision text (remove the prefix)
        decision_text=$(echo "$line" | sed 's/^[\*•] Decision: //' | sed 's/^\*\*Decision: //' | xargs)
        
        if [ -n "$decision_text" ] && [ "$decision_text" != "Decision:" ]; then
            # Check if this decision already exists
            if ! grep -q "$decision_text" "$DECISIONS_DIR/memory-system.md" 2>/dev/null; then
                echo "" >> "$DECISIONS_DIR/memory-system.md"
                echo "## $(date +%Y-%m-%d)" >> "$DECISIONS_DIR/memory-system.md"
                echo "**Decision:** $decision_text" >> "$DECISIONS_DIR/memory-system.md"
                echo "*(Promoted from: $filename)*" >> "$DECISIONS_DIR/memory-system.md"
                echo "PROMOTED: $decision_text"
                ((PROMOTED_COUNT++))
            fi
        fi
    done
done

if [ $PROMOTED_COUNT -gt 0 ]; then
    echo ""
    echo "✅ Decision promotion complete!"
    echo "📋 Total decisions promoted: $PROMOTED_COUNT"
    echo "📁 Updated: $DECISIONS_DIR/memory-system.md"
else
    echo ""
    echo "ℹ️ No new decisions to promote."
    echo "📁 Decisions folder: $DECISIONS_DIR/"
fi

exit 0