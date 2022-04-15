from tkinter import *
# from tkinter.font import *


def convert():
    """Convert miles to km"""
    miles_entry = float(entry.get())
    value_label["text"] = f"{miles_entry * 1.609344:.3f}"


# Create window
window = Tk()

# Change default font size
# default_font = nametofont("TkDefaultFont")
# default_font.configure(size=11)
# window.option_add("*Font", "@MicrosoftJhengHeiLight")

window.title("Convert Miles to Km")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


# Miles entry
entry = Entry(width=15)
entry.insert(END, 0)
entry.grid(column=1, row=0)

# Labels
miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

value_label = Label(text="0")
value_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

# Buttons

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)


window.mainloop()
