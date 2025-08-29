import requests
import json
from bs4 import BeautifulSoup  # optional for HTML prettify

def fetch_page(url: str) -> str:
    """Fetch raw page content"""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def pretty_fetch(url: str, lines: int = 20) -> str:
    """
    Fetch webpage and pretty-print content:
    - Detect JSON: pretty-print with indentation
    - Detect HTML: extract visible text
    - Otherwise: raw text
    """
    raw = fetch_page(url)

    # try JSON
    try:
        data = json.loads(raw)
        pretty = json.dumps(data, indent=4)
        return "\n".join(pretty.splitlines()[:lines])
    except json.JSONDecodeError:
        pass

    # try HTML
    try:
        soup = BeautifulSoup(raw, "html.parser")
        text = soup.get_text(separator="\n")
        return "\n".join(text.splitlines()[:lines])
    except Exception:
        pass

    # fallback: raw text
    return "\n".join(raw.splitlines()[:lines])
