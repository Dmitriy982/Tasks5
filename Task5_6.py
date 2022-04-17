def create():
    my_dict = {}
    with open(r"c:\text_6.txt", "r", encoding="utf-8") as f:
        for line in f:
            name, j = line.split(':')
            sum1 = sum(map(int, "".join([i for i in j if i in '1234567890 ']).split()))
            my_dict[name] = sum1
    print(my_dict)


create()
