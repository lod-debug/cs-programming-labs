f = 1
number = int(input())
for i in range(2,(int(number**0.5))+1):
    if number % i ==0:
        print('Не простое')
        f = 0
        break
if f ==1:
    print("простое")

