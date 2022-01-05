import bs4
import requests

def get_text(url: str) -> str:
    response = requests.get(url)
    parsed = bs4.BeautifulSoup(response.text, features='html.parser')
    text = ""
    for p in parsed.select('p'):
        text += p.getText().strip()
    return text