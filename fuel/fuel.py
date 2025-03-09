def main():
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = fraction.split("/")
            numerator = int(numerator)
            denominator = int(denominator)
            fuel = int(numerator) / int(denominator)
            if numerator <= denominator:
                if int(fuel * 100) <= 1:
                    print("E")
                elif int(fuel * 100) >= 99:
                    print("F")
                else:
                    print(f"{round(fuel * 100)}%")
                break
            elif numerator > denominator:
                continue
        except (ValueError, ZeroDivisionError):
            continue

main()

