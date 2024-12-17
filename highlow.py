import random
#randomnumber is here
random_num = random.randint(1, 100)
print(random_num)

#introduce to the game and select mode

print("Welcome to my number guessing game\n"
      "The goal is to guess the number!\n"
      "I am thinking of a number 1 - 100")

game_mode = input("Choose difficulty: Type easy or hard").lower()
def game_difficutly(game_mode):
    if game_mode == "hard":
        return 10
    else:
        return 5

#check if the guess is right, hard mode for 10 and easy for 5
def checkGuess(random_num, rounds):

    for _ in range(rounds):
        print(f"You have {rounds} chances.")
        user_input_guess = input("Make a guess:")
        user_guess = int(user_input_guess)
        rounds -= 1
        if random_num != user_guess:
            if user_guess > random_num:
                print("Too high")
            elif user_guess < random_num:
                print("Too Cold")
        else:
            print("You guessed it right")
            return
    print(f"The number is: {random_num}")

game_difficutly(game_mode)
rounds = game_difficutly(game_mode)
checkGuess(random_num, rounds)






