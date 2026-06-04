def somar(a: int, b: int) -> int:
    """
    Soma dois números inteiros.

    Args:
        a (int): Primeiro número.
        b (int): Segundo número.
    Returns:
        int: Resultado da soma.    
    """
    return a + b

if __name__ == "__main__":
    result = somar(2,7)
    result2 = somar(5,3)

    print(result)
    print(result2)

    print(somar(10,8))