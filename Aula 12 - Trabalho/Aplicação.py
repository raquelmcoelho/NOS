import random
import string
import re
import json


class User:
    def __init__(self, nome):
        self.nome = str(nome).lower()
        self.dados = [self.nome]

    def adicionardados(self, dado):
        self.dados.append(str(dado).lower())

    def adicionardadodata(self, data):
        self.adicionardados(str("".join(re.findall(r"\d", data))))


class Cofre:
    def __init__(self, username, senha):
        self.user = User(username)
        self.cofre = {"Clientid": self.user.nome + str(senha), "Nome" : self.user.nome, "Senha desse app": str(senha)}

    def __str__(self):
        txt = ""
        for x in self.cofre:
            txt += x + " : " + self.cofre[x] + "\n"
        return txt

    def adicionarsenha(self, cadeado, senha):
        self.cofre[str(cadeado)] = str(senha)

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
        for i in self.user.dados:
            if len(re.findall("[%s]{%d,%d}" % (i, len(i)/2,  len(i)), senha.lower())) > 0:
                fraqueza += 1
                print(i, " : ", re.findall("[%s]{%d,%d}" % (i, len(i)/2, len(i)), senha.lower()))
        for i in self.cofre.values():
            if i == senha:
                fraqueza += 1
        maxfraqueza = len(self.user.dados) + len(self.cofre.values())
        if fraqueza == maxfraqueza:
            return "senha muito fraca"
        elif 0 < fraqueza < maxfraqueza:
            return "senha fraca"
        elif fraqueza == 0:
            return "senha forte"

    def acesso(self, chave):
        if chave in self.cofre.keys():
            return self.cofre[chave]
        else:
            return "chave não criada ainda"


class Info:
    # todo no init pra ser dado + cofre
    def __init__(self, filename, dados):
        self.filename = str(filename) + ".json"
        self.dados = dados

    def salvar(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.dados, f)

    def ler(self):
        with open(self.filename, "r") as f:
            txt = json.load(f)
        return txt



texto = """
Gerenciador de Senhas, frame, image, em cima

texto utilidades ux, frame embaixo
button começar e sair , desroy frame


Fazer inscrição ou entrar, frame embaixo
    inserir nome, entry 
    criar senha para o cofre , entry
    button,  infor.salvar()
    if info.ler() == "" 
        explicar que precisa de dados pra criar senhas mais fortes que não sejam fáceis de deduzir, messagebox
        Inserir dados : user.adicionardados() - nascimento, pai, mãe, dataimportante, nomeimportante
        infor.salvar()
    frame.destroy()


Visualizar senhas existentes: info.ler(), frame
    adicionar senha, addsenha(), info.salvar(), info.ler()
    checar se são seguras (individual cada) - button no seu label c função de checarsenha()
        if != "senha forte" : 
            criarsenha() c button de command [cadeado] = nova senha
            info.salvar()
    pesquisar por cadeado
        label(acesso(entry.get))
    salvar dados e sair
    
"""
