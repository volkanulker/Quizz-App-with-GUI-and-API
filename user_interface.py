from tkinter import *

SCORE_TEXT_COLOR = "#dddddd"
THEME_COLOR = "#222831"

from quizzler import QuizBrain

class QuizInterface:

    def __init__(self):
        self.quiz = QuizBrain()
        #Window
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR , padx=20 , pady=20)
        
        self.canvas = Canvas(width=300 , height=250 , bg="white" )
        self.canvas.grid(row=1 , column=0 , columnspan=2)
    
        #images
        true_icon = PhotoImage(file="images/true.png")
        false_icon = PhotoImage(file="images/false.png")

        #Buttons
        self.true_button = Button(image=true_icon , command= self.button_event , bg=THEME_COLOR )
        self.false_button = Button(image=false_icon , command= self.button_event  , bg=THEME_COLOR )
        
        self.true_button.grid(row=2 , column=1 , pady=50)
        self.false_button.grid(row=2 , column=0 , pady=50 )

        #Score
        self.score_text = Label(text=f"Score: {self.quiz.score} ")
        self.score_text.grid(row=0 , column=1 ,padx=20 , pady=20)
        self.score_text.config(bg=THEME_COLOR ,fg=SCORE_TEXT_COLOR,  font="Helvetica 16 bold italic")
        

        self.question = self.canvas.create_text(150 , 125 , width=280 , text=self.quiz.next_question() , font="Helvetica 16 bold italic")


        self.window.mainloop()

    #Get next question
    def show_question(self):
        self.change_button_state()
        self.window.after(3000,self.canvas.config(bg="white"))
        self.canvas.itemconfig(self.question , text=self.quiz.next_question())
    
    #Call button actions
    def button_event(self):

        if self.quiz.still_has_questions():

            if self.quiz.check_answer("False"):
                self.canvas.config(bg="green")
            else:
                self.canvas.config(bg="red")
            
            

            self.score_text.config(text=f"Score: {self.quiz.score} ")
            self.change_button_state()
            self.window.after(1000,self.show_question)
      
        else:
            self.terminate_screen()

   
    #Terminate Program
    def terminate_screen(self):
        print("You've completed the quiz")
        print(f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
        self.window.destroy()

    

    def change_button_state(self):
        #print(self.true_button['state'])
        if self.true_button['state'] == 'normal':
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")

        else:
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")

        
        

        







        
        
        


