from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # UI window setup
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Set canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Question", fill=THEME_COLOR,
            font=("Arial", 14, "italic"))
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)

        # Set buttons
        right_image = PhotoImage(file="./day_34/images/true.png")
        self.right_button = Button(
            image=right_image, highlightthickness=0, border=0, activebackground=THEME_COLOR, command=self.right_pressed)
        self.right_button.grid(column=0, row=2)

        wrong_image = PhotoImage(file="./day_34/images/false.png")
        self.wrong_button = Button(
            image=wrong_image, highlightthickness=0, border=0, activebackground=THEME_COLOR, command=self.wrong_pressed)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="That's the end!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_pressed(self):
        self.feedback(self.quiz.check_answer("True"))

    def wrong_pressed(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
