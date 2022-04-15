from re import T
from question_model import Question
from question_data import question_data
from quiz_brain import QuizBrain


# Creates a question bank
question_bank = []
for _ in question_data:
    # Alternative for Open Trivia imported questions:
    # new_question = Question(_['question'], _['answer'])
    new_question = Question(_['text'], _['answer'])
    question_bank.append(new_question)


# Stars the quiz
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


# Final messages
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
