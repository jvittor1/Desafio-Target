# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?


def atividade01(index: int, sum: int, k: int):
    while k < index:
        k += 1
        sum += k
    return sum


if __name__ == "__main__":
    index = 13
    sum = 0
    k = 0
    print(atividade01(index, sum, k))
