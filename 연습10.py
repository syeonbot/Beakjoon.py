num = input()
cnt = 0
len = str

for i in range(int(num)): #num 받은 횟수만큼 반복
    len = input()
    list_len = list(len)
    flag = True
    temp = []
    for char in list_len: #받은 단어의 수만큼 반복
        if char not in temp: #만약 temp 안에 char이 없으면
            temp.append(char) #새로운 문자가 나오면 저장
        else:
            if char != temp[-1]: #여태껏 받은 temp값의 마지막에 존재하지 않다면
                flag = False #깃발은 틀림
                break
    if flag == True:
        cnt += 1

print(cnt)