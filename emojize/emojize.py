import emoji

def main():
    emo = input("Input: ")
    output = emoji.emojize(emo, language='alias')
    print(f"Output: {output}")

main()
