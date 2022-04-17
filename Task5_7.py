import json


def create():
    with open(r"c:\text_7.txt", "r", encoding="utf-8") as f, open("text.json", "w", encoding="utf-8") as w:
        dict1 = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        dict2 = [dict1, {"average_profit": sum([int(i) for i in dict1.values() if int(i) > 0]) / len(
            [int(i) for i in dict1.values() if int(i) > 0])}]
        json.dump(dict2, w, ensure_ascii=False)


create()
