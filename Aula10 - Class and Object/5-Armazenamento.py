"""
1. Controle de cotas de disco. A ACME Inc., uma organização com mais de 1500 funcionários, está tendo problemas de
espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber
qual o espaço em disco ocupado pelas contas dos usuários, e identificar os usuários com maior espaço ocupado. Através
de um aplicativo baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado usuarios.txt:
alexandre 456123789
anderson 1245698456
antonio 123456456
carlos 91257581
cesar 987458
rosemary 789456125

• Neste arquivo, o primeiro campo corresponde ao login do usuário e o segundo ao espaço em disco ocupado pelo seu
diretório home. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado relatório.txt, no
seguinte formato:
ACME Inc. Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr. Usuário Espaço utilizado % do uso
1 alexandre 434,99 MB 16,85%
2 anderson 1187,99 MB 46,02%
3 antonio 117,73 MB 4,56%
4 carlos 87,03 MB 3,37%
5 cesar 0,94 MB 0,04%
6 rosemary 752,88 MB 29,16%
Espaço total ocupado: 2581, 57 MB
Espaço médio ocupado: 430, 26 MB
• O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma
a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita
através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá
ser feito através de uma função, que será chamada pelo programa principal.
"""


class Relatorio:
    def __init__(self, filename):
        self.file = filename
        self.relatorio = "relatório.txt"
        self.nomes, self.armazenamento = [], []

        # separando nomes dos armazenamentos
        with open(self.file, "r+") as f:
            for line in f.readlines():
                a = line.strip("\n").split(" ")
                self.nomes.append(a[0])
                self.armazenamento.append(a[1])

        # tornando em número
        for i in range(len(self.armazenamento)):
            self.armazenamento[i] = int(self.armazenamento[i])

        # convert
        self.convertbytetomegabyte()
        # cria média e total
        self.total = sum(self.armazenamento)
        self.media = self.total / len(self.armazenamento)

    def convertbytetomegabyte(self):
        # decode bytes
        for i in range(len(self.armazenamento)):
            self.armazenamento[i] = self.armazenamento[i] / 1024 ** 2

    def percentagemdeuso(self):
        # dados
        porcentagens = []
        [porcentagens.append(i / self.total * 100) for i in self.armazenamento]
        return porcentagens

    def criarrelatorio(self):
        with open(self.relatorio, "w") as f2:
            # escrevendo introdução
            intro = """
             ACME Inc. Uso do espaço em disco pelos usuários
             ------------------------------------------------
              Nr. Usuário || Espaço utilizado || % do uso
             """
            f2.write(intro)

            # escrevendo dados
            st = "\n"
            percent = self.percentagemdeuso()
            for i in range(len(self.nomes)):
                st += "%15s%12s%13.2f%3s%10.2f%2s\n" % (i, self.nomes[i], self.armazenamento[i], "MB", percent[i], "%")
            f2.write(st)

            # escrevendo final
            str2 = """
            Espaço total ocupado: %7.2f MB
            Espaço médio ocupado: %7.2f MB""" % (self.total, self.media)

            f2.write(str2)

    def lerrelatorio(self):
        with open(self.relatorio, "r") as f2:
            print(f2.read())

    def clearrelatorio(self):
        import os
        os.remove(self.relatorio)
        open("relatório.txt", "x")


rel = Relatorio(r"usuarios.txt")
rel.criarrelatorio()
rel.lerrelatorio()
rel.clearrelatorio()
