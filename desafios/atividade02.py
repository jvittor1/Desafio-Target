# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


def atividade02(n: int):
    numA = 0
    numB = 1
    nextValue = 0
    while nextValue < n:
        nextValue = numA + numB
        numA = numB
        numB = nextValue

    return nextValue == n


if __name__ == "__main__":
    n = 34  # Retorna True
    print(atividade02(n))
    n = 6  # Retorna False
    print(atividade02(n))
