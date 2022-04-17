def read():
    my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    with open("text", "w", encoding="utf-8") as f:
        with open(r"C:\text_4.txt", "r", encoding="utf-8") as r:
            f.writelines([line.replace(line.split()[0], my_dict.get(line.split()[0])) for line in r])
    

read()