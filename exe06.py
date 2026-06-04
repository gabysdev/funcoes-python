def contar_vogais(texto):
    count_vogal = 0
    for letra in texto:
        if letra.upper() in 'AEIOU':
            count_vogal += 1
    return count_vogal

if __name__ == "__main__":
    print(contar_vogais("GABRIELLE"))     