from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"],question["answer"])) #datadaki soru cevap sözlük verisini Question clasına direk gönderip objeler oluşturduk
#print(question_bank[0].answer) test
quiz = QuizBrain(question_bank)

while quiz.still_has_questions:
    quiz.next_question()

print("u ve completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")