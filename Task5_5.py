from random import randint


def create():
    with open("text1.txt", "w", encoding="utf-8") as f:
        lis = [randint(1, 20) for i in range(10)]
        f.write(" ".join(map(str, lis)))
        print(lis)
    print("Сумма чисел: ", sum(lis))


create()
