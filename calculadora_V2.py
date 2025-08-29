def menu():
    print("Calculadora do Guilherme")
    print("0 - Sair")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

def soma(num1, num2):
    igual = num1 + num2
    return igual

def subtracao(num1, num2):
    igual = num1 - num2
    return igual

def multiplicacao(num1, num2):
    igual = num1 * num2
    return igual

def divisao(num1, num2):
    igual = num1 / num2
    return igual


def pedir_numero(num):
    tentativa = 1
    numero = None  
    while numero is None:
        
        try:
            mensagem = f"Numero {num}: " 
            if tentativa > 1:
                mensagem = "Invalido, Digite novamente: "
            numero = float(input(mensagem))
        except:
            pass
        tentativa = tentativa + 1
    return numero

def pedir_operacao():
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
        return operação


while True:
    menu()

    operação = pedir_operacao()
    
    if operação == 0:
        print("Saindo...")
        break
    if operação not in  [1, 2, 3, 4]:
        print("Opção inválida")
        continue 
    
    numero1 = pedir_numero(1)
    numero2 = pedir_numero(2)

    if operação == 1:
        print("A soma de", numero1,"e", numero2,"é", soma(numero1, numero2))
    elif operação == 2:
        print("A subtração do", numero1,"e", numero2,"é", subtracao(numero1, numero2))
    elif operação == 3:
        print("A multiplicação do", numero1,"e", numero2,"é", multiplicacao(numero1, numero2))
    elif operação == 4:
        print("A divisão do", numero1,"e", numero2,"é", divisao(numero1, numero2))        
    print("-------------------")