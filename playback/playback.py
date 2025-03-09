string = input()
empty_list = []
for char in string:
    if char.isspace():
        empty_list.append("...")
    else:
        empty_list.append(char)
complete_string = ''.join(empty_list)
print(complete_string)
