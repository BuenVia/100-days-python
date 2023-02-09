from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzerInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        self.score_label = Label(text="Score", fg="#fff", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(row=0, column=1, padx=20, pady=20)
        
        self.question_area = Canvas(width=300, height=250, bg="#fff")
        self.question_text = self.question_area.create_text(
            150, 125, 
            width=280,
            text="Question Text", 
            font=("Arial", 16, "italic"))
        self.question_area.grid(row=1 , column=0, columnspan=2, padx=20, pady=20)
        
        self.correct_img = PhotoImage(file="./quizzler/images/true.png")
        self.correct_btn = Button(image=self.correct_img, highlightthickness=0, command=self.true_pressed())
        self.correct_btn.grid(row=2, column=0, padx=20, pady=20)
        
        self.wrong_img = PhotoImage(file="./quizzler/images/false.png")
        self.wrong_btn = Button(image=self.wrong_img, highlightthickness=0, command=self.false_pressed())
        self.wrong_btn.grid(row=2, column=1, padx=20, pady=20)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.question_area.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        self.quiz.check_answer(user_answer="true")

    def false_pressed(self):
        self.quiz.check_answer(user_answer="false")
