from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/blog')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template("index.html", post=all_post)



@app.route("/post/<int:num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()[num - 1]
    return render_template("post.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
