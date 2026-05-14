#Estrutura condicional aninhada

nome = str(input("Qual é seu nome? "))
print(f"Tenha um bom dia {nome}!")
if nome == "Asana":
    print("Que nome generico!")
elif nome == 'ana' or nome == 'julio' or nome == 'paulo':
    print("Que nome antigo!")
elif nome in 'Danilo gentili de arrobas':
    print("para, para, para, para!!!")
else:
    print("Mais um ano comum") 
print(f"Tenha uma boa noite {nome}!")