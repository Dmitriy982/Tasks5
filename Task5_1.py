with open("text1", "w+", encoding="utf-8") as f:
    while True:
        x = input("Введите данные в файл: ")
        f.write(x)
        if x == "":
            break
        else:
            f.write("\n")
    f.seek(0)
    content = f.read()
    print(content)

