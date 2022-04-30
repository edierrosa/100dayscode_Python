import json
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
    website = website_entry.get().lower()
    email_user = email_user_entry.get()
    password_value = password_entry.get()
    new_entry = {
        website: {
            "email": email_user,
            "password": password_value,
        }
    }
    if len(website) == 0 or len(password_value) == 0:
        messagebox.showinfo(
            title="Oops!", message="Please, make sure you haven't left any fields empty.")
    else:
        try:
            with open("./day_30/30-4_challenges_1-2_password_manager_update/data.json", "r") as data:
                # Read existing entries
                data_entries = json.load(data)
        except FileNotFoundError:
            with open("./day_30/30-4_challenges_1-2_password_manager_update/data.json", "w") as data:
                json.dump(new_entry, data, indent=4)
        else:
            # Update existing entries
            data_entries.update(new_entry)
            with open("./day_30/30-4_challenges_1-2_password_manager_update/data.json", "w") as data:
                json.dump(data_entries, data, indent=4)
        finally:
            # Clear fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# Search existing entry
def search_entry():
    entry_search = website_entry.get().lower()
    try:
        with open("./day_30/30-4_challenges_1-2_password_manager_update/data.json", "r") as data:
            data_entries = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(
            "Data file not found. Perhaps no passwords were created yet.")
    else:
        # Check if entry already exists
        if entry_search in data_entries:
            email_user = data_entries[entry_search]["email"]
            password_value = data_entries[entry_search]["password"]
            messagebox.showinfo(title=entry_search.capitalize(
            ), message=f"Email/Username: {email_user}\nPassword: {password_value}")
        else:
            messagebox.showinfo(
                title=f"{entry_search.capitalize()} not found", message=f"No details for {entry_search} yet.")


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
website_entry.grid(column=1, row=1, sticky="EW")
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

search_button = Button(
    text="Search", width=14, highlightthickness=0, command=search_entry)
search_button.grid(column=2, row=1)


window.mainloop()
