from flask import Flask, render_template, request
import json

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
#api npoint somehow blocked, using a local file
with open("60_html_forms\\blog-data.json", "r") as file:
    data_blogs = json.load(file)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=data_blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html",msg_sent=True)
    else:
        return render_template("contact.html",msg_sent=False)  


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data_blogs:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
