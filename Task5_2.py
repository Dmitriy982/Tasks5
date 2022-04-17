def create():
    with open("text1.txt", "w+", encoding="utf-8") as f:
        while True:
            x = input("Введите данные в файл: ")
            f.write(x)
            if x == "":
                break
            else:
                f.write("\n")


def read():
    with open("text1.txt", "r", encoding="utf-8") as r:
        x = r.read()
        y = len(x) - x.count("\n")
        print("Количество символов = ", y)
        print("Количество строк = ", x.count("\n"))


create()
read()
