from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE = 0

class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.text_score = Label(text=f"Score: {SCORE}", anchor=CENTER, bg=THEME_COLOR, fg= "white", font=("Arial", 15,
                                                                                                          "bold"))
        self.text_score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question", font=("Arial", 20, "italic"),
                                                     width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.image_true = PhotoImage(file="./images/true.png")
        self.button_true = Button(image=self.image_true, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(column=0, row=2)

        self.image_false = PhotoImage(file="./images/false.png")
        self.button_false = Button(image=self.image_false, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="YOU HAVE ANSWERED ALL QUESTIONS")
            self.button_false.config(state=DISABLED)
            self.button_true.config(state=DISABLED)

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            global SCORE
            SCORE += 1
            self.text_score.config(text=f"Score: {SCORE}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)