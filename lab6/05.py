n = int(input())
if 1<n<10:
    for row in range(n):
        for column in range(n):
            if row == column:
                print('0',end=" ")
            elif row>column:
                print(row-column,end=" ")
            elif column == n-1:
                print(column-row)
            else:
                print(column-row,end=" ")
            
else:
    print('Ошибка')