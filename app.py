from rules import Rules
import random

user_choice = Rules()
computer_choice = Rules()


def match(user, computer):
    if user == computer:
        return "\ntie"
    elif (user == "Rock" and computer == "Scissor") or (user == "Scissor" and computer == "Paper") or (user == "Paper" and computer == "Rock"):
        return "user wins this round"
    elif (computer == "Rock" and user == "Scissor") or (computer == "Scissor" and user == "Paper") or (computer == "Paper" and user == "Rock"):
        return "computer wins this round"
    else:
        return "\nWrong input !"


def game():
    print("First to 5 wins")

    counter1 = 0
    counter2 = 0

    while True:

        try:
            input_from_user = int(input("\nChoose:\n1 = Rock\n2 = Paper\n3 = Scissor\n- "))
        except ValueError:
            input_from_user = -1

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






