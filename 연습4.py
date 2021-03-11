num = input("")

for e in range(int(num)):
    rpt, str = input("").split()
    list_str = str

    for index, value in enumerate(list_str):
        for j in range(int(rpt)):
            print(value, end = "")
    print("")