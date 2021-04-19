"""
2.Escrever um programa em Python que encontre a palavra mais longa em um arquivo.
"""
maior = [""]

with open("arquivo.txt") as f:
    for a, line in enumerate(f.readlines()):
        words = line.split()
        for i in words:
            if len(i) > len(maior[0]):
                maior.clear()
                maior.append(i)
                maior.append(f"que se encontra na linha {a}")

            elif len(i) == len(maior[0]):
                maior.append(i)
                maior.append(f"que se encontra na linha {a}")

print("palavra(s) maior(es):\n")
[print(maior[b]) for b in range(len(maior))]
