def main():
    output = []
    vowel = 'AEIOUaeiou'
    string = input("Input: ")
    for char in string:
        if char in vowel:
            continue
        else:
            output.append(char)
    print(f"Output: {''.join(output)}")
main()
