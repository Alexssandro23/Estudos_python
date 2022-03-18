from datetime import date
ano_d_nasc=int(input("informe seu ano de nascimento..:"))

data=date.today()
ano=data.strftime("%Y")
idade=int(ano)-ano_d_nasc
print(idade)
if idade <= 9:
    print("Mirin")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 20:
    print("Sênior")
else:
    print("Master")                