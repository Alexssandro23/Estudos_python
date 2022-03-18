n=int(input("digite um numero inteiro...:"))
opcao=int(input('''
escolha a base de converção:
1-binário
2-octal
3-hexadecimal
opcão..:'''))
if opcao==1:
    print("número convertido em binário..:{}".format(bin(n)[2:]))
elif opcao==2:    
    print("número convertido em octal..:{}".format(oct(n)[2:]))
elif opcao==3:
    print("número convertido em hexadecimal..:{}".format(hex(n)[2:]))
else:
    print("insira uma opcao válida !!!")    