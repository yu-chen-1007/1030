from flask import Flask, render_template

app = Flask(__name__)

# 模擬資料庫
posts = [
    {
        "id": 1,
        "title": "第一篇文章",
        "author": "Alice",
        "content": "這是我的第一篇 Flask 部落格文章！"
    },
    {
        "id": 2,
        "title": "第二篇文章",
        "author": "Bob",
        "content": "Flask 超好用，歡迎學習 Python Web 開發。"
    }
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    article = next((p for p in posts if p["id"] == post_id), None)
    return render_template("post.html", post=article)

if __name__ == "__main__":
    app.run(debug=True)
