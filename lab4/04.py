x = int(input())
y = int(input())
z = int(input())
if (x>0 and y>0 and z>0) and((x+y>z and x+z>y and y+z>x)):
    if x==y and y==z:
        print('равносторонный')
    elif x==y or y==z or z==x:
        print('Равнобедренный') 
    else:
        print('разносторонний')
else:
    print('треугольник не существует')