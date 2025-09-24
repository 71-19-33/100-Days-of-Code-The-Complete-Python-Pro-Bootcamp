from tkinter import *

#window
window = Tk()
window.title("mi to km converter")
window.minsize(width=275, height=50)
window.config(padx=50, pady=25)

#layout
#column 0
text0_1 = Label(text="is equal to")
text0_1.grid(column=0, row=1)

#column 1
#input
miles_to_convert = Entry(width=9)
miles_to_convert.insert(END, "0")
miles_to_convert.grid(column=1, row=0)

#result
text1_1 = Label(text="0")
text1_1.grid(column=1, row=1)

def conversion():
    text1_1["text"]=round(float(miles_to_convert.get())*1.609344, 2)

#button
button1_2 = Button(text="Calculate", command=conversion)
button1_2.grid(column=1, row=2)

#column 2
text2_0 = Label(text="mi")
text2_0.grid(column=2, row=0)

text2_1 = Label(text="km")
text2_1.grid(column=2, row=1)

#---END---
window.mainloop()