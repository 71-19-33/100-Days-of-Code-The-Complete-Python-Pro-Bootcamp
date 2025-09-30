from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPETITIONS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global REPETITIONS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    text1_0.config(text="Timer")
    text1_3.config(text="")
    REPETITIONS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPETITIONS
    REPETITIONS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPETITIONS % 8 == 0:
        text1_0.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif REPETITIONS % 2 == 0:
        text1_0.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        text1_0.config(text="Work")
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = "✓ " * int(REPETITIONS/2)
        if REPETITIONS % 2 == 0:
            text1_3.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#---layout
#----------column0
#start button
button0_2 = Button(text="Start", command=start_timer)
button0_2.grid(column=0, row=2)

#----------column1
#title
text1_0 = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
text1_0.grid(column=1, row=0)

#graphic
#load image
tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#check mark
text1_3 = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
text1_3.grid(column=1, row=3)

#----------column2
#reset button
button2_2 = Button(text="Reset", command=reset)
button2_2.grid(column=2, row=2)
# ---------------------------- END ------------------------------- #
window.mainloop()