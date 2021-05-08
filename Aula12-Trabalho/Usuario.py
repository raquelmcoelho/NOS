# NO CLIENTE MANUSEAREMOS APENAS UMA CÓPIA DO COFRE FORNECIDA PELO SERVIDOR
from tkinter import messagebox
from Classes import *
from tkinter import *
from socket import *
from random import *
import pickle

# criação socket
clientsocket = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 9999
clientsocket.connect((host, port))
print("cliente conectado")

# padrões
BG = "#222222"
FG = "#00ffff"
FONT = ("Century Gothic", "12")
escolhadetema = 0

# textos
txtintro = """\nAqui é possivel armazenar \nsuas senhas em um lugar seguro\ntrocar se estiverem fracas
\nchecar sua segurança\ncriar senhas aleatórias \na acessa-las se necessario
"""
txtdados = """\n
No momento de checar se suas senhas são seguras ou não precisamos 
ter dados básicos seus que todos tem acesso (públicos), 
\nIsto para evitar que um hacker que lhe conheça na internet tenha 
pistas do que procurar primeiro na sua senha
\nPor isso vamos evitar essas pistas na hora de criar senhas novas
"""
txtinstrucoes = """
\n\nCADEADO: o lugar de onde ele abre
\n\nSENHA: a chave do cadeado
\n\nBOTÃO CHECK: checa o nível de força e segurança da sua senha
\n\nBOTÃO ADD/REPLACE SENHA: Adicionar ou substituir. 
Você ou entra com um cadeado novo ou com um já existente, 
se ele já existir então a senha dele será substituída pela chave que você inserir.
\n\nBOTÃO APAGAR SENHA: apaga algum cadeado que você inserir
\n\nBOTÃO VER DADOS: lhe é informado os dados que usamos como base
(fornecidos por você) para checar e criar suas senhas
\n\nBOTÃO SALVAR E SAIR: sua conta e dados são atualizados
\n\nBOTÃO EXCLUIR MINHA CONTA: sua conta é excluída não podendo ser recuperada"""


# funções para o tkinter
def mudarcor(framename):
    for widget in framename.winfo_children():
        widget["bg"] = BG
        widget["fg"] = FG
    framename["bg"] = BG
    limpaframe(framename)


def mudartema():
    global BG, FG, escolhadetema
    fontes = [("#ff80ff", "#000000"), ("#ffff00", "#0b4b88"),
              ("#eeeeee", "#d10000"), ("#00ffff", "#222222")]
    escolha = escolhadetema % len(fontes)
    print("escolha de fonte", escolhadetema, "%", len(fontes), "=",  escolha, fontes[escolha])
    FG = fontes[escolha][0]
    BG = fontes[escolha][1]
    escolhadetema += 1
    mudarcor(frame0)
    mudarcor(frame1)
    mudarcor(frame2)
    tk["bg"] = BG
    tela1()


def limpaframe(framename):
    for widget in framename.winfo_children():
        widget.destroy()


def labelentry(frame, txt, place, place2):
    Label(frame, text=txt,
          font=FONT, bg=BG, fg=FG).place(relx=place[0], rely=place[1], relheight=place[2], relwidth=place[3])
    e = Entry(frame, font=FONT)
    e.place(relx=place2[0], rely=place2[1], relheight=place2[2], relwidth=place2[3])
    return e


def lbl(frame, txt, p):
    Label(frame, text=txt, font=FONT, bg=BG, fg=FG).place(relx=p[0], rely=p[1], relheight=p[2], relwidth=p[3])


def b(frame, txt, command, p):
    Button(frame, text=txt, command=command,
           font=FONT, bg=FG, fg=BG).place(relx=p[0], rely=p[1], relheight=p[2], relwidth=p[3])


def requestsocketreplace(client):
    print("cliente enviado para a função", client)
    clientsocket.send("replace".encode())
    bclient = pickle.dumps(client)
    clientsocket.send(bclient)
    txt = clientsocket.recv(4096)
    print(txt.decode())
    return txt.decode()


# início do app
def tela1():
    lbl(frame0, "Gerenciador de senhas", [0.25, 0.20, 0.70, 0.5])
    b(frame1, "Vamos começar", lambda: tela2(), [0.33, 0, 0.15, 0.33])
    b(frame1, "Mudar tema", lambda: mudartema(), [0.33, 0.20, 0.15, 0.33])


# tela de apresentação
def tela2():
    limpaframe(frame1)
    limpaframe(frame2)
    lbl(frame1, txtintro, [0.25, 0, 0.85, 0.50])
    b(frame1, "ok", lambda: tela3(), [0.33, 0.85, 0.15, 0.33])


# tela de login
def tela3():
    def sair():
        clientsocket.send("sair".encode())
        clientsocket.close()
        tk.quit()
    # limpeza dos frames
    limpaframe(frame0)
    limpaframe(frame1)
    limpaframe(frame2)
    tk.title("Inscrever||Entrar")
    # inserir informações de login
    lbl(frame0, "Para se inscrever ou entrar digite:", [0.15, 0.60, 0.30, 0.70])
    nome = labelentry(frame1, "Seu nome:", [0.10, 0.00, 0.25, 0.25], [0.35, 0.00, 0.25, 0.55])
    senha = labelentry(frame1, "Sua senha:", [0.10, 0.50, 0.25, 0.25], [0.35, 0.50, 0.25, 0.55])
    # direcionamento ou para se inscrever ou para entrar
    b(frame2, "Inscrever", lambda: tela4(nome.get().lower(), senha.get().lower()), [0.25, 0, 0.30, 0.25])
    b(frame2, "Entrar", lambda: tela5(nome.get().lower(), senha.get().lower()), [0.50, 0, 0.30, 0.25])
    # botão de sair
    b(frame2, "sair", lambda: sair(), [0.25, 0.30, 0.30, 0.50])


# tela de se inscrever
def tela4(nome, senha):
    # se tiver vazio volta para a tela anterior
    if senha == "" or nome == "":
        messagebox.showinfo("erro", "Por favor preencha os dois espaços")
        tela3()
    else:
        nomecliente = nome
        senhacliente = senha

        def continuar():
            # dados numéricos ele armazena de uma vez e dados string ele armazenada com split e strip
            dados = [entrys[0].get(), entrys[1].get(), entrys[2].get()]
            for dado in range(len(dados)):
                dadoh = "".join(re.findall(r"\d+", dados[dado]))
                dados.append(dadoh)
            for _ in range(0, 3, 1):
                dados.remove(dados[0])
            dados += entrys[3].get().strip().split(" ") + entrys[4].get().strip().split(" ")
            print("dados:", dados)
            # se algum dado vier vazio
            if dados.count("") > 0:
                # aviso e volta para a tela de preencher dados
                messagebox.showinfo("erro", "Você esqueceu de preencher um espaço corretamente")
                tela4(nomecliente, senhacliente)
            else:
                # salvar cliente no json de users
                clientsocket.send("salvarnovocliente".encode())
                client = Cofre(nomecliente, senhacliente)
                bclient = pickle.dumps(client)
                clientsocket.send(bclient)
                resposta = clientsocket.recv(4096)
                print(resposta.decode())
                if resposta.decode() == "Seu cliente foi salvo":
                    # salvar os dados informando em qual cliente salvar
                    clientsocket.send("adddados".encode())
                    bdados = pickle.dumps(dados)
                    clientsocket.send(bdados)
                    client = Cofre(nomecliente, senhacliente)
                    bclient1 = pickle.dumps(client)
                    print(client, "sendo enviado")
                    clientsocket.send(bclient1)
                    resposta = clientsocket.recv(4096)
                    print(resposta.decode())
                    # direcionar para a tela de acesso aos próprios dados
                    tela5(nomecliente, senhacliente)

        limpaframe(frame0)
        limpaframe(frame1)
        limpaframe(frame2)
        # aviso sobre os dados
        messagebox.showinfo("Dados Públicos", txtdados)
        # pegar dados
        lbl(frame0, "Dados Públicos - (dicas para o hacker)", [0.15, 0.30, 0.30, 0.70])
        entrys = [0, 0, 0, 0, 0]
        txts = ["Data de nascimento:", "N° de telefone:", "Número importante:", "Nome completo:", "Nome importante:"]
        # criar entrys para cada dado
        j = 0
        for i in range(1, 6):
            entrys[i - 1] = labelentry(frame1, txts[i - 1], [0.05, j, 0.2, 0.40], [0.45, j, 0.2, 0.50])
            j += 0.2

        b(frame2, "Continuar", lambda: continuar(), [0.50, 0.30, 0.15, 0.25])
        b(frame2, "Voltar", lambda: tela3(), [0.25, 0.30, 0.15, 0.25])


# tela de acesso as senhas e manuseio (coração do app)
def tela5(nome, senha):
    # retornar para a inscrição
    if senha == "" or nome == "":
        messagebox.showinfo("erro", "Por favor preencha os dois espaços")
        tela3()
    # copiar cliente para manuseio
    else:
        idclient = str(nome) + str(senha)
        # pesquisar se o cliente existe no file
        clientsocket.send("acessaruserinfo".encode())
        clientsocket.send(idclient.encode())
        binfor = clientsocket.recv(4096)
        infor = pickle.loads(binfor)
        print("Dados encontrados do cliente no file:", infor, "\nidclient:", idclient)
        if infor is None:
            # se não tiver nada retorna a tela de login
            messagebox.showinfo("erro", "Usuário não encontrado")
            tela3()
        else:
            # pegar o cliente no socket
            clientsocket.send("pegarclient".encode())
            binfor = pickle.dumps(infor)
            clientsocket.send(binfor)
            bclient = clientsocket.recv(4096)
            client = pickle.loads(bclient)
            nomecliente = nome
            senhacliente = senha

            #
            # funções dos botões do frame2 (frame de baixo)
            #
            def deletar2(num, elemento=""):
                # se o método for 1 ele quer deletar uma senha
                elem = elemento.lower()
                if num == 1:
                    # se elemento for o cofre, ou for vazio ou não estiver no cofre ele interrompe
                    if elem == "cofre" or elem == "" or elem not in client.cofre:
                        messagebox.showinfo("erro", "Não é possível deletar isto")
                        # volta ao def de inserir cadeado a ser deletado
                        deletar(1)
                    else:
                        aviso = messagebox.askyesno("cuidado", "Tem certeza que deseja fazer isso?")
                        # se sim
                        if aviso == 1:
                            # deleta do cofre
                            print("deletando cadeado")
                            del client.cofre[elemento]
                            # substitui o cliente do file com o cliente que tem o elemento deletado através do servidor
                            message = requestsocketreplace(client)
                            if message == "seu cliente foi substituido":
                                tela5(nomecliente, senhacliente)
                        # se não
                        elif aviso == 0:
                            deletar(1)

                # se o número for 0 ele quer deletar um cliente
                elif num == 0:
                    a = messagebox.askyesno("cuidado", "Tem certeza que deseja fazer isso? Todos seus dados e "
                                                       "senhas serão apagados")
                    # se sim ele deleta o client
                    if a == 1:
                        clientsocket.send("deleteuser".encode())
                        client3 = Cofre(nomecliente, senhacliente)
                        bclient3 = pickle.dumps(client3)
                        clientsocket.send(bclient3)
                        txt = clientsocket.recv(4096)
                        print(txt.decode())
                        clientsocket.send("sair".encode())
                        clientsocket.close()
                        tk.quit()

                    # se não volta a tela anterior
                    elif a == 0:
                        tela5(nomecliente, senhacliente)

            def deletar(metodo):
                limpaframe(frame0)
                limpaframe(frame4)
                limpaframe(frame2)
                lbl(frame4, "Qual cadeado você deseja deletar?", [0, 0, 0.20, 1])
                deletado = Entry(frame4, font=FONT)
                deletado.place(relx=0.33, rely=0.30, relheight=0.10, relwidth=0.33)
                # deletar o cadeado do entry utilizando o método 1 na função deletar2
                b(frame2, 'deletar', lambda: deletar2(metodo, deletado.get()), [0.50, 0, 0.15, 0.25])
                b(frame2, "voltar", lambda: tela5(nomecliente, senhacliente), [0.25, 0, 0.15, 0.25])

            def logout():
                # salva cliente
                message = requestsocketreplace(client)
                if message == "seu cliente foi substituido":
                    # fecha tk e o socket
                    clientsocket.send("sair".encode())
                    clientsocket.close()
                    tk.quit()

            def printdados():
                limpaframe(frame0)
                limpaframe(frame4)
                limpaframe(frame2)
                txt = "Esses são os dados que usamos na hora de checar\n se suas senhas são seguras ou não:\n"
                for i in client.dados:
                    txt += "\n" + str(i)
                lbl(frame4, txt, [0, 0, 1, 1])
                b(frame2, "voltar", lambda: tela5(nomecliente, senhacliente), [0.33, 0, 0.15, 0.33])

            def add():
                limpaframe(frame4)
                limpaframe(frame2)
                lbl(frame4, "O que você deseja adicionar ou substituir?", [0, 0, 0.10, 1])
                addcadeado = labelentry(frame4, "Seu cadeado: ", [0.10, 0.10, 0.10, 0.40], [0.50, 0.10, 0.10, 0.40])
                addsenha = labelentry(frame4, "Sua Senha: ", [0.10, 0.20, 0.10, 0.40], [0.50, 0.20, 0.10, 0.40])
                # recebe dois valores e ou manda para o troca 3 ou volta para a tela anterior
                b(frame2, "adicionar", lambda: troca3(addcadeado.get(), addsenha.get()), [0.33, 0, 0.15, 0.33])
                b(frame2, "voltar", lambda: tela5(nomecliente, senhacliente), [0.33, 0.20, 0.15, 0.33])

            #
            # funções do botão check
            #
            def troca3(cadeado3, key2):
                # se chegar aqui é porque a troca é definitiva
                limpaframe(frame1)
                # quando se adiciona uma senha em um cadeado existente ele só substitui a senha
                client.adicionarsenha(cadeado3, key2)
                # salvar o cliente e substituir ele no file json
                message = requestsocketreplace(client)
                if message == "seu cliente foi substituido":
                    # voltar a tela de acesso
                    tela5(nomecliente, senhacliente)

            def troca2(cadeado2, key):
                limpaframe(frame4)
                # aqui é retornado o nível da senha criada
                nivel, texto = client.checarsenha(key)
                lbl(frame4, cadeado2 + " : " + key, [0.33, 0, 0.10, 0.33])
                lbl(frame4, nivel + "\n" + texto, [0, 0.10, 0.60, 1])
                # perguntado se quer realmente trocar ou tentar novamente
                lbl(frame4, "Deseja por como a nova senha?", [0, 0.70, 0.10, 1])
                # se sim ele realiza a troca mandando para o troca 3
                b(frame4, "sim", lambda: troca3(cadeado2, key), [0.50, 0.85, 0.10, 0.40])
                # se tentar novamente ele manda para a tela de escolhe se cria senha manual ou automático
                b(frame4, "tentar novamente", lambda: troca(cadeado2), [0.10, 0.85, 0.10, 0.40])

            def manual(cadeado1):
                limpaframe(frame4)
                lbl(frame4, "Inserir nova senha:", [0.33, 0, 0.10, 0.33])
                novasenha = Entry(frame4, font=FONT)
                novasenha.place(relx=0.33, rely=0.33, relheight=0.10, relwidth=0.33)
                # manda para o troca2 com uma senha criada manualmente
                b(frame4, "avançar", lambda: troca2(cadeado1, novasenha.get()), [0.33, 0.66, 0.10, 0.33])

            def troca(cadeado):
                limpaframe(frame0)
                limpaframe(frame4)
                # escolher se prefere criar a nova senha ou criar automaticamente
                b(frame4, "Criar a nova senha", lambda: manual(cadeado), [0.16, 0, 0.10, 0.66])
                # se criar automaticamente ele já manda pro troca dois com uma senha criada de tamanho entre 7 e 12
                b(frame4, "Criar automaticamente senha forte",
                  lambda: troca2(cadeado, client.criarsenha(randint(7, 12))), [0.16, 0.10, 0.10, 0.66])

            def check(cadeadocheck, senhacheck):
                limpaframe(frame2)
                limpaframe(frame4)
                nivel, texto = client.checarsenha(senhacheck)
                # mostrar qual cadeado e qual senha tá checando
                lbl(frame4, cadeadocheck + " : " + senhacheck, [0.33, 0, 0.10, 0.33])

                # mostrar o nível e o texto que explica o nível
                lbl(frame4, nivel + "\n" + texto, [0, 0.10, 0.90, 1])

                # opção de trocar senha existente depois de receber o feedback
                b(frame2, "trocar", lambda: troca(cadeadocheck), [0.60, 0, 0.15, 0.30])
                # retorna pra tela anterior
                b(frame2, "voltar", lambda: tela5(nomecliente, senhacliente), [0.20, 0, 0.15, 0.30])

            def definir_metodo(cadeado):
                # retorna um método único para cada botão criado
                return lambda: check(cadeado, client.cofre[cadeado])

            def labelbutton(cadeado, Y):
                # cria um label e um botão do lado
                # todo se for cofre ele troca o id tbm
                # labelbutton(frame4, "check", i2, [0, y, 0.10, 0.32], [0.80, y, 0.10, 0.20])
                Label(frame4, text="%s :" % cadeado, font=FONT,
                      bg=BG, fg=FG, anchor=E, justify=RIGHT). place(relx=0.05, rely=Y, relheight=0.10, relwidth=0.30)
                Label(frame4, text="%10s" % client.cofre[cadeado], font=FONT,
                      bg=BG, fg=FG, anchor=E, justify=RIGHT).place(relx=0.35, rely=Y, relheight=0.10, relwidth=0.35)
                b(frame4, "check", definir_metodo(cadeado), [0.80, Y, 0.10, 0.20])
            #
            # GUI da tela5
            #
            frame4 = Frame(tk)
            frame4["bg"] = BG
            frame4.place(relx=0, rely=0.10, relheight=0.56, relwidth=1)
            frame4["borderwidth"] = 10
            frame4["relief"] = "sunken"
            tk.title("Cofre")
            limpaframe(frame0)
            limpaframe(frame1)
            limpaframe(frame2)
            lbl(frame0, "Seja bem vindo(a) %s" % client.user.name, [0.15, 0, 0.10, 0.70])

            if len(client.cofre) > 3:
                # enumerar todas as senhas do cofre e criar um label e um botão para cada uma
                y = 0
                for j2, i2 in enumerate(client.cofre):
                    # não criar para o clienteid nem para o nome
                    if i2 != "clientid" and i2 != "nome" and i2 != "cofre":
                        labelbutton(i2, y)
                        y += 1 / 10
            else:
                lbl(frame4, "Adicione suas senhas apertando em Add/Replace", [0.05, 0.10, 0.30, 0.90])

            # botões de manuseio
            b(frame2, "Add/Replace senha", lambda: add(), [0.10, 0.18, 0.15, 0.40])
            b(frame2, "Apagar senha", lambda: deletar(1), [0.50, 0.18, 0.15, 0.40])
            b(frame2, "Ver meus dados", lambda: printdados(), [0.10, 0.33, 0.15, 0.40])
            b(frame2, "Instruções", lambda: messagebox.showinfo("instruções", txtinstrucoes), [0.50, 0.33, 0.15, 0.40])
            b(frame2, "Salvar e sair", lambda: logout(), [0.10, 0.48, 0.15, 0.40])
            b(frame2, "Excluir minha conta", lambda: deletar2(0), [0.50, 0.48, 0.15, 0.40])


# Interface gráfica tkinter
tk = Tk()
tk.title("Key Manager")
tk.geometry("500x600+433+84")
tk.iconbitmap("images/keylogogrande.ico")
tk["bg"] = BG


def fecharjanela():
    clientsocket.send("sair".encode())
    clientsocket.close()
    tk.quit()


tk.protocol("WM_DELETE_WINDOW", lambda: fecharjanela())

frame0 = Frame(tk, bg=BG)
frame0.place(relx=0, rely=0, relheight=0.33, relwidth=1)
frame1 = Frame(tk, bg=BG)
frame1.place(relx=0, rely=0.33, relheight=0.33, relwidth=1)
frame2 = Frame(tk, bg=BG)
frame2.place(relx=0, rely=0.66, relheight=0.33, relwidth=1)

# chamar primeira tela
tela1()
mainloop()
