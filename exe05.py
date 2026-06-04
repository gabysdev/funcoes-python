def calculadora(a, b, operacao):
    if operacao == '+':
        result = a + b
    elif operacao == '-':
        result = a - b 
    elif operacao == '*':
        result = a * b
    else:
        result = a / b
    return result        

if __name__ == "__main__":
    print(calculadora(4, 2, "+"))
    print(calculadora(4, 2, "-"))
    print(calculadora(4, 2, "*"))
    print(calculadora(4, 2, "/"))