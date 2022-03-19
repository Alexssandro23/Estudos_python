# inputs
  #forma de pagamento
  #preço
 

opcao=int(input('''
forma de pagamento:
1 - á vista (dinhero/cheque).
2 - á vista  (cartão).
3 - parcelado em até 2x (cartão).
4 - parcelado em até 3x ou mais (cartão)  
informe o método de pagamento..:'''))

valor=float(input("informe o valor do produto...:"))

if opcao==1:
    desconto=valor-(valor*0.1)
    print("valor original: R${:.2f}".format(valor))
    print("valor com desconto: R${:.2f}".format(desconto))
elif opcao==2:
    desconto=valor-(valor*0.05)
    print("valor original: R${:.2f}".format(valor))
    print("valor com desconto: R${:.2f}".format(desconto))
elif opcao==3:
    print("valor original: R${:.2f}".format(valor))
elif opcao==4:
    juros=valor+(valor*0.2)
    print("valor original: R${:.2f}".format(valor))
    print("valor com juros: R${:.2f}".format(juros))
else:
    print("informe uma opção válida (1,2,3 ou 4) !!!")        
