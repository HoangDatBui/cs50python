def main():
    fraction = input("Fraction: ")
    output = gauge(convert(fraction))
    print(output)
def convert(fraction):
    while True:
        try:
            numerator, denominator = fraction.split("/")
            numerator = int(numerator)
            denominator = int(denominator)
            fuel = round(numerator / denominator * 100)
            if fuel > 100:
                raise ValueError
            else:
                return fuel
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percent):
    if percent <= 1:
        return "E"
    elif 100 >= percent >= 99:
        return "F"
    else:
        return f"{percent}%"

if __name__ == "__main__":
    main()

