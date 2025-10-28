from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry1_3.delete(0, END)
    password_entry1_3.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry1_1.get()
    email = mail_entry1_2.get()
    password = password_entry1_3.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Please don't leave any fields empty")
    else:
         with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent = 4)
            website_entry1_1.delete(0, END)
            password_entry1_3.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#---column0
website_text0_1 = Label(text="Website:")
website_text0_1.grid(column=0, row=1)

mail_text0_2 = Label(text="Email/Username:")
mail_text0_2.grid(column=0, row=2)

password_text0_3 = Label(text="Password:")
password_text0_3.grid(column=0, row=3)

#---column1
lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_entry1_1 = Entry(width=52)
website_entry1_1.grid(column=1, row=1, columnspan=2)
website_entry1_1.focus()

mail_entry1_2 = Entry(width=52)
mail_entry1_2.grid(column=1, row=2, columnspan=2)
mail_entry1_2.insert(0, "mustermann_max@test.de")

password_entry1_3 = Entry(width=33)
password_entry1_3.grid(column=1, row=3)

add_button1_4 = Button(text="Add", width=44, command=save)
add_button1_4.grid(column=1, row=4, columnspan=2)

#---column2
button2_3 = Button(text="Generate Password", command=generate_password)
button2_3.grid(column=2, row=3)
# ---------------------------- END ------------------------------- #
window.mainloop()