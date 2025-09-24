for num in range(1, 51):  
    if num > 1:  
        e_primo = True
        for i in range(2, num):  
            if num % i == 0:
                e_primo = False
                break
        if e_primo:
            print(num)