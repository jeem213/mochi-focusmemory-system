# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

---

### GitHub Repos

- **mochi-backup** → Private repo: `https://github.com/jeem213/mochi-backup`
- **mochi-focusmemory-system** → Public repo: `https://github.com/jeem213/mochi-focusmemory-system`

**Token:** See `API_KEYS.md`

**To push to different repos:**
```bash
git remote set-url origin https://TOKEN@github.com/jeem213/REPO_NAME.git
git push origin main
```

Or configure in `~/.gitconfig` with multiple remotes (like Stuart's workspace).

---

### Python Scripts (via /home/openclaw/.venv/bin/python)

- **memory-report.py** → Generates HTML memory dashboard
  - Run: `python scripts/memory-report.py`
  - Output: `memory/memory-report.html`

- **fast-search.py** → SQLite fast search + analytics
  - Run: `python scripts/fast-search.py [rebuild|analytics|search]`
  - Database: `memory/memory-search.db`

- **python-backup.py** → Enhanced Python backup
  - Run: `python scripts/python-backup.py [backup|list|verify|restore]`
  - Output: `memory/backups/memory_backup_*.zip`

- **web-research.py** → HTML parsing + web scraping
  - Run: `python scripts/web-research.py [fetch|links|tables|headings|article|meta|research]`
  - Requires: BeautifulSoup4 (installed in venv)
