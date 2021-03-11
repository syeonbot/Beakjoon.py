input_s = input("")
cnt = 0

input_split= input_s.split(" ")

for i in range(len(input_split)):
    if(input_split[i] != ""):
        cnt = cnt + 1

print(cnt)