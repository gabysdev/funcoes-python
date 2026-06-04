def media_lista(numeros):
    if not numeros:
        return 0  # Retorna 0 se a lista estiver vazia para evitar erro de divisão por zero
    return sum(numeros) / len(numeros)

# Exemplo de uso:
if __name__ == "__main__":
    resultado = media_lista([10, 20, 30])
    print(resultado)  # Saída: 20.0