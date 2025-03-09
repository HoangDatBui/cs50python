def main():
    fruit = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cataloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Sweet Cherries": 100,
        "Kiwifruit": 90,
        "Pear": 100
    }

    item = input("Item: ").title()
    if item in fruit:
        print(f"Calories: {fruit[item]}")
    else:
        pass

main()
