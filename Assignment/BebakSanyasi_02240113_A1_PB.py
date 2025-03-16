import random
def guess_game():
    print("Guess Number Game")
    correct_num = 5
    num = int(input("Enter the number from 1 to 10: "))
    
    if num == correct_num:
        print("Hurray, your guess is right, wanna play another game?")
        print("Your luck did favour, try your luck in another game.")
    else:
        print("your gess is wrong,sorry.")
        print("Don't worry,try another game!")

def second_game():
    print("Rock Paper Scissors Game")
    options = ["rock", "paper", "scissors"]
    Player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    ai_choice = random.choice(options)
    print(f"Computer's choice: {ai_choice}")
    if Player_choice == ai_choice:
        print("It's a draw!")
    elif (Player_choice == "rock" and ai_choice == "scissors")or \
     (Player_choice == "scissors" and ai_choice == "paper")or \
     (Player_choice == "paper" and ai_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")
def main():
    while True:
        game_choosing = input("Which game would you like to play? (1) Guess Number or (2) Rock Paper Scissors (Enter 1 or 2, or 'quit' to exit): ").lower()
        
        if game_choosing == "1":
            guess_game()
        elif game_choosing == "2":
            second_game()
        elif game_choosing == "leave":
            print("Thank you for playing! bye.")
            break
        else:
            print("Invalid choice. Please enter 1 for Guess game and 2 for second game, or type 'leave' to exit.")

main()