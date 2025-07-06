from flask import Flask, request, render_template
import json, os

app = Flask(__name__)

def get_posts():
    if not os.path.exists("xehostel_posts.json"):
        return []
    with open("xehostel_posts.json", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def index():
    q = request.args.get("q", "").lower()
    posts = get_posts()
    if q:
        results = [p for p in posts if q in p["title"].lower() or q in p["summary"].lower()]
    else:
        results = []
    return render_template("index.html", results=results, query=q)
