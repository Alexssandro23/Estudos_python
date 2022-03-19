#jonkepô
#regras: pedra>tesoura e pedra < papel
#        papel>pedra e papel < tesoura
#        tesoura>papel e tesoura < pedra 
from random import randint
resp="S"
while resp == "S":
    adversario=(randint(1,3))
    eu=int(input('''
    1-pedra
    2-papel
    3-tesoura
       escolha:'''))
      
#------------------------------------------------------------------------------------------    
    if eu==1:
        print("pedra !!!")
        if adversario==1:
            print("# pedra x pedra #")
            print("empate !!!")
        elif adversario==2:
            print("# pedra x papel #")
            print("derrota !!!")
        elif adversario==3:
            print("# pedra x tesoura #")
            print("vitória !!!") 
#-----------------------------------------------------------------------------------------                            
    elif eu==2:
        print("papel !!!")
        if adversario==1:
            print(" # papel x pedra # ")
            print("vitoria !!!")
        elif adversario==2:
            print(" # papel x papel # ")
            print("empate !!!")
        elif adversario==3:       
            print(" # papel x tesoura # ") 
            print("derrota")    
#-----------------------------------------------------------------------------------------
    elif eu==3:
        print("tesoura !!!") 
        if adversario==1:
            print(" # tesoura x pedra # ")
            print("derrota !!!")
        elif adversario==2:
            print(" # tesoura x papel # ")
            print("vitória !!!")
        elif adversario==3:       
            print(" # tesoura x tesoura # ") 
            print("empate !!!")  
#-----------------------------------------------------------------------------------------                          
    resp=input("continuar? ").upper()