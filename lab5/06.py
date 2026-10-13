n = int(input())   #5
odd_count = 0

for i in range(n):
    val = 1
    for j in range(i+1):
        if val %2 !=0:
            odd_count +=1
        if j<i:
            print(val,end=' ')
        else:
            print(str(val))
        val = val*(i-j)//(j+1)
print(f'нечетных чисел {odd_count}')
    