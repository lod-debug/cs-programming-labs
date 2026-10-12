pokupki = 0
stoimost = 0
srStoimost = 0
while True:
    n = input()
    if n =='stop':
        break
    pokupki +=1
    stoimost +=int(n)
print(f'покупок: {pokupki}')
print(f'Общая стоимость: {stoimost}')
print(f'Средняя стоимость: {(stoimost/pokupki):.02f}')
