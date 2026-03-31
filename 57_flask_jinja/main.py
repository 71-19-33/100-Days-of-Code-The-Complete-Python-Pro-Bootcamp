from flask import Flask, render_template
import json


app = Flask(__name__)

#api npoint somehow blocked, using a local file
with open("57_flask_jinja\\blog-data.json", "r") as file:
    data_blogs = json.load(file)

@app.route('/')
def home():
    return render_template("index.html", data_blogs = data_blogs)

@app.route("/post/<int:blog_id>")
def post(blog_id):
    data_post = data_blogs[blog_id-1]
    return render_template("post.html", data_post = data_post)

if __name__ == "__main__":
    app.run(debug=True)
