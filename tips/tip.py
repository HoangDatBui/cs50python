def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dola = [float(d.replace('$', ''))]
    return dola[0]
def percent_to_float(p):
    percen = [int(p.replace('%', ''))]
    return percen[0] / 100

main()
