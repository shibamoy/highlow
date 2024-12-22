import random
import art
import game_data
data = game_data.data

def starting():
    print(art.logo)
    print("Welcome to High/Low, see what you can score in this!")

starting()

def gameTime():
    choice_a = random.choice(data)
    choice_b =  random.choice(data)
    score = 0
    while True:
        a = "A: " + choice_a['name'] + ", a " + choice_a['description'] + " ,from " +choice_a['country']
        b = "B: " + choice_b['name'] + ", a " + choice_b['description'] + " ,from " + choice_b['country']
        print(a)
        print(art.vs)
        print(b)
        guess = input("Which one has the most followers? Type A or B").lower()

        if guess == "a":
            if choice_a['follower_count'] > choice_b['follower_count']:
                choice_b = random.choice(data)
                score += 1
                print(f"Score is: {score}")
            else:
                print("you guessed wrong dummy")
                break
        if guess == "b":
            if choice_b['follower_count'] > choice_a['follower_count']:
                choice_a = choice_b
                choice_b = random.choice(data)
                score += 1
                print(f"Score is: {score}")
            else:
                print("you guessed wrong dummy")
                break
    print("Game over")

gameTime()
