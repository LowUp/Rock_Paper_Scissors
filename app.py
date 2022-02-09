from rules import Rules
import random

user_choice = Rules()
computer_choice = Rules()


def match(user, computer):
    if user == "Rock" and computer == "Rock": return "tie"
    elif user == "Scissor" and computer == "Scissor": return "tie"
    elif user == "Paper" and computer == "Paper": return "tie"
    elif user == "Rock" and computer == "Paper": return "computer wins this round"
    elif user == "Paper" and computer == "Rock": return "user wins this round"
    elif user == "Paper" and computer == "Scissor": return "computer wins this round"
    elif user == "Scissor" and computer == "Paper": return "user wins this round"
    elif user == "Rock" and computer == "Scissor": return "user wins this round"
    elif user == "Scissor" and computer == "Rock": return "computer wins this round"
    else: return "failed !"


def game():
    print("First to 5 wins")

    counter1 = 0
    counter2 = 0

    while True:

        input_from_user = int(input("\nChoose:\n(1)Rock\n(2)Paper\n(3)Scissor\n- "))
        input_from_computer = random.randint(1, 3)

        result = match(user_choice.rules(input_from_user), computer_choice.rules(input_from_computer))
        if result == "computer wins this round":
            counter2 += 1
            print(result)
            print(f"\nUser's pick: {user_choice.rules(input_from_user)}, user's win count: {counter1}")
            print(f"Computer's pick: {computer_choice.rules(input_from_computer)}, computer's win count: {counter2}")
            if counter2 >= 5:
                print("Computer wins the game")
                break
        elif result == "user wins this round":
            counter1 += 1
            print(result)
            print(f"\nUser's pick: {user_choice.rules(input_from_user)}, user's win count: {counter1}")
            print(f"Computer's pick: {computer_choice.rules(input_from_computer)}, computer's win count: {counter2}")
            if counter1 >= 5:
                print("User wins the game")
                break
        else:
            print(result)


game()






