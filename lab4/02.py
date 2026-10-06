price = float(input())
age = int(input())
if price>0 and (0 <= age <= 120):
    if (0<=age<=5):
        print(f'стоимость: {(0):.2f} руб')
    elif (6<=age<=17):
        print(f'стоимость: {(price*0.5):.2f} руб')
    elif (18<=age<=59):
        print(f'стоимость: {price:.2f} руб')
    elif (60<=age<=120):
        print(f'стоимость: {price*0.7:.2f} руб')        
else:
    print("ошибка")