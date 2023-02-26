def longest_words(file):
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().split()
        count = 0

        for ind in range(len(text)):
            if len(text[ind]) > count:
                count = len(text[ind])
        for i in text:
            if len(i) == count:
                print(i, end=" ")


longest_words("article.txt")
