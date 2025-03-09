from pyfiglet import Figlet
import random
import sys

def main():
    figlet = Figlet()
    if len(sys.argv) == 1:
        font_list = figlet.getFonts()
        figlet.setFont(font = random.choice(font_list))
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in figlet.getFonts():
                figlet.setFont(font = sys.argv[2])
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    a = input("Input: ")
    print(figlet.renderText(a))

main()

