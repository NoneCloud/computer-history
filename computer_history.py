import math

century = [
    (1945, "没有计算机"),
    (1957, "电子管计算机"),
    (1964, "晶体管计算机"),
    (1970, "集成电路计算机"),
    (1980, "大规模集成电路计算机"),
    (math.inf, "超大规模集成电路与智能计算机"),

]

while True:
    while True:
        year = input("Please input the year:  ")
        if year.lower() == "end":
            raise SystemExit
        try:
            year = int(year)
            break
        except ValueError:
            print("\033[31m[Please input a number]\033[0m")

    for i in century:
        if year <= i[0]:
            print(i[1])
            break