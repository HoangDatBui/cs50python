def main():
    greeting = input("Greeting: ").strip().capitalize()
    output = value(greeting)
    print(f"${output}")

def value(greeting):
    price = 0
    if "Hello" in greeting:
        price = 0
    elif greeting.startswith("H") and "Hello" not in greeting:
        price = 20
    else:
        price = 100
    return price

if __name__ == "__main__":
    main()
