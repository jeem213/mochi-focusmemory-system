#!/usr/bin/env python3
"""
Web Research & HTML Parsing Tool
Extract data from any webpage using BeautifulSoup!
"""

import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
import sys
from pathlib import Path

# Use venv Python
PYTHON = "/home/openclaw/.venv/bin/python"

def fetch_page(url):
    """Fetch a page and return BeautifulSoup object."""
    print(f"🌐 Fetching: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"   ✅ Fetched {len(response.text)} bytes")
        return soup
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return None

def extract_text(url, clean=True):
    """Extract clean text from a page."""
    soup = fetch_page(url)
    if not soup:
        return None
    
    if clean:
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text and clean whitespace
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
    
    return text

def extract_links(url):
    """Extract all links from a page."""
    soup = fetch_page(url)
    if not soup:
        return []
    
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        text = link.get_text().strip()
        
        if href:
            # Make absolute URL
            full_url = urljoin(url, href)
            links.append({
                'url': full_url,
                'text': text if text else full_url
            })
    
    return links

def extract_tables(url):
    """Extract all tables as data."""
    soup = fetch_page(url)
    if not soup:
        return []
    
    tables = []
    for i, table in enumerate(soup.find_all('table')):
        rows = []
        for row in table.find_all('tr'):
            cells = row.find_all(['th', 'td'])
            row_data = [cell.get_text().strip() for cell in cells]
            if row_data:
                rows.append(row_data)
        
        if rows:
            tables.append({
                'table_num': i + 1,
                'rows': len(rows),
                'data': rows
            })
    
    return tables

def extract_headings(url):
    """Extract all headings (h1-h6)."""
    soup = fetch_page(url)
    if not soup:
        return {}
    
    headings = {'h1': [], 'h2': [], 'h3': [], 'h4': [], 'h5': [], 'h6': []}
    
    for level in headings:
        for heading in soup.find_all(level):
            text = heading.get_text().strip()
            if text:
                headings[level].append(text)
    
    return headings

def extract_article(url):
    """Extract main article content - tries common patterns."""
    soup = fetch_page(url)
    if not soup:
        return None
    
    # Try to find main content
    article = None
    
    # Try article tag
    article = soup.find('article')
    if not article:
        # Try main tag
        article = soup.find('main')
    if not article:
        # Try common class names
        article = soup.find(class_=lambda x: x and ('content' in x.lower() or 'article' in x.lower()))
    if not article:
        # Fall back to body
        article = soup.find('body')
    
    if article:
        # Remove unwanted elements
        for unwanted in article(["script", "style", "nav", "footer", "header"]):
            unwanted.decompose()
        
        # Get text
        text = article.get_text()
        
        # Clean whitespace
        lines = (line.strip() for line in text.splitlines())
        text = ' '.join(line for line in lines if line)
        
        return text[:5000]  # Limit to 5000 chars
    
    return None

def extract_meta(url):
    """Extract meta tags from page."""
    soup = fetch_page(url)
    if not soup:
        return {}
    
    meta = {}
    
    # Title
    if soup.title:
        meta['title'] = soup.title.string
    
    # Meta tags
    for tag in soup.find_all('meta'):
        name = tag.get('name') or tag.get('property')
        content = tag.get('content')
        if name and content:
            meta[name] = content
    
    return meta

def research(url, what_to_find):
    """Custom research - find specific things on a page."""
    soup = fetch_page(url)
    if not soup:
        return []
    
    results = []
    
    what = what_to_find.lower()
    
    if 'link' in what:
        results = extract_links(url)
    elif 'table' in what:
        results = extract_tables(url)
    elif 'heading' in what:
        results = extract_headings(url)
    elif 'article' in what or 'content' in what:
        content = extract_article(url)
        results = [{'content': content[:2000]}] if content else []
    elif 'meta' in what:
        results = extract_meta(url)
    else:
        # Default - search for text
        text = soup.get_text()
        if what in text.lower():
            # Find context around the term
            import re
            matches = re.finditer(r'.{0,50}' + what + r'.{0,50}', text, re.IGNORECASE)
            for match in matches:
                results.append({'context': match.group()})
    
    return results

# CLI
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("""
🔍 Mochi Web Research Tool

Usage:
  python3 web-research.py fetch <url>              - Fetch and show basic info
  python3 web-research.py links <url>               - Extract all links
  python3 web-research.py tables <url>              - Extract all tables
  python3 web-research.py headings <url>           - Extract all headings
  python3 web-research.py article <url>              - Extract main article
  python3 web-research.py meta <url>                - Extract meta tags
  python3 web-research.py research <url> <query>    - Custom research
        """)
        sys.exit(1)
    
    command = sys.argv[1]
    url = sys.argv[2]
    
    if command == "fetch":
        soup = fetch_page(url)
        if soup and soup.title:
            print(f"\n📄 Title: {soup.title.string}")
            print(f"📝 Links: {len(soup.find_all('a'))}")
            print(f"📊 Tables: {len(soup.find_all('table'))}")
            print(f"📑 Headings: {len(soup.find_all(['h1','h2','h3']))}")
    
    elif command == "links":
        links = extract_links(url)
        print(f"\n🔗 Found {len(links)} links:")
        for link in links[:10]:
            print(f"   - {link['text'][:50]}: {link['url']}")
    
    elif command == "tables":
        tables = extract_tables(url)
        print(f"\n📊 Found {len(tables)} tables:")
        for table in tables:
            print(f"   Table {table['table_num']}: {table['rows']} rows")
    
    elif command == "headings":
        headings = extract_headings(url)
        print(f"\n📑 Headings:")
        for level, items in headings.items():
            if items:
                print(f"   {level.upper()}: {len(items)}")
                for h in items[:3]:
                    print(f"      - {h[:60]}")
    
    elif command == "article":
        article = extract_article(url)
        if article:
            print(f"\n📄 Article Content (first 500 chars):")
            print(article[:500])
        else:
            print("❌ Could not extract article")
    
    elif command == "meta":
        meta = extract_meta(url)
        print(f"\n🏷️ Meta Tags:")
        for key, value in meta.items():
            print(f"   {key}: {value}")
    
    elif command == "research":
        query = sys.argv[3] if len(sys.argv) > 3 else "link"
        results = research(url, query)
        print(f"\n🔍 Research results for '{query}':")
        for r in results[:5]:
            print(f"   - {r}")
    
    else:
        print("Unknown command")