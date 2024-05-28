#ROCK PAPER SCISSOR GAME USING PYTHON
#PICK A NUMBER FROM 1 TO 3
import random
rock=1
paper=2
scissor=3
user_choice=int(input("Enter your choice(1.Rock,2.Paper,3.Scissor):"))
computer_choice=random.randint(1,3)
if user_choice==rock and computer_choice==scissor:
 print("You Win! Rock Beats Scissor") 
elif user_choice==paper and computer_choice==rock:
 print("You Win! Paper Beats Rock")
elif user_choice==scissor and computer_choice==paper:
 print("You Win! Scissor Beats Paper")
elif user_choice==computer_choice:
 print("It's a tie!")
else:
 print("You Lose! Try again...")
 print()
 print("Computer went with",computer_choice)
