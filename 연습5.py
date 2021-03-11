from collections import Counter

str = input("")
list_str = str
max = 0
list_up = list_str.upper()
counter = Counter(list_up)

for index, values in counter.items():
    if(max <= values -1) :
       max = values
       idx = index
    elif (max == values):
        idx = '?'
print(idx)   

