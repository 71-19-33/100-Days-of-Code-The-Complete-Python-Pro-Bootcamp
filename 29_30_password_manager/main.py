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
        try:
            with open("data.json", "r") as data_file:
                # Read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving new data
                json.dump(new_data, data_file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent = 4)
        finally:
            website_entry1_1.delete(0, END)
            password_entry1_3.delete(0, END)
# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = website_entry1_1.get()
    if len(website) == 0:
        messagebox.showinfo("Oops", "Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                query = data[website]
        except FileNotFoundError:
            messagebox.showinfo("Oops", "No Data File Found")
        except KeyError:
            messagebox.showinfo("Oops", "No details for the website exists")
        else:
            messagebox.showinfo(title=website, message=f"Email: {query['email']}\nPassword: {query['password']}")

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

website_entry1_1 = Entry(width=33)
website_entry1_1.grid(column=1, row=1)
website_entry1_1.focus()

mail_entry1_2 = Entry(width=52)
mail_entry1_2.grid(column=1, row=2, columnspan=2)
mail_entry1_2.insert(0, "mustermann_max@test.de")

password_entry1_3 = Entry(width=33)
password_entry1_3.grid(column=1, row=3)

add_button1_4 = Button(text="Add", width=44, command=save)
add_button1_4.grid(column=1, row=4, columnspan=2)

#---column2
button2_1 = Button(text="Search", width= 15,command=find_password)
button2_1.grid(column=2, row=1)


button2_3 = Button(text="Generate Password", command=generate_password)
button2_3.grid(column=2, row=3)
# ---------------------------- END ------------------------------- #
window.mainloop()