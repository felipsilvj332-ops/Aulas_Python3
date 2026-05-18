# Escreva um programa para aprovar o empréstimo bancario de uma casa;
# O programa deve perguntar o valor da casa, o valor do salario do comprador, e em quantos anos ele vai pagar;
# Calcule o valor da prestação mensal, sabendo que ela não pode ultrapassar 30% do salario do comprador;
# Se ultrapassar o emprestimo é negado

print("Emprestimos certamentecaros")
nome = input("Sejá Bem vindo a sua avaliação de crédito!\nPara começarmos qual seu nome?")
print(f"Muito prazer {nome}! precisamos de mais detalhes sobre você, então informe:")
salario = float(input("Salario liquido: R$"))
parcelas = int(input("Quantidade de parcelas mênsais pretendidas?: "))
valcasa = float(input(f"\nPara prosseguir informe: \nO valor da casa desejado: R$"))

taxajuros = 0.15
totalparcelas = parcelas
valor_juros = valcasa + (valcasa * taxajuros)
prestmensal = valor_juros / parcelas

print(f"o valor será de R${prestmensal}")

if prestmensal>salario:
    print("Seu emprestimo foi reprovado!")
else:
    print("Seu emprestimo foi aprovado")