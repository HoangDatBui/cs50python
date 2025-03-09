def convert(string):
    if ":)" or ":(" in string:
        print(string.replace(":)", "🙂").replace(":(", "🙁"))

def main():
    a = input()
    convert(a)

main()

