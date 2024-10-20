from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for i in range(0,len(question_data)):
    new_question=Question(question_data[i]['text'],question_data[i]['answer'])
    question_bank.append(new_question)
obj=QuizBrain(question_bank)
while obj.is_still_has_question():
      obj.next_question()
print(f"Yeah! You completed the Quiz.\nYour final score is: {obj.score}/{obj.question_number}")