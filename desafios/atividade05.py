# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;


def atividade05(string: str):
    inverted_string = ""

    for char in range(len(string) - 1, -1, -1):
        inverted_string += string[char]

    return inverted_string


if __name__ == "__main__":
    string = "Hello, World!"
    print(atividade05(string))
