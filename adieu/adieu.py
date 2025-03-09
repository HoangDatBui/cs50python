import inflect
def main():
    p = inflect.engine()
    name_list = []
    try:
        while True:
            name = input("Name: ")
            name_list.append(name)
            mylist = p.join(name_list)
    except EOFError:
        print(f"Adieu, adieu, to {mylist}")

main()
