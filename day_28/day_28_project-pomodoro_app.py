import math
from tkinter import *

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Timer reset


def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Ready?")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0

# Timer Mechanism


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

# Avoid bug when start button's clicked during execution


def start_timer_button():
    if reps == 0:
        start_timer()
    else:
        pass

# Countsown Mechanism


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:0>2}:{count_sec:0>2}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        sessions = math.floor(reps/2)
        for _ in range(sessions):
            marks += "🗸"
        check_label.config(text=marks)


# UI setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas image and text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./day_28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Labels
title_label = Label(text="Ready?", bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
check_label.config(pady=10)
check_label.grid(column=1, row=3)

# Buttons
start_button = Button(text="Start", font=(
    FONT_NAME, 12, "bold"), highlightthickness=0,  command=start_timer_button)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(
    FONT_NAME, 12, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Loop
window.mainloop()
