from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

mail_entry1_2 = Entry(width=52)
mail_entry1_2.grid(column=1, row=2, columnspan=2)

password_entry1_3 = Entry(width=33)
password_entry1_3.grid(column=1, row=3)

add_button1_4 = Button(text="Add", width=44)
add_button1_4.grid(column=1, row=4, columnspan=2)

#---column2
button2_3 = Button(text="Generate Password")
button2_3.grid(column=2, row=3)
# ---------------------------- END ------------------------------- #
window.mainloop()