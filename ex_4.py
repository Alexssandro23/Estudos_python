from datetime import date
data=date.today()
ano=data.strftime("%Y")
print(ano)

ano_nasc=int(input("em que ano voçê nasceu?"))
idade=int(ano)-ano_nasc
print(idade)
if idade < 18:
    ano_d_alist=idade-18
    print('você deve se apresentar para o alistamento em {} anos'.format(abs(ano_d_alist)))

elif idade > 18:
    ano_d_alist=idade-18
    print('voçê deveria ter se alistado há {} anos'.format(abs(ano_d_alist)))
else:
    print("chegou a hora de se apresentar ao serviço militar !!!")
