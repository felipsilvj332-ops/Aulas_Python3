import datetime as dt
print("Teste calendario - 2026")
#padrão americano (year, week, day):
data = dt.date.fromisoformat('2020-06-03')
data2 = dt.date.fromisoformat('20190104')
data3 = dt.date.fromisoformat('2020-W06-5')
print(data)
print(data2)
print(data3)
#Padrão 2
datat = input("Digite dia e mês: ")
data_string = (datat)
datareal = when = dt.date.strptime(f"{data_string}/2025", "%m/%d/%Y") # Avoids leap year bug.
datacorrida = when.strftime("%B %d")
print(datareal)
print(datacorrida)