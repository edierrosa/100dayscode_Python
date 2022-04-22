from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip


# Password generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# Save password
def add_password():
    website = website_entry.get()
    email_user = email_user_entry.get()
    password_value = password_entry.get()
    # Validate entries
    if len(website) == 0 or len(password_value) == 0:
        messagebox.showinfo(
            title="Oops!", message="Please, make sure you haven't left any fileds empty.")
    else:
        confirm_data = messagebox.askokcancel(
            title=website, message=f"Website: {website}\nEmail/Username: {email_user}\nPassword: {password_value}\nPlease, confirm the details:")

        if confirm_data:
            with open(f"./day_29/data.txt", "a") as data:
                new_entry = f"{website} | {email_user} | {password_value}\n"
                data.write(new_entry)
            website_entry.delete(0, END)
            # email_user_entry.delete(0, END)
            password_entry.delete(0, END)


# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

# Canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
padlock_img = PhotoImage(file="./day_29/logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username:", bg="white")
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_user_entry = Entry()
email_user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_user_entry.insert(0, "youremail@yourprovider.dummy")

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
generate_button = Button(text="Generate Password",
                         highlightthickness=0, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
