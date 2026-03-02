#!/usr/bin/env python3
"""
Regulatory Intelligence Feed - Daily scraper
Simple RSS parser for regulatory sources
"""

import requests
from datetime import datetime
import json
import re

SOURCES = {
    'sec': {
        'url': 'https://www.sec.gov/news/pressreleases.rss',
        'name': 'SEC',
    },
    'fincen': {
        'url': 'https://www.fincen.gov/news/rss/all',
        'name': 'FinCEN',
    },
}

def fetch_url(url):
    """Fetch URL with headers"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return None

def parse_rss_simple(xml_text):
    """Simple regex-based RSS parser"""
    items = re.findall(r'<item>(.*?)</item>', xml_text, re.DOTALL)
    
    results = []
    for item in items[:10]:
        title_match = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', item, re.DOTALL)
        link_match = re.search(r'<link>(.*?)</link>', item)
        desc_match = re.search(r'<description>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</description>', item, re.DOTALL)
        
        if title_match:
            results.append({
                'title': title_match.group(1).strip(),
                'link': link_match.group(1).strip() if link_match else '',
                'description': desc_match.group(1).strip()[:200] if desc_match else ''
            })
    
    return results

def categorize(text):
    """Categorize by fintech sector"""
    text = text.lower()
    
    keywords = {
        'crypto': ['crypto', 'bitcoin', 'ethereum', 'token', 'digital asset', 'virtual currency'],
        'payments': ['payment', 'transfer', 'remittance', 'money transmission', 'venmo', 'paypal'],
        'lending': ['lending', 'credit', 'loan', 'interest rate', 'borrow'],
        'banking': ['bank', 'charter', 'fdic', 'occ', 'federal reserve'],
        'aml': ['aml', 'anti-money', 'kyc', 'know your customer', 'suspicious', 'BSA'],
        'securities': ['securities', 'investment', 'registration', 'offering', 'SEC'],
        'privacy': ['privacy', 'data protection', 'gdpr', 'ccpa', 'breach'],
    }
    
    categories = []
    for cat, words in keywords.items():
        if any(word in text for word in words):
            categories.append(cat)
    
    return categories if categories else ['general']

def generate_briefing():
    """Generate daily briefing"""
    briefing = {
        'date': datetime.now().isoformat()[:10],
        'updates': [],
        'summary': {'total': 0, 'by_category': {}}
    }
    
    for source_id, source_info in SOURCES.items():
        xml = fetch_url(source_info['url'])
        if xml:
            items = parse_rss_simple(xml)
            for item in items:
                text = item['title'] + ' ' + item['description']
                cats = categorize(text)
                
                briefing['updates'].append({
                    'source': source_info['name'],
                    'title': item['title'],
                    'link': item['link'],
                    'categories': cats
                })
                
                briefing['summary']['total'] += 1
                for cat in cats:
                    briefing['summary']['by_category'][cat] = briefing['summary']['by_category'].get(cat, 0) + 1
    
    return briefing

if __name__ == "__main__":
    b = generate_briefing()
    
    print(f"📋 REGULATORY BRIEFING - {b['date']}")
    print(f"Updates: {b['summary']['total']}")
    print(f"Categories: {b['summary']['by_category']}")
    print("\n---")
    
    for u in b['updates'][:5]:
        print(f"• [{u['source']}] {u['title'][:70]}")
        print(f"  Tags: {', '.join(u['categories'])}")
