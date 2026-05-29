from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank=[Question(x["text"],x["answer"]) for x in question_data ]
quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("Thankyou for playing.")
print(f"Your final score is {quiz.score}/{len(question_bank)}!")