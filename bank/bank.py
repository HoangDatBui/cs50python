greeting = input("Greeting: ").strip().capitalize()
if "Hello" in greeting:
    print("$0")
elif greeting.startswith("H") and "Hello" not in greeting:
    print("$20")
else:
    print("$100")
