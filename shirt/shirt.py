import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command()
    try:
        imageFile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirtFile = Image.open("shirt.png")

    size = shirtFile.size

    muppet = ImageOps.fit(imageFile, size)

    muppet.paste(shirtFile, shirtFile)

    muppet.save(sys.argv[2])
    
def check_command():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if check_extension(file1[1]) == False:
        sys.exit("Invalid input")
    if check_extension(file2[1]) == False:
        sys.exit("Invalid output")
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have difference extensions")

def check_extension(file):
    if file in [".jpg", ".jepg", ".png"]:
        return True
    return False

if __name__ == '__main__':
    main()
