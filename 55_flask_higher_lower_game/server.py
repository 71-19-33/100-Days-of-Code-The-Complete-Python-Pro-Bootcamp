from flask import Flask
from random import randint

app = Flask(__name__)

number_generated = randint(0,9)

#define app routes
@app.route("/")
def hello_world():
    #Rendering HTML elements
    
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"\


@app.route("/<int:number_guessed>")
def check_guess(number_guessed):
    if number_guessed == number_generated:
        return "<h1 style='color: green'>You found me!</h1>" \
                   "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif number_guessed < number_generated:
        return "<h1 style='color: red'>Too low, try again</h1>" \
                   "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 style='color: purple'>Too high, try again</h1>" \
                   "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"

if __name__ == "__main__":
    #Run app in debug mode to auto-reload
    app.run(debug=True)