V_casa=float(input("insira o valor da casa...:"))
salario=float(input("informe seu salário...:"))
ano=int(input("por quantos anos voçê deseja pagar...:"))

parcela= V_casa/(ano*12)
print(parcela)
print(salario*0.3)
if salario*0.3 > parcela:
    print("emprestimo autorizado !!!")
else:
    print("emprestimo negado !!!")
    