# main.py

def analisar_lista(numeros):
    """
    Analisa uma lista de números inteiros e retorna um dicionário com:
    - maior número
    - menor número
    - média
    - quantidade de pares
    - quantidade de ímpares
    """
    if not numeros:
        return "Lista vazia."

    maior = max(numeros)
    menor = min(numeros)
    media = sum(numeros) / len(numeros)
    pares = len([n for n in numeros if n % 2 == 0])
    impares = len(numeros) - pares

    return {
        "maior": maior,
        "menor": menor,
        "media": media,
        "pares": pares,
        "impares": impares
    }
