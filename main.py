import random
from art import logo,vs
from game_data import data

def format_data(account):
    account_name = account["name"]
    account_descript = account["description"]
    account_from = account["country"]
    return f"{account_name}, a {account_descript}, from {account_from}"

def check_answer(guess,answer_a, answer_b):
    if answer_a > answer_b:
        return guess == "a"
    else:
        return guess == "b"

def higher_lower():
    game = True
    while game:
        print(logo)
        current_score = 0
        game_is_over = False
        random_a = random.choice(data)
        random_b = random.choice(data)

        while random_a == random_b:
            random_b = random.choice(data)
        while not game_is_over:
            print(f"Compare A: {format_data(random_a)}")
            print(vs)
            print(f"against B: {format_data(random_b)}")
            user_choice = input("Who has more followers Type 'a' or 'b'?: ").lower()
            is_right = check_answer(user_choice, random_a["follower_count"], random_b["follower_count"])

            if is_right:
                if user_choice == "a":
                    random_b = random.choice(data)
                else:
                    random_a = random_b
                    random_b = random.choice(data)
                current_score += 1
                print(f"You're right! Current score: {current_score}")
            else:
                print(f"Sorry, that's wrong. Final score: {current_score}")
                game_is_over = True

        again = input("Do You want play again. Type 'y' or 'n' ").lower()
        if again == "y":
            game = True
        else:
            game = False

higher_lower()