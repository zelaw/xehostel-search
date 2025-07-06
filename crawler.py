import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://xehostel.blogspot.com/"
POST_LIMIT = 20  # 가져올 최대 글 수

def crawl():
    posts = []

    print(f"Crawling {BASE_URL}")
    res = requests.get(BASE_URL)
    soup = BeautifulSoup(res.text, "html.parser")

    post_elements = soup.select("h3.post-title.entry-title a")

    for i, a_tag in enumerate(post_elements):
        if i >= POST_LIMIT:
            break

        title = a_tag.get_text(strip=True)
        link = a_tag["href"]

        # 본문 일부 요약 가져오기
        post_res = requests.get(link)
        post_soup = BeautifulSoup(post_res.text, "html.parser")
        content_elem = post_soup.select_one(".post-body")
        summary = content_elem.get_text(strip=True)[:200] if content_elem else ""

        posts.append({
            "title": title,
            "link": link,
            "summary": summary
        })

    with open("xehostel_posts.json", "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(posts)} posts saved to xehostel_posts.json")

if __name__ == "__main__":
    crawl()
