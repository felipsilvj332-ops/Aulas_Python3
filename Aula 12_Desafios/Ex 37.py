# Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será a base de conversão:
# 1 - Binario // 2 - octal // 3 - hexadecimal
selecao = int(input("Oque deseja converter:\n1-Binario\n2-Octal\n3-Hexadecimal\n"))
valor = int(input("Valor a converter: "))
if selecao == 1:
    print(bin(valor)[:2])
elif selecao == 2:
    print(oct(valor)[:2])
elif selecao == 3:
    print(hex(valor)[:2])