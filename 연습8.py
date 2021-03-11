s = input()

dial = ['1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ','0']

sum=0

for i in s:
    time=2
    for j in range(len(dial)):
        for k in dial[j]:
            if i==k: break
        if i==k: break
        time+=1
    sum += time

print(sum)