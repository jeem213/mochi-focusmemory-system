#!/usr/bin/env python3
"""
Enhanced Python Backup Script
Better compression, manifest, integrity checks, and auto-cleanup!
"""

import os
import zipfile
import json
from datetime import datetime
from pathlib import Path
import shutil

BASE = Path("/home/openclaw/.openclaw/workspace-mochi")
BACKUP_DIR = BASE / "memory" / "backups"

def create_backup(include_skills=True, include_memory=True):
    """Create an enhanced backup with manifest and verification."""
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    backup_name = f"memory_backup_{timestamp}"
    
    print("🚀 Creating Enhanced Python Backup...")
    print(f"   Timestamp: {timestamp}")
    
    items_backed_up = []
    total_size = 0
    
    # Create zip file
    zip_path = BACKUP_DIR / f"{backup_name}.zip"
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        
        # Backup memory folder
        if include_memory:
            memory_dir = BASE / "memory"
            for file in memory_dir.rglob("*.md"):
                if "memory-report.html" not in str(file):  # Skip generated reports
                    arcname = f"memory/{file.relative_to(BASE)}"
                    zipf.write(file, arcname)
                    items_backed_up.append(arcname)
                    total_size += file.stat().st_size
        
        # Backup skills folder
        if include_skills:
            skills_dir = BASE / "skills"
            for file in skills_dir.rglob("*.md"):
                arcname = f"skills/{file.relative_to(BASE)}"
                zipf.write(file, arcname)
                items_backed_up.append(arcname)
                total_size += file.stat().st_size
        
        # Backup config files
        config_files = ["SOUL.md", "AGENTS.md", "IDENTITY.md", "USER.md"]
        for cf in config_files:
            file = BASE / cf
            if file.exists():
                arcname = cf
                zipf.write(file, arcname)
                items_backed_up.append(arcname)
                total_size += file.stat().st_size
        
        # Create and add manifest
        manifest = {
            "timestamp": timestamp,
            "items": items_backed_up,
            "total_items": len(items_backed_up),
            "total_size_bytes": total_size,
            "total_size_mb": round(total_size / 1024 / 1024, 2),
            "include_skills": include_skills,
            "include_memory": include_memory,
            "created_by": "Mochi Python Backup Script v1.0"
        }
        
        zipf.writestr("manifest.json", json.dumps(manifest, indent=2))
        items_backed_up.append("manifest.json")
    
    # Get final size
    final_size = zip_path.stat().st_size
    
    print(f"   ✅ Created: {backup_name}.zip")
    print(f"   📦 Items: {len(items_backed_up)}")
    print(f"   💾 Size: {round(final_size / 1024, 2)} KB")
    print(f"   📍 Location: {BACKUP_DIR}/{backup_name}.zip")
    
    # Auto-cleanup old backups (keep last 10)
    cleanup_old_backups(10)
    
    return {
        "name": backup_name,
        "items": len(items_backed_up),
        "size": round(final_size / 1024, 2),
        "path": str(zip_path)
    }

def cleanup_old_backups(keep_count=10):
    """Auto-cleanup old backups, keeping only the most recent."""
    backups = sorted(BACKUP_DIR.glob("memory_backup_*.zip"), 
                     key=lambda x: x.stat().st_mtime, 
                     reverse=True)
    
    if len(backups) > keep_count:
        removed = 0
        for old_backup in backups[keep_count:]:
            old_backup.unlink()
            removed += 1
        if removed > 0:
            print(f"   🧹 Auto-cleaned {removed} old backups")

def verify_backup(zip_path):
    """Verify a backup is valid and readable."""
    print(f"\n🔍 Verifying backup: {zip_path}")
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            # Test the zip is valid
            bad_file = zipf.testzip()
            if bad_file:
                print(f"   ❌ Corrupted file: {bad_file}")
                return False
            
            # Read manifest if exists
            if "manifest.json" in zipf.namelist():
                manifest = json.loads(zipf.read("manifest.json"))
                print(f"   ✅ Valid backup!")
                print(f"   📦 Items: {manifest.get('total_items', 'N/A')}")
                print(f"   💾 Size: {manifest.get('total_size_mb', 'N/A')} MB")
                print(f"   📅 Created: {manifest.get('timestamp', 'N/A')}")
                return True
            else:
                print(f"   ⚠️ No manifest found")
                return True
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def list_backups():
    """List all available backups."""
    print("\n📋 Available Backups:")
    backups = sorted(BACKUP_DIR.glob("memory_backup_*.zip"), 
                     reverse=True)
    
    for i, backup in enumerate(backups, 1):
        size_kb = round(backup.stat().st_size / 1024, 1)
        mtime = datetime.fromtimestamp(backup.stat().st_mtime)
        print(f"   {i}. {backup.stem} ({size_kb} KB) - {mtime.strftime('%Y-%m-%d %H:%M')}")
    
    return backups

def restore_backup(backup_name, restore_to=None):
    """Restore from a backup."""
    backup_path = BACKUP_DIR / backup_name
    
    if not backup_path.exists():
        print(f"❌ Backup not found: {backup_name}")
        return False
    
    print(f"📥 Restoring from: {backup_name}")
    
    with zipfile.ZipFile(backup_path, 'r') as zipf:
        extract_to = restore_to if restore_to else BASE
        zipf.extractall(extract_to)
    
    print(f"   ✅ Restored to: {extract_to}")
    return True

# CLI
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("""
🐹 Mochi Python Backup Script

Usage:
  python3 python-backup.py backup     # Create backup
  python3 python-backup.py list       # List backups
  python3 python-backup.py verify     # Verify latest backup
  python3 python-backup.py restore [filename]  # Restore backup
  python3 python-backup.py clean      # Clean old backups
        """)
    
    command = sys.argv[1] if len(sys.argv) > 1 else "help"
    
    if command == "backup":
        create_backup()
    elif command == "list":
        list_backups()
    elif command == "verify":
        backups = list_backups()
        if backups:
            verify_backup(backups[0])
    elif command == "restore" and len(sys.argv) > 2:
        restore_backup(sys.argv[2])
    elif command == "clean":
        cleanup_old_backups(0)  # Clean all
        print("✅ Cleaned all old backups")
    else:
        print("Unknown command")