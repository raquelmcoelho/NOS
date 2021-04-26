"""
1.Escrever um programa em Python para informar ao usuário a quantidade de linhas e caracteres
de um arquivo texto.
"""

resposta = input("você deseja escrever no arquivo?(sim/não) ")
while resposta != "não":
    with open("arquivo.txt", "a") as f:
        a = input("escreva o que quer por:\n")
        f.write(a + "\n")
        f.close()
        resposta = input("você deseja mais uma linha?(sim/não) ")
else:
    tamanho = 0
    print("aqui está o arquivo que você criou:")
    with open("arquivo.txt", "r") as f:
        for i, line in enumerate(f.readlines()):
            print(f"linha {i}:", line)
            tamanho += len(line)

    print("número de caracteres:", tamanho)
