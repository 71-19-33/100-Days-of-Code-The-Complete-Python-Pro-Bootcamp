from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    return ("Name: " + request.form["username"] + " / Password: " + request.form["password"])

if __name__ == "__main__":
    app.run(debug=True)