#variáveis
a = 0
b = 0
x = 0
operacao = ""

#definição da operação matemática
operacao = input("Escolha a operação + ou - : ")

if(operacao != '+'):
    print("A operação não é válida ")

elif(operacao == '+'):

#entrada dos valores
    a = eval(input("Digite o número: "))
    b = eval(input("Digite o número: "))

#realização do cálculo
    if(operacao == '+'):
        x = a + b
        print("A resultado é " + str(x))
    elif(operacao == '-'):
        x = a - b
        print("A resultado é " + str(x))