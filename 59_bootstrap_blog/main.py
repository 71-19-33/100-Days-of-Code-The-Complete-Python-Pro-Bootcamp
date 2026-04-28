from flask import Flask, render_template
import json

app = Flask(__name__)

#api npoint somehow blocked, using a local file
with open("59_bootstrap_blog\\blog-data.json", "r") as file:
    data_blogs = json.load(file)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", data_blogs = data_blogs)

@app.route("/post/<int:blog_id>")
def post(blog_id):
    data_post = data_blogs[blog_id-1]
    return render_template("post.html", data_post = data_post)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)