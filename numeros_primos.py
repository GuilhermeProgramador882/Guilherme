for num in range(1, 51):  # percorre de 1 até 50
    if num > 1:  # números primos são maiores que 1
        eh_primo = True
        for i in range(2, num):  # testa divisores de 2 até num-1
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            print(num)