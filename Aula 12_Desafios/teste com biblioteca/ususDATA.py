# contagem de dias para um evento:

import time
import datetime as dt
today = dt.date.today() # mostra a data atual no padrão de sequencia americano
print(f"hoje: {today}")
today == dt.date.fromtimestamp(time.time())
my_birthday = dt.date(today.year, 6, 14) # identifica o ano atual e realiza a montagem da data 
if my_birthday < today: #verifica se o aniversario esta proximo do sia atual calculado
    my_birthday = my_birthday.replace(year=today.year + 1)
print(f"Meu aniversario: {my_birthday}")
time_to_birthday = abs(my_birthday - today) #calcula os dias até o aniversario
print(time_to_birthday.days)

