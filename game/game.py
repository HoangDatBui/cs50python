import random
def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
            else:
                continue
        except:
            continue

    guess_num = random.randint(1,level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess >= 0:
                if guess < guess_num:
                    print("Too small!")
                elif guess > guess_num:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        except:
            continue
main()
