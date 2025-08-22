while True:
    print("Calculadora do Guilherme")
    print("0 - Sair")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    operação = int(input("Qual a operação? "))
    if operação == 0:
        print("Saindo")
        break
    if operação not in  [1, 2, 3, 4]:
        print("Opção inválida")
        continue 

    numero1 = float(input("Numero 1: "))
    numero2 = float (input("Numero 2: "))
    if operação == 1:
        print("A soma de", numero1,"e", numero2,"é", numero1+numero2)
    elif operação == 2:
        print("A subtração do", numero1,"e", numero2,"é", numero1-numero2)
    elif operação == 3:
        print("A multiplicação do", numero1,"e", numero2,"é", numero1*numero2)
    elif operação == 4:
       if numero2 == 0:
           print("A divisão do",numero1,"com o",numero2,"é igual a 0")
       else:
           print("A divisão do", numero1,"e", numero2,"é", numero1/numero2)
    else:
       print("Opção nao existe")