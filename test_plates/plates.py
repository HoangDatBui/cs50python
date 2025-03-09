def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len_string(s) == True and characters(s) == True:
        if two_first_character(s) == True and number(s) == True and middle(s) == True:
            return True
        else:
            return False
    else:
        return False

def two_first_character(string):
    if string[0].isalpha() and string[1].isalpha():
        return True
    else:
        return False

def len_string(string):
    if 2 <= len(string) <= 6:
        return True
    else:
        return False

def number(string):
    output = []
    for char in string:
        if char.isdigit() == True:
            output.append(int(char))
    if output:
        if output[0] == 0:
            return False
        elif output[0] != 0:
            return True
    else:
        return True

def characters(string):
    if string.isalnum():
        return True
    else:
        return False

def middle(string):
    if string.isalpha():
        return True
    else:
        for char in string:
            if char.isdigit():
                position = string.index(char)
                if string[position:].isdigit():
                    return True
                else:
                    return False

if __name__ == "__main__":
    main()

