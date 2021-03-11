str = input("")
list_str = str


for i in range(97, 122):
    for index, value in enumerate(list_str):
        rslt = -1
        if chr(i) == value:
            rslt = index
            break
    print(rslt, end = ' ')   
     
     
           