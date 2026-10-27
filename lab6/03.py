n = int(input())
first = 1
if n<2:
    print("Ошибка")
else:
    while n>2:
        for i in range(2,n+1):
            while n%i==0:
                n = n//i
                if first:
                    print (i,end = "")
                    first = 0
                else:
                    print("", i,end="")


