import os
import json
from flask import Flask, request, render_template

# 크롤러 실행 (JSON 없을 때만 실행)
if not os.path.exists("xehostel_posts.json"):
    import crawler
    crawler.crawl()

app = Flask(__name__)

def load_posts():
    with open("xehostel_posts.json", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    posts = load_posts()

    if not query:
        results = []
    else:
        results = [post for post in posts if query in post["title"] or query in post["summary"]]

    return render_template("search.html", query=query, results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
