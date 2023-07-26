from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain
FONT = ("Arial", 20, "italic")
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quizbrain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady=20, bg=THEME_COLOR)
        self.label = Label(text=f"Score: {self.quizbrain.score}", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)
        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.quiz_text = self.canvas.create_text(150, 125, text = "Sample Text", font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan = 2, pady=50)
        check_photo = PhotoImage(file = "images/true.png")
        self.check_button = Button(image=check_photo, bg=THEME_COLOR, command=self.true_button_command)
        self.check_button.grid(row=2, column=0)
        cross_button = PhotoImage(file="images/false.png")
        self.false_button =  Button(image=cross_button, bg=THEME_COLOR, command=self.false_button_command)
        self.false_button.grid(row=2, column=1,)
        self.display_next_question()
        self.window.mainloop()

    def display_next_question(self):
        if self.quizbrain.still_has_questions():  
            question_to_display = self.quizbrain.next_question()
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.quiz_text, text=question_to_display)
        else:
            self.game_over()
    
    def true_button_command(self):
        if self.quizbrain.check_for_true():
            self.quizbrain.score += 1
            self.label.config(text=f"Score: {self.quizbrain.score}")
            self.show_feedback(True)
        else:
            self.show_feedback(False)
        
    
    def false_button_command(self):
        if self.quizbrain.check_for_false():
            self.quizbrain.score += 1
            self.label.config(text=f"Score: {self.quizbrain.score}")
            self.show_feedback(True)
        else:
            self.show_feedback(False)

    def show_feedback(self, status):
        if status:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.display_next_question)

    def game_over(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz!")
        messagebox.showinfo("Game Over", f"Out of questions.\nYour final score: {self.quizbrain.score}/{self.quizbrain.question_number}")
        self.window.destroy()
        
