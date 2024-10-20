class QuizBrain:
      def __init__(self,questionlist):
          self.question_number=0
          self.qlist=questionlist
          self.score=0
      def is_still_has_question(self,):
          if len(self.qlist) > self.question_number :
              return True
          else:
              return False
      def check_answer(self,user_answer,current_question):
          if user_answer.lower() == current_question.answer.lower():
              self.score+=1
              print("You got it right!")
          else:
              print("You got it wrong!")
          print(f"The correct answer was: {current_question.answer}")
          print(f"Your current Score is : {self.score}/{self.question_number}")
          print("\n")
      def next_question(self):
          current_question=self.qlist[self.question_number]
          self.question_number+=1
          user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
          self.check_answer(user_answer,current_question)