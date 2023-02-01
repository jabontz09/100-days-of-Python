class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        user_answer = input(f"Q. {self.question_number + 1}:  + {self.question_list[self.question_number].text} (True/False) \n").lower()

        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def ask_questions(self):
        while self.question_number != len(self.question_list):
            self.next_question()

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer: 
            print("you got it right!")
            self.score += 1
        else: print("that is wrong")

        print(f"the correct answer is {correct_answer}")
        print(f"your current score is {self.score}/{self.question_number +1}")
        print("\n")
