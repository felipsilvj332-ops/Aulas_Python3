#Verificar se o candidato se alista, ou não

from datetime import date, datetime
nome = input("Imforme o nome completo: ")
entrada = input("Imforme dua data de nascimento: (dd/mm/aaaa)")
nascimento = datetime.strptime(entrada, "%d/%m/%Y").date()
hoje = date.today()
idade = hoje.year - nascimento.year
if  (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
    idade -= 1
print(f"DADOS RELEVANTES:\nNome: {nome}")
print(f"Data de nascimento: {nascimento.strftime("%d/%m/%Y")}")
print(f"Idade: {idade} anos")

if idade < 18:
    falta = idade - 18
    print("O candidato ainda é muito jovem")
elif idade == 18:
    print("O candidato possui a idade requerida e devera se apresentar no quartel mais proximo!")
elif idade > 18:
    print("O candidato possui idade superior ao minimo exigido!")


