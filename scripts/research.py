import sys
import argparse
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

def search(query, max_results=7):
    try:
        results = DDGS().text(query, max_results=max_results)
        if not results:
            print("No results found.")
            return
            
        for i, r in enumerate(results):
            print(f"[{i+1}] Title: {r.get('title', 'No Title')}")
            print(f"    URL: {r.get('href', 'No URL')}")
            print(f"    Snippet: {r.get('body', 'No Snippet')}\n")
    except Exception as e:
        print(f"Search failed: {e}")

def read_url(url):
    try:
        # Using a standard browser User-Agent to avoid basic blocks
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
            
        # Extract text mostly from headings and paragraphs to keep it readable
        content_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'li'])
        text = '\n'.join([elem.get_text().strip() for elem in content_elements if elem.get_text().strip()])
        
        # Output limits to prevent agent token overflow
        char_limit = 15000 
        print(f"--- Content from {url} ---")
        print(text[:char_limit])
        if len(text) > char_limit:
            print(f"\n...[Content truncated at {char_limit} characters]...")
            
    except Exception as e:
        print(f"Failed to read URL: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deep Research Web Tools")
    parser.add_argument("action", choices=["search", "read"], help="Action to perform: 'search' for web search, 'read' to scrape a URL")
    parser.add_argument("target", help="The search query or the URL to read")
    
    args = parser.parse_args()
    
    if args.action == "search":
        print(f"Searching for: '{args.target}'...\n")
        search(args.target)
    elif args.action == "read":
        print(f"Reading: '{args.target}'...\n")
        read_url(args.target)
