from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"].lower()))

quiz = QuizBrain(question_bank)
quiz.ask_questions()

print("you've completed the quiz")
print(f"your final score is: {quiz.score}/{quiz.question_number}")