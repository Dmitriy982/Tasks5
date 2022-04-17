def read():
    my_dict = {}
    with open(r"C:\text_3.txt", "r", encoding="utf-8") as r:
        for line in r:
            my_dict[line.split()[0]] = float(line.split()[1])
    print("Сотрудники с зп меньше 20000")
    for i, j in my_dict.items():
        if j < 20000:
            print(i)
    print("Средняя зарплата = ", sum(my_dict.values()) / len(my_dict))


read()
