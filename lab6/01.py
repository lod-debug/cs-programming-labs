a = int(input())
b = int(input())
f = 1
if a<0 or b<0 or (a==0 and b==0):
    print("ошибка")
    f = 0
while f == 1:
    if a==0 or b==0:
        print(f'НОД: {max(a,b)}')
        f = 0
    if b>0: a = a%b
    if a>0: b = b%a


