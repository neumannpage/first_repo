print("===============================")
print("Rock, Paper, Scissors, Lizard, Spock")
print('===============================')
print("Welcome to the game!")
u=1
pw=0
cw=0
while u==1:
 print('(1) Rock')
 print('(2) Paper')
 print('(3) Scissors')
 print('(4) Lizard')
 print('(5) Spock')
 p=int(input("Enter your choice (1-5): "))

 import random
 choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
 c=random.choice(choices)
 if p==1:
     player_choice = 'Rock'
 elif p==2:
     player_choice = 'Paper'
 elif p==3:  
     player_choice = 'Scissors'
 elif p==4:
     player_choice = 'Lizard'
 elif p==5:
     player_choice = 'Spock'
 print(f"You chose: {player_choice}")
 print(f"Computer chose: {c}")       

 
 if p==1:
     if c=='Rock':
         print("It's a tie!")
     elif c=='Paper':
         print("Computer wins!")
         cw+=1
     elif c=='Scissors':
         print("You win!")
         pw+=1
     elif c=='Lizard':
         print("You win!")
         pw+=1
     elif c=='Spock':
         print("Computer wins!")
         cw+=1
 elif p==2:
     if c=='Rock':
         print("You win!")
         pw+=1
     elif c=='Paper':
         print("It's a tie!")
     elif c=='Scissors':
         print("Computer wins!")
         cw+=1
     elif c=='Lizard':
         print("Computer wins!")
         cw+=1
     elif c=='Spock':
         print("You win!")
         pw+=1
 elif p==3:  
     if c=='Rock':
         print("Computer wins!")
         cw+=1
     elif c=='Paper':
         print("You win!")
         pw+=1
     elif c=='Scissors':
         print("It's a tie!")
     elif c=='Lizard':
         print("You win!")
         pw+=1
     elif c=='Spock':
         print("Computer wins!")
         cw+=1
 elif p==4:
     if c=='Rock':
         print("Computer wins!")
         cw+=1
     elif c=='Paper':
         print("You win!")
         pw+=1
     elif c=='Scissors':
         print("Computer wins!")
         cw+=1
     elif c=='Lizard':
         print("It's a tie!")
     elif c=='Spock':
         print("You win!")
         pw+=1
 elif p==5:
     if c=='Rock':
         print("You win!")
         pw+=1
     elif c=='Paper':
         print("Computer wins!")
         cw+=1
     elif c=='Scissors':
         print("You win!")
         pw+=1
     elif c=='Lizard':
         print("Computer wins!")
         cw+=1
     elif c=='Spock':
         print("It's a tie!")
 print(f"Score: You {pw} - Computer {cw}")
 n=input("Do you want to play again? (y/n): ")
 if n=='y':
     u=1
 else:
     u=0
     print("Thanks for playing!")