a, b= input("").split()

rslt_a = int(str(a)[::-1])
rslt_b = int(str(b)[::-1])

if(rslt_a >= rslt_b):
    print(rslt_a)
else:
    print(rslt_b)



