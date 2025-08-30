import requests
import json
from bs4 import BeautifulSoup
import urllib.parse
from datetime import datetime

def fetch_page(url: str, timeout: int = 10) -> dict:
    """
    Fetch raw page content with comprehensive error handling

    Returns:
        dict: Contains 'success', 'content', 'error', 'status_code', 'content_type'
    """
    try:
        # Validate URL
        parsed = urllib.parse.urlparse(url)
        if not parsed.scheme:
            url = f"https://{url}"

        # Set headers to mimic a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

        response = requests.get(url, timeout=timeout, headers=headers, verify=True)
        response.raise_for_status()

        return {
            'success': True,
            'content': response.text,
            'status_code': response.status_code,
            'content_type': response.headers.get('content-type', '').lower(),
            'url': response.url,
            'error': None
        }

    except requests.exceptions.Timeout:
        return {
            'success': False,
            'content': None,
            'error': f"Request timeout after {timeout} seconds",
            'status_code': None,
            'content_type': None
        }
    except requests.exceptions.ConnectionError:
        return {
            'success': False,
            'content': None,
            'error': "Connection error - check your internet connection",
            'status_code': None,
            'content_type': None
        }
    except requests.exceptions.HTTPError as e:
        return {
            'success': False,
            'content': None,
            'error': f"HTTP Error {e.response.status_code}: {e.response.reason}",
            'status_code': e.response.status_code,
            'content_type': None
        }
    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'content': None,
            'error': f"Request error: {str(e)}",
            'status_code': None,
            'content_type': None
        }

def pretty_fetch(url: str, lines: int = 20) -> str:
    """
    Fetch webpage and pretty-print content with intelligent formatting
    - Detect JSON: pretty-print with indentation
    - Detect HTML: extract visible text
    - Otherwise: raw text
    """
    print(f"🌐 Fetching: {url}")

    result = fetch_page(url)

    if not result['success']:
        return f"❌ Error fetching URL: {result['error']}"

    raw_content = result['content']
    content_type = result['content_type'] or ''

    # Add metadata header
    output_lines = [
        f"📊 Fetch Results for: {url}",
        f"🕒 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"📋 Status: {result['status_code']} | Type: {content_type}",
        "=" * 60,
        ""
    ]

    try:
        # Try JSON first
        if 'json' in content_type or raw_content.strip().startswith(('{', '[')):
            try:
                data = json.loads(raw_content)
                pretty_json = json.dumps(data, indent=2, ensure_ascii=False)
                content_lines = pretty_json.splitlines()
                output_lines.append("📄 Content Type: JSON")
                output_lines.append("-" * 30)
                output_lines.extend(content_lines[:lines-len(output_lines)])
                return "\n".join(output_lines)
            except json.JSONDecodeError:
                pass

        # Try HTML
        if 'html' in content_type or '<html' in raw_content.lower():
            try:
                soup = BeautifulSoup(raw_content, "html.parser")

                # Remove script and style elements
                for script in soup(["script", "style"]):
                    script.decompose()

                # Get text and clean it up
                text = soup.get_text(separator="\n")
                clean_lines = []

                for line in text.split('\n'):
                    line = line.strip()
                    if line and len(line) > 1:  # Skip empty lines and single chars
                        clean_lines.append(line)

                output_lines.append("📄 Content Type: HTML (text extracted)")
                output_lines.append("-" * 30)

                # Add title if available
                title = soup.find('title')
                if title:
                    output_lines.append(f"📌 Title: {title.get_text().strip()}")
                    output_lines.append("")

                output_lines.extend(clean_lines[:lines-len(output_lines)])
                return "\n".join(output_lines)

            except Exception as e:
                output_lines.append(f"⚠️  HTML parsing error: {e}")
                output_lines.append("📄 Falling back to raw text")
                output_lines.append("-" * 30)

        # Fallback to raw text
        output_lines.append("📄 Content Type: Plain Text")
        output_lines.append("-" * 30)

        text_lines = raw_content.splitlines()
        remaining_lines = lines - len(output_lines)
        output_lines.extend(text_lines[:remaining_lines])

        return "\n".join(output_lines)

    except Exception as e:
        return f"❌ Error processing content: {str(e)}"

def save_content(url: str, filename: str = None) -> bool:
    """
    Save fetched content to a file
    """
    try:
        result = fetch_page(url)

        if not result['success']:
            print(f"❌ Failed to fetch content: {result['error']}")
            return False

        if not filename:
            # Generate filename from URL
            parsed = urllib.parse.urlparse(url)
            domain = parsed.netloc.replace('www.', '')
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{domain}_{timestamp}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(result['content'])

        print(f"💾 Content saved to: {filename}")
        return True

    except Exception as e:
        print(f"❌ Error saving content: {e}")
        return False

def check_url_status(url: str) -> dict:
    """
    Quick URL status check without fetching full content
    """
    try:
        response = requests.head(url, timeout=5)
        return {
            'url': url,
            'status_code': response.status_code,
            'accessible': response.status_code < 400,
            'content_type': response.headers.get('content-type', 'unknown'),
            'content_length': response.headers.get('content-length', 'unknown')
        }
    except Exception as e:
        return {
            'url': url,
            'status_code': None,
            'accessible': False,
            'error': str(e)
        }
