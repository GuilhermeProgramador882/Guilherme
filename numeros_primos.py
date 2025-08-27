for num in range(1, 51):  
    if num > 1:  
        eh_primo = True
        for i in range(2, num):  
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            print(num)