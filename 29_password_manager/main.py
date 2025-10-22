from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_entry1_1.get()) == 0 or len(password_entry1_3.get()) == 0:
        messagebox.showinfo("Oops", "Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title= website_entry1_1.get(), message=f"These are details entered: "
                                                                      f"\nEmail: {mail_entry1_2.get()} "
                                                                      f"\nPassword: {password_entry1_3.get()} "
                                                                      f"\nIs it ok to save?")
        if is_ok is True:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_entry1_1.get()} | {mail_entry1_2.get()} | {password_entry1_3.get()}\n")
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
button2_3 = Button(text="Generate Password")
button2_3.grid(column=2, row=3)
# ---------------------------- END ------------------------------- #
window.mainloop()