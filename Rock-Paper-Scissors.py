from time import *
import random

def get_computer_choice():
    choices = ["rock", "scissors", "paper"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():

    privet = input("Welcome, this is a game called 'Rock-scissors-paper'.\nDo you want to play with me?(Yes or No):")
    privet = privet.lower()

    if privet == "yes":

        print("Great! Let's start the game.")
    else:
        print("Okay, maybe next time. Goodbye!")
        time.sleep(2)
        exit()
    
    player_score = 0
    computer_score = 0
    
    print("First who score 3 points wins the game. Let's begin!\n")

    while player_score < 3 and computer_score < 3:
        user_choice = input("Please enter your choice (rock, scissors, paper): ").lower()
        
        if user_choice not in ["rock", "scissors", "paper"]:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        print(f"Score - You: {player_score}, Computer: {computer_score}\n")
    if player_score == 3:
        print("Congratulations! You won the game!")
    else:
        print("Computer won the game! Better luck next time!")
main()