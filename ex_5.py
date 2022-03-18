nota1=float(int("digite sua primeira nota"))
nota2=float(int("digite sua segunda nota"))
media=(nota1+nota2)/2
if media < 5 :
    print("reprovado !!!")
elif media >= 5 and media <= 6.9 :
    print("recuperação !!!")
elif media >= 7:
    print("aprovado !!!")    
else:
    print("error !!!")
