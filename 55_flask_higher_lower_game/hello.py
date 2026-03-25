from flask import Flask

app = Flask(__name__)

#construct decorators
#make a string bold
def make_bold(function):
    def wrapper (*args, **kwargs):
        result = function(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper

#make a string italic
def make_italic(function):
    def wrapper (*args, **kwargs):
        result = function(*args, **kwargs)
        return f"<em>{result}</em>"
    return wrapper

#make a string underlined
def make_underlined(function):
    def wrapper (*args, **kwargs):
        result = function(*args, **kwargs)
        return f"<u>{result}</u>"
    return wrapper

#define app routes
@app.route("/")
def hello_world():
    #Rendering HTML elements
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a paragraph.</p>" \

#Different routes using the the app.route decorator
@app.route("/bye")
@make_bold
@make_italic
@make_underlined
def bye():
    return "Bye!"

#Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old."

if __name__ == "__main__":
    #Run app in debug mode to auto-reload
    app.run(debug=True)