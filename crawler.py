import requests, json
from bs4 import BeautifulSoup

BASE = "https://xehostel.blogspot.com/"
LIMIT = 20

def crawl():
    res = requests.get(BASE)
    soup = BeautifulSoup(res.text, "html.parser")
    posts = []

    for i, tag in enumerate(soup.select("h3.post-title.entry-title a")):
        if i >= LIMIT: break
        link = tag['href']
        title = tag.text.strip()
        page = requests.get(link)
        body = BeautifulSoup(page.text, "html.parser").select_one(".post-body")
        summary = body.get_text(strip=True)[:300] if body else ""
        posts.append({"title": title, "link": link, "summary": summary})

    with open("xehostel_posts.json", "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    crawl()
