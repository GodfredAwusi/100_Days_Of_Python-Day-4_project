import random
# Write a program for rock paper scissors game based the rules:
# rock wins against scissors
# scissors wins against paper
# paper wins against rock
# When the user makes a choice, the computer should also randomly make a choice

rock = """               _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \\ / __| |/ /
| | | (_) | (__|   < 
|_|  \\___/ \\___|_|\\_\\ """

paper = """  _ __   __ _ _ __   ___ _ __ 
| '_ \\ / _` | '_ \\ / _ \\ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \\__,_| .__/ \\___|_|   
| |         | |              
|_|         |_|               """

scissors = """"           _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \\| '__/ __|
\\__ \\ (__| \\__ \\__ \\ (_) | |  \\__ \\
|___/\\___|_|___/___/\\___/|_|  |___/
                                    """

images = [rock, paper, scissors]
print("\n")
print("Welcome to the Rock Paper Scissors game!")
user_choice = int(input("What is your choice? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(images[user_choice])
computer_choice = random.randint(0, 2)
print(f"\nComputer chose\n{images[computer_choice]}")

if user_choice == 0 :
    if computer_choice == 2:
        print("\nYou Win")
    elif computer_choice == 1:
        print("\nYou Lose")
    else:
        print("\nIt'aa draw")
elif user_choice == 1:
    if computer_choice == 0:
        print("\nYou Win")
    elif computer_choice == 2:
        print("\nYou Lose")
    else:
        print("\nIt'aa draw")
elif user_choice == 2:
    if computer_choice == 0:
        print("\nYou Lose")
    elif computer_choice == 1:
        print("\nYou Win")
    else:
        print("\nIt'aa draw")
else:
    print("You chose an invalid number, you lose")





