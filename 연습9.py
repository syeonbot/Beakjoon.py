list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

sc = input()

while True:
    temp = sc
    for char in list:
        if char in temp:
            index = temp.index(char)
            c = len(char)
            temp = temp[:index] + '/' + temp[index + c:]
            break
    if temp != sc:
        sc = temp
    else:
        break
print(len(sc))
