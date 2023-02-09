def opcao(): 
    print("\n")
    print('-'*40)
    print(' '*14+"Calculadora")
    print('-'*40)
    op = int(input("\n1- soma\n2- subtracao\n3- divisao\n4- multiplicacao\n5- sair\n"))
    return op

def calculo(opcao):
    a = float(input("Primeiro numero:"))
    b = float(input("Segundo numero:"))

    if opcao==1:
        print(f"{a} + {b} = {a+b}")
    
    elif opcao == 2:
        print(f"{a} - {b} = {a-b}")
    
    elif opcao == 3:
        print(f"{a}/{b} = {a/b}")
    
    elif opcao == 4:
        print(f"{a} x {b} = {a*b}")
    
    else:
        print("opcao invalida, tente de novo")


op = 0
while(op!=5):
    op = opcao()
    if(op!=5):
        calculo(op)
        
    elif(op==5):
        print("Obrigado por usar o programa, volte sempre!")
