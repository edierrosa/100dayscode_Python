from tkinter import *
import requests


def get_quote():
    get_data = requests.get(url="https://api.kanye.rest")
    get_data.raise_for_status()
    data = get_data.json()
    canvas.itemconfig(quote_text, text=data["quote"])


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(
    file="./day_33/day_33_challenge_1-kanye_quotes_app/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Ready for some Kanye 'wisdom'? ", width=250, font=(
    "Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(
    file="./day_33/day_33_challenge_1-kanye_quotes_app/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
