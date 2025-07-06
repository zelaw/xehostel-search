from flask import Flask, render_template, request
import json

app = Flask(__name__)
DATA_FILE = "xehostel_posts.json"

def search_posts(query):
    query = query.lower()
    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            posts = json.load(f)
    except FileNotFoundError:
        return []
    return [p for p in posts if query in p["title"].lower() or query in p["content"].lower()]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get("q", "")
    results = search_posts(q)
    return render_template("results.html", query=q, results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
