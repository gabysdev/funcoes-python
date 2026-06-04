def palindromo(texto):
    # Remove espaços e converte tudo para minúsculo
    texto_limpo = texto.replace(" ", "").lower()
    # Verifica se o texto é igual ao seu inverso
    return texto_limpo == texto_limpo[::-1]

if __name__ == "__main__":
    print(palindromo("radar")) 
    # Saída: True