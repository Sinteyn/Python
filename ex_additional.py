def find_time(file):
    with open(file, 'r', encoding='utf-8') as file:

        condition = file.read().splitlines()
        time_pipes = []
        filling_time = 0

        start = input("Чтобы начать нажмите Enter")

        while start != "":
            start = input("Чтобы начать нажмите Enter")

        while True:
            pipe = input("Введите номер трубы: ")
            if pipe != "":
                time_pipes.append(float(condition[int(pipe)]))
            else:
                break
        for time in set(time_pipes):
            filling_time += 1 / time
        else:
            return str(1 / filling_time * 60)


def result_record(result):
    with open('time.txt', 'w', encoding='utf-8') as file:
        file.write(result)


result_record(find_time("pipes.txt"))
