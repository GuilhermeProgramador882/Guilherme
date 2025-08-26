while True:
    print("Calculadora do Guilherme")
    print("0 - Sair")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    operação = None
    tentativa = 1
    while operação is None:

        try:
            mensagem = "Qual operação? "
            if tentativa > 1:
                mensagem = "Digite um numero, letras são invalidas: "
            operação = int(input(mensagem))
        except ValueError:
            pass  
        tentativa = tentativa + 1  
    
    if operação == 0:
        print("Saindo...")
        break
    if operação not in  [1, 2, 3, 4]:
        print("Opção inválida")
        continue 
    tentativa = 1
    numero1 = None  
    while numero1 is None:
        
        try:
    
            mensagem = "Numero 1: " 
            if tentativa > 1:
                mensagem = "Invalido, Digite novamente: "
            numero1 = float(input(mensagem))
        except ValueError:
            pass
        tentativa = tentativa + 1

    tentativa = 1
    numero2 = None  
    while numero2 is None:
        
        try:
    
            mensagem = "Numero 2: " 
            if tentativa > 1:
                mensagem = "Invalido, Digite novamente: "
            numero2 = float(input(mensagem))
        except ValueError:
            pass
        tentativa = tentativa + 1

    if operação == 1:
        print("A soma de", numero1,"e", numero2,"é", numero1+numero2)
    elif operação == 2:
        print("A subtração do", numero1,"e", numero2,"é", numero1-numero2)
    elif operação == 3:
        print("A multiplicação do", numero1,"e", numero2,"é", numero1*numero2)
    elif operação == 4:
        print("A divisão do", numero1,"e", numero2,"é", numero1/numero2)        