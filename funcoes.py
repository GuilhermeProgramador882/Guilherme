def multiplicacao(num1, num2):
    igual = num1 * num2
    return igual
print (multiplicacao(5, 5))

def divisao(num1, num2):
    igual = num1 / num2
    return igual
print (divisao(5, 5))

def soma(num1, num2):
    igual = num1 + num2
    return igual
print (soma(5, 5))

def subtracao(num1, num2):
    igual = num1 - num2
    return igual
print (subtracao(5, 5))


def numero_impar(e_impar):
 if e_impar % 2 > 0:
  return True
 else:
  return False 
 
for num in range(1, 101):
 if numero_impar(num):
  print(f"o numero {num} e impar")
 else:
  print(f"o numero {num} e par")