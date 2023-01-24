import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)

# Routes the home page iterating the JSON file to populate the blog
@app.route('/')
def home():
    year = datetime.date.today().year
    request = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = request.json()
    return render_template("index.html", blogPost=request.json(), allPost=all_posts, year=year)


# Redirects to blog post specific to the ID to read the fill body of the post
@app.route("/blog/<int:num>")
def get_blog(num):
    year = datetime.date.today().year
    request = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = request.json()
    return render_template("post.html", blogPost=request.json(), allPost=all_posts, num=num, year=year)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
