def enter_lines():
    number_of_lines = input("Введите кол-во строк: ")
    while not number_of_lines.isdigit():
        number_of_lines = input("Неккоректный ввод. Введите кол-во строк: ")
    return int(number_of_lines)


def read_last(lines, file):
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        amount_lines = len(text)
        start = amount_lines - lines
        for i in text[start:]:
            print(i)


article_file = "article.txt"
last_lines = enter_lines()
read_last(last_lines, article_file)
