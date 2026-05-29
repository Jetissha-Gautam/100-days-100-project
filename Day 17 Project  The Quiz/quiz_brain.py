class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0
    def next_question(self):
        answer=input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False): " )
        self.check_answer(self.question_list[self.question_number].answer,answer)
        self.question_number+=1
        print("")
    def still_has_questions(self):
        if self.question_number+1<=len(self.question_list):
            return True
        else:
            return False
    def check_answer(self,ans1 ,ans2):
        if ans1.lower()==ans2.lower():
            self.score+=1
            print("You got it right ! ")            
        else:
            print("You got it wrong ! ")
        print(f"The correct answer is {ans1}")
        print(f"Your current score {self.score}/{self.question_number+1}")