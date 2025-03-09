def main():
    amount_due_list = [50]
    print(f"Amount Due: {amount_due_list[-1]}")
    while True:
        insert_coin = int(input("Insert Coin: "))
        if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
            amount_due_list.append(amount_due_list[-1] - insert_coin)
            if amount_due_list[-1] > 0:
                print(f"Amount Due: {amount_due_list[-1]}")
            else:
                print(f"Change Owed: {abs(amount_due_list[-1])}")
                break
        else:
            print(f"Amount Due: {amount_due_list[-1]}")
            continue
main()

