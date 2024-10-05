def menu():

    while True:
        print("OPÇÕES:")
        print("[1] - ADIÇÃO: ")
        print("[2] - SUBTRAÇÃO: ")
        print("[3] - MULTIPLICAÇÃO: ")
        print("[4] - DIVISÃO: ")

options = input("Digite qual operação você deseja escolher: ")

if options == '1':
    n1 = int(input("Digite o primeiro valor para soma: "))
    n2 = int(input("Digite o segundo valor para soma: "))
    print(n1 + n2)
if options == '2':
    n1 = int(input("Digite o primeiro valor para subtração: "))
    n2 = int(input("Digite o segundo valor para subtração: "))
    print(n1 - n2)
if options == '3':
    n1 = int(input("Digite o primeiro valor para multiplicação: "))
    n2 = int(input("Digite o segundo valor para multiplicação: "))
    print(n1 * n2)
if options == '4':
    n1 = int(input("Digite o primeiro valor para divisão: "))
    n2 = int(input("Digite o segundo valor para divisão: "))
    print(n1 / n2)
