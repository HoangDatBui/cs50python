import random


def main():
    total_points = 0
    test = []
    level = get_level()
    for _ in range(10):
        a, b = generate_integer(level)
        while True:
            answer = input(f"{a} + {b} = ")

            if answer.isdigit():
                if int(answer) == a + b:
                    total_points += 1
                    test.append(True)
                    break
                else:
                    test.append("EEE")
                    print(test[-1])
                    try:
                        if test[-1] == "EEE" and test[-2] == "EEE" and test[-3] == "EEE":
                            print(f"{a} + {b} = {a + b}")
                            test.append(True)
                            break
                    except IndexError:
                        continue
            else:
                test.append("EEE")
                print(test[-1])
                try:
                    if test[-1] == "EEE" and test[-2] == "EEE" and test[-3] == "EEE":
                        print(f"{a} + {b} = {a + b}")
                        test.append(True)
                        break
                except IndexError:
                    continue
                continue

    print(f"Score: {total_points}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                continue
        except:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
        return x, y
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
        return x, y
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
        return x, y
    else:
        get_level()


if __name__ == "__main__":
    main()




