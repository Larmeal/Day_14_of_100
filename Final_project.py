# สร้างเกม ทายว่าใครมีผู้ติดตามใน ig มากกว่ากัน

import random
from art import logo, vs
from game_data import data

number = []
for i in range(1, 51):
    number.append(i)

random_number_question_1 = random.choice(number)
number.pop(random_number_question_1 - 1)
random_number_question_2 = random.choice(number)

question_1 = [data[random_number_question_1]["name"], data[random_number_question_1]["description"], data[random_number_question_1]["country"]]
score_1 = data[random_number_question_1]["follower_count"]
A = score_1

question_2 = [data[random_number_question_2]["name"], data[random_number_question_2]["description"], data[random_number_question_2]["country"]]
score_2 = data[random_number_question_2]["follower_count"]
B = score_2

point = 0
again = True

print(logo)

while again:
    show_question_1 = print(f"\nCompare a: {question_1[0]}, a {question_1[1]}, from {question_1[2]}")
    print(vs)
    show_question_2 = print(f"\nCompare b: {question_2[0]}, a {question_2[1]}, from {question_2[2]}")
    ask = input("Who has more follows? Type 'A' or 'B': ").lower()
    # correct a
    if ask == "a" and A > B: 
        point += 1 
        right = print(f"You're right! Current score: {point}")
        random_number_question_1 = random_number_question_2
        number.pop(random_number_question_2 - 1)
        random_number_question_2 = random.choice(number)
        question_1 = [data[random_number_question_1]["name"], data[random_number_question_1]["description"], data[random_number_question_1]["country"]]
        score_1 = data[random_number_question_1]["follower_count"]
        A = score_1

        question_2 = [data[random_number_question_2]["name"], data[random_number_question_2]["description"], data[random_number_question_2]["country"]]
        score_2 = data[random_number_question_2]["follower_count"]
        B = score_2
    # wrong a
    elif ask == "a" and A < B:
        wrong = print(f"Sorry, that's wrong. Final score: {point}")
        again = False
    # correct b
    elif ask == "b" and B > A:
        point += 1 
        right = print(f"You're right! Current score: {point}")
        random_number_question_1 = random_number_question_2
        number.pop(random_number_question_2 - 1)
        random_number_question_2 = random.choice(number)
        question_1 = [data[random_number_question_1]["name"], data[random_number_question_1]["description"], data[random_number_question_1]["country"]]
        score_1 = data[random_number_question_1]["follower_count"]
        A = score_1

        question_2 = [data[random_number_question_2]["name"], data[random_number_question_2]["description"], data[random_number_question_2]["country"]]
        score_2 = data[random_number_question_2]["follower_count"]
        B = score_2

    # wrong b
    elif ask == "b" and B < A:
        wrong = print(f"Sorry, that's wrong. Final score: {point}")
        again = False
    

# # My teacher version
# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong.""" 
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"


# def game():
#   print(logo)
#   score = 0
#   game_should_continue = True
#   account_a = get_random_account()
#   account_b = get_random_account()

#   while game_should_continue:
#     account_a = account_b
#     account_b = get_random_account()

#     while account_a == account_b:
#       account_b = get_random_account()

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
    
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     clear()
#     print(logo)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")

# game()
    



    

    
    

