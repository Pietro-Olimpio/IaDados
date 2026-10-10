# Funções da calculadora
def soma(n1,n2):
    resultado = n1 + n2
    print("O resultado da soma é:",resultado)

def subtracao(n1,n2):
    resultado = n1 - n2
    print("O resultado da subtração é:",resultado)

def divisao(n1,n2):
    if n2 == 0:
        print("Não se divide por 0 ")
    resultado = n1 / n2
    print("O resultado da divisão é:",resultado)

def multiplicacao(n1,n2):
    resultado = n1 * n2
    print("O resultado da multiplicacao é:",resultado)




#while para as opções 

while True:
    print("\nQual opção vc quer??")
    print("(1)soma")
    print("(2)subtração")
    print("(3)divisão")
    print("(4)multiplicação")
    print("(0) Sair")

    opcao = int(input("Qual opção deseja escolher? "))

    if opcao == 0:
        print("Saindo da calculadora....")
        break

    elif opcao >=1 and opcao <=4:
        if opcao == 1:
            print("\nVamos somar")
        
        elif opcao == 2:
            print("\nVamos subtrair")
        
        elif opcao == 3:
            print("\nVamos dividir")
        
        elif opcao == 4:
            print("\nVamos multiplicar")

        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))

        if opcao == 1:
            soma(n1,n2)

        elif opcao == 2:
            subtracao(n1,n2)
        
        elif opcao == 3:
            divisao(n1,n2)
        
        elif opcao == 4:
            multiplicacao(n1,n2)

        else:
            print("Burrao tem essa opção n")