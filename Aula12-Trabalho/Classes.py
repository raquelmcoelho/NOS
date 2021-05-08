from collections import namedtuple
import random
import string
import re


# class do usuário
class User:
    def __init__(self, username):
        self.name = str(username).lower()
        self.dados = []

    def adicionardados(self, dado):
        self.dados.append(str(dado).lower())

    def adicionardadonumero(self, data):
        self.adicionardados(str("".join(re.findall(r"\d", data))))


# class bank methods
class Cofre:
    def __init__(self, username, senha):
        self.user = User(username)
        self.cofre = {"clientid": self.user.name + str(senha), "nome": self.user.name, "cofre": str(senha)}
        self.dados = self.user.dados

    def __str__(self):
        txt = ""
        for x in self.cofre:
            txt += x + " : " + self.cofre[x] + "\n"
        return txt

    def adddados(self, dados, num):
        dados1 = str(dados)
        if num == 0:
            self.user.adicionardados(dados1)
        elif num == 1:
            self.user.adicionardadonumero(dados1)

    def adicionarsenha(self, cadeado, senha):
        self.cofre[str(cadeado.lower())] = str(senha)

    def criarsenha(self, tamanho):
        caracteres = string.digits + string.ascii_letters + string.punctuation
        resp = 0
        senha = 0
        while resp != "senha forte":
            senha = "".join(random.choices(caracteres, k=int(tamanho)))
            resp, valor = self.checarsenha(senha)
            print(valor)
        return senha

    def checarsenha(self, senha):
        senha = str(senha)
        fraqueza = 0
        forte = 0
        a, b = self.iterardados(senha)
        a1, b1 = self.iterarcofre(senha)
        a2, b2 = self.checarrequisitos(senha)
        txt = a + a1 + a2
        total = -b - b1 + b2
        # todo reverter requisito 6 asteriscos
        total += forte - fraqueza
        # retornando nível de segurança senha é
        if total < 0:
            return "senha extremamente ruim", txt
        if total == 0:
            return "fraca", txt
        if total > 0:
            if total == 1 or total == 2:
                return "senha boa", txt
            if total == 3:
                return "senha média", txt
            if total >= 5:
                return "senha forte", txt

    def checarrequisitos(self, elemento):
        import re
        fraqueza = 0
        forte = 0
        txt = ""
        # checando se tem no mínimo uma letra maiúscula, uma minúscula, um dígito e 6 caracteres
        cond = {"dígito": string.digits, "símbolo": string.punctuation, "minúscula": string.ascii_lowercase,
                "maiúscula": string.ascii_uppercase}
        for i in cond:
            if len(re.findall("[%s]" % (cond[i]), elemento)) > 0:
                forte += 1
            else:
                txt += f"Não encontramos um(a) {i} na sua senha\n"
                fraqueza += 1

        if len(elemento) >= 6:
            forte += 1
        elif len(elemento) < 6:
            txt += f"Sua senha tem menos de 6 dígitos\n"
            fraqueza += 1

        total = forte - fraqueza
        return txt, total

    def iterardados(self, elemento):
        import re
        # iterando dados
        fraqueza = 0
        txt = ""
        for i in self.user.dados:
            if len(re.findall("%s" % i, elemento.lower())) > 0:
                txt += "foi encontrado o dado '%s' na sua senha\n" % i
                fraqueza += 1
        return txt, fraqueza

    def iterarcofre(self, elemento):
        # iterando cofre
        txt = ""
        fraqueza = 0
        for i in self.cofre:
            if len(re.findall("%s" % i, elemento.lower())) > 0:
                txt += f"foi encontrado o nome do cadeado '{i}' na sua senha\n"
                fraqueza += 1

            if len(re.findall("%s" % self.cofre[i], elemento.lower())) > 0:
                fraqueza += 1
        if fraqueza > 2:
            txt += f"essa senha já foi utilizada em outro cadeado\n"

        return txt, fraqueza

    def acesso(self, chave):
        for i in zip(self.cofre.keys(), self.cofre.values()):
            if chave in i:
                return i

    def acessarpelocadeado(self, key):
        for i in self.cofre:
            if key == i:
                return {i: self.cofre[i]}

    def save(self):
        dadoscofre = namedtuple("user", ["clientid", "dados", "cofre"])
        dadoscliente = dadoscofre(clientid=self.cofre["clientid"],
                                  dados=self.user.dados,
                                  cofre=self.cofre)
        return dadoscliente
