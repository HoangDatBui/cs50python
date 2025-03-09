def main():
    camel_case = input("camelCase: ")
    converted(camel_case)

snake_case_list = []
def converted(snake_case):
    for word in snake_case:
        if word.isupper():
            snake_case_list.append("_")
            snake_case_list.append(word.lower())
        else:
            snake_case_list.append(word)
    snake_case_str = "".join(snake_case_list)
    return print(f'snake_case: {snake_case_str}')

main()
