from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"
from tkinter import *

FONT = ("Arial", 16, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_lbl = Label(text="Score: 0", foreground="white", background=THEME_COLOR)
        self.score_lbl.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Some text", fill=THEME_COLOR, font=FONT, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.r_image = PhotoImage(file="./images/true.png")
        self.w_image = PhotoImage(file="./images/false.png")

        self.r_button = Button(image=self.r_image, highlightthickness=0, bd=0, activebackground=THEME_COLOR, command=self.true_pressed)
        self.w_button = Button(image=self.w_image, highlightthickness=0, bd=0, activebackground=THEME_COLOR, command=self.false_pressed)
        self.r_button.grid(row=2, column=0)
        self.w_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_lbl.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=f"{q_text}")
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the quiz")
            self.r_button.config(state="disabled")
            self.w_button.config(state="disabled")

    def true_pressed(self):
        self.get_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.get_feedback(self.quiz.check_answer("false"))
    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.after(1000, self.get_next_question)

