def main():
    gro_list = {}
    while True:
        try:
            item = input().upper()
            if item not in gro_list:
                gro_list[item] = 1
            else:
                gro_list[item] += 1

        except EOFError:
            for key, value in sorted(gro_list.items()):
                print(f"{value} {key}")
            break

main()
