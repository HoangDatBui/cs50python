def main():
    item_list = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total_cost = 0
    while True:
        try:
            item = input("Item: ").title()
            if item in item_list:
                total_cost += item_list[item]
                print(f"Total: ${total_cost:.2f}")
            else:
                continue
        except EOFError:
            print()
            break
main()
