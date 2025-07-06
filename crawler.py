import requests
from bs4 import BeautifulSoup
import json, time

BASE = "https://xehostel.blogspot.com"
def crawl():
    posts, url = [], BASE
    while url:
        print("크롤링:", url)
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        for art in soup.select(".date-outer"):
            t = art.select_one(".post-title a")
            b = art.select_one(".post-body")
            d = art.select_one(".date-header span")
            if t and b:
                posts.append({
                    "title": t.text.strip(),
                    "url": t["href"],
                    "content": b.text.strip(),
                    "date": d.text.strip() if d else ""
                })
        nxt = soup.select_one("a.blog-pager-older-link")
        url = nxt["href"] if nxt else None
        time.sleep(1)
    with open("xehostel_posts.json","w",encoding="utf-8") as f:
        json.dump(posts,f,ensure_ascii=False,indent=2)
    print(f"{len(posts)}개 저장됨")

if __name__=="__main__":
    crawl()
