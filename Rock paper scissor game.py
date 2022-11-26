import random
def game():
    print("Enter rock, paper or scissor")
    while True:
        user=input("Enter your choice")
        possible=["rock", "paper", "scissor"]
        comp_action=random.choice(possible)
        if user==comp_action:
            print("You both selected{user}. it's a tie!!")
        elif user == "rock":
            if comp_action == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user =="paper":
            if comp_action== "rock":
                 print("Paper covers rock! You win!")
            else:
                 print("Scissors cuts paper! You lose.")
        elif user == "scissor":
            if comp_action =="paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
game()