# Escreva um programa para aprovar o empréstimo bancario de uma casa;
# O programa deve perguntar o valor da casa, o valor do salario do comprador, e em quantos anos ele vai pagar;
# Calcule o valor da prestação mensal, sabendo que ela não pode ultrapassar 30% do salario do comprador;
# Se ultrapassar o emprestimo é negado

print("Emprestimos certamentecaros")
nome = input("Sejá Bem vindo a sua avaliação de crédito!\nPara começarmos qual seu nome? ")
print(f"Muito prazer {nome}! precisamos de mais detalhes sobre você, então informe:")
salario = float(input("Salario liquido: R$"))
parcelas = int(input("Quantidade de parcelas mênsais pretendidas?: "))
valcasa = float(input(f"\nPara prosseguir informe: \nO valor da casa desejado: R$"))

valano = parcelas / 12
taxajuros = 0.015
limite = salario * 0.30
totalparcelas = parcelas
valor_cjuros = valcasa + (valcasa * taxajuros)
prestmensal = valor_cjuros / parcelas
#print(f"O limite é R${limite:.2f}\n")
#print(f"Parcelas de R${prestmensal:.2f}\n")
#print(f"o valor será de R${prestmensal:.2f}\n")

if prestmensal>limite:
    print("Seu emprestimo foi reprovado!")
else:
    print("Seu emprestimo foi aprovado, parabens!\n")
    print("RESUMO DO ACORDO: ")
    print(f"Valor solicitado: R${valcasa}\n")
    print(f"Anos a pagar: {valano} anos.\n")
    print(f"Parcelas mensais de R${prestmensal:.2f}")
    print("Custo total: ", prestmensal * parcelas)