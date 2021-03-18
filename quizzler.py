import html
from api_data import question_data
from question_model import Question
class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.question_list = self.fill_question_bank()
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
       
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        #Get rid of html characters
        q_text = html.unescape(self.current_question.text)
        return q_text
       

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True

        else:
            return False
           

    def fill_question_bank(self):
        question_bank = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)

        return question_bank
        
