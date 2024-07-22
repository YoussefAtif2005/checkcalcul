def calculatrice(num1, num2, opérat):
    
    if opérat=="+":
        return num1+num2
    elif opérat=="*":
        return num1*num2
    elif opérat=="-":
        return num1-num2
    elif (opérat=="/"and num2!=0):
        return num1/num2
    
print(calculatrice(23, 5, "/"))