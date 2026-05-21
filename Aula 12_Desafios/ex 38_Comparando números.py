# O programa deve ler dois números inteiros e comparar, exibindo na tela:
# O primeiro valor é maior // O segundo valor é maior // Os valores são iguais

valor = int(input("insira um valor: "))
valordois = int(input("insira um valor: "))

if valor > valordois:
    print("O primeiro valor é maior!")
elif valor < valordois:
    print("O segundo valor é maior!")
elif valor == valordois:
    print("Os valores são iguais!")