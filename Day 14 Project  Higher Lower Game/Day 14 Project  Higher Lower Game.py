from data import data 
import random
import os 
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
logo = r'''
██   ██ ██  ██████  ██   ██ ███████ ██████      
██   ██ ██ ██       ██   ██ ██      ██   ██     
███████ ██ ██   ███ ███████ █████   ██████      
██   ██ ██ ██    ██ ██   ██ ██      ██   ██     
██   ██ ██  ██████  ██   ██ ███████ ██   ██     
                                                
                                                
██       ██████  ██     ██ ███████ ██████       
██      ██    ██ ██     ██ ██      ██   ██      
██      ██    ██ ██  █  ██ █████   ██████       
██      ██    ██ ██ ███ ██ ██      ██   ██      
███████  ██████   ███ ███  ███████ ██   ██      
                                                
                                                '''
vs=r'''
__      ________ 
\ \    / / ___| 
 \ \  / /\___ \ 
  \ \/ /  ___) |
   \__/  |____/ '''
print(logo)
number1=random.randint(0,49)
correct=True
score=0
number2=0
while correct:
    number2=random.randint(0,49)
    while number1==number2:
        number2=random.randint(0,49)
    print("current_score ",score)

    print(f"Compare A : {data[number1]['name']}, a {data[number1]['description']} from {data[number1]['country']}")
    fol1=data[number1]['follower_count']
    print(vs)
    print(f"Against B : {data[number2]['name']}, a {data[number2]['description']} from {data[number2]['country']}")
    fol2=data[number2]['follower_count']
    ans = 'A' if data[number1]["follower_count"]>data[number2]["follower_count"] else 'B'
    guess = input("Who has more followers ? Type 'A' or 'B'")
    clear_screen()
    number1 = number2
    if guess==ans:
        score+=1
        correct = True
    else:
        print("Wrong Answer!")
        print("Your final score is ",score)
        print(f"A has {fol1} followers while B has {fol2} followers")
        correct = False
    