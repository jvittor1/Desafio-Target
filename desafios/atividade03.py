# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.


def atividade03(profit: list):
    min_profit = min(profit)
    max_profit = max(profit)
    avg_profit = sum(profit) / len(profit)
    days = 0
    for value in profit:
        if value > avg_profit:
            days += 1
    return min_profit, max_profit, days


if __name__ == "__main__":
    profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    print(atividade03(profit))
