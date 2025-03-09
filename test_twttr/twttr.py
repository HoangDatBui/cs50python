def main():
    string = input("Input: ")
    output = shorten(string)
    print("Output:", output)

def shorten(s):
    output = []
    vowel = 'AEIOUaeiou'
    for char in s:
        if char in vowel:
            continue
        else:
            output.append(char)
    converted_string = ''.join(output)
    return converted_string

if __name__ == "__main__":
    main()
