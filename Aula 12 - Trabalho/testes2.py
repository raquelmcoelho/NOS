import random
import string
import re


class Cofre:
    def __init__(self, username, senha):
        self.nome = str(username).lower()
        self.cofre = {"Client": self.nome, "Password": str(senha)}
        self.dados = [self.nome]

    def __str__(self):
        txt = ""
        for x in self.cofre:
            txt += x + " : " + self.cofre[x] + "\n"
        return txt

    def adicionarsenha(self, cadeado, senha):
        self.cofre[str(cadeado)] = str(senha)

    # dados para o regex
    def adicionardados(self, dado):
        self.dados.append(str(dado).lower())

    def adicionardadodata(self, data):
        self.adicionardados(str("".join(re.findall(r"\d", data))))

    def criarsenha(self, tamanho):
        caracteres = string.digits + string.ascii_letters + string.punctuation
        resp = 0
        senha = 0
        while resp != "senha forte":
            senha = "".join(random.choices(caracteres, k=int(tamanho)))
            resp = self.checarsenha(senha)
        return senha

    def checarsenha(self, senha):
        fraqueza = 0
        for i in self.dados:
            if len(re.findall("[%s]{%d,%d}" % (i, len(i)/2,  len(i)), senha.lower())) > 0:
                fraqueza += 1
                print(i, " : ", re.findall("[%s]{%d,%d}" % (i, len(i)/2, len(i)), senha.lower()))

        if fraqueza == len(self.dados):
            return "senha muito fraca"
        elif 0 < fraqueza < len(self.dados):
            return "senha fraca"
        elif fraqueza == 0:
            return "senha forte"

    def acesso(self, chave):
        if chave in self.cofre.keys():
            return self.cofre[chave]
        else:
            return "chave não criada ainda"

raquel = Cofre("raquel", "123")
print(raquel.dados)