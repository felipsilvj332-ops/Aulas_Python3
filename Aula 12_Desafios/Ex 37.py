# Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será a base de conversão:
# 1 - Binario // 2 - octal // 3 - hexadecimal

num = int(input("Digite um número inteiro: "))
print('''Escolha uma das opções a baixo:
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL      
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print("{} convertido para binario é igual a: {}".format(num, bin(num)[2:]))
elif opção == 2:
    print("{} convertido para Octal é igual a: {}".format(num, oct(num)[2:]))
elif opção == 3:
    print("{} Convertido para hexadecimal é igual a: {}".format(num, hex(num)[:2]))
    print(f"{num} Convertido para hexadecimal é igual a:{hex(num)[2:]}")