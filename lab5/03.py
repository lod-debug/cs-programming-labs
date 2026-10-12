n = int(input())
bolshe0 = 0
ravno0 = 0
menshe0= 0 
for i in range(n):
    i = float(input())
    if i<0:
        menshe0 +=1
    if i==0:
        ravno0 +=1
    if i >0:
        bolshe0 +=1
print(f'ниже нуля: {menshe0}')
print(f'равны нулю: {ravno0}')
print(f'выше нуля: {bolshe0}')

