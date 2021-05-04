# NO CLIENTE MANUSEAREMOS APENAS UMA CÓPIA DO COFRE FORNECIDA PELO SERVIDOR
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import *
from socket import *
from random import *
from Classes import *
import pickle


# criação socket
clientsocket = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 9999
clientsocket.connect((host, port))
print("cliente conectado")
escolhadetema = 0

# padrões
BG = "#000000"
FG = "#ff6600"
FONT = ("Century Gothic", "12")


# funções para o tkinter
def mudarcor(framename):
    for widget in framename.winfo_children():
        widget["bg"] = BG
        widget["fg"] = FG
    framename["bg"] = BG
    limpaframe(framename)


def mudartema():
    global BG, FG, escolhadetema
    fontes = [("#ff9999", "#000033"), ("#ff0000", "#333333"), ("#99ff66", "#cc0066"), ("#facd05", "#0b4b88"),
              ("#ffffff", "#996633"), ("#ff6600", "#000000")]
    escolha = escolhadetema % len(fontes)
    print("escolha e fonte", escolhadetema, "%", len(fontes), "=",  escolha, fontes[escolha])
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


def labelentry(frame, txt, grid):
    Label(frame, text=txt,  font=FONT, bg=BG, fg=FG).grid(row=grid[0], column=grid[1])
    e = Entry(frame)
    e.grid(row=grid[0], column=grid[1] + 1)
    return e


# início
def tela1():
    Label(frame0, text="Gerenciador de Chaves", font=FONT, bg=BG, fg=FG).grid()
    Button(frame1, text="Vamos começar", font=FONT, bg=FG, fg=BG, command=lambda: tela2()).grid()
    Button(frame2, text="Mudar tema", font=FONT, bg=FG, fg=BG, command=lambda: mudartema()).grid()


# tela de apresentação
def tela2():
    # print(tk.winfo_screenwidth())
    # print(tk.winfo_screenheight())
    limpaframe(frame1)
    limpaframe(frame2)
    txt = """
Aqui é possivel armazenar suas senhas em um lugar seguro
trocar se estiverem fracas
checar sua segurança
criar senhas aleatórias a acessa-las se necessario
"""
    Label(frame1, text=txt, font=FONT, bg=BG, fg=FG).grid()
    Button(frame1, text="ok", font=FONT, bg=FG, fg=BG, command=lambda: tela3()).grid()


# tela de login
def tela3():
    def sair():
        clientsocket.send("sair".encode())
        clientsocket.close()
        tk.quit()
    # limpeza dos frames
    limpaframe(frame1)
    limpaframe(frame2)
    tk.title("Inscrever||Entrar")
    # inserir informações de login
    Label(frame1, text="Para se inscrever ou entrar digite", font=FONT, bg=BG, fg=FG).grid(row=1, columnspan=4)
    nome = labelentry(frame1, "Seu nome:", [2, 0])
    senha = labelentry(frame1, "Sua senha", [3, 0])
    # direcionamento ou para se inscrever ou para entrar
    Button(frame1, text="Inscrever", font=FONT, bg=FG, fg=BG,
           command=lambda: tela4(nome.get().lower(), senha.get().lower())).grid(row=4)
    Button(frame1, text="Entrar", font=FONT, bg=FG, fg=BG,
           command=lambda: tela5(nome.get().lower(), senha.get().lower())).grid(row=5)
    # botão de sair
    Button(frame2, text="sair", font=FONT, bg=FG, fg=BG, command=lambda: sair()).grid(column=0)


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
                objeto = pickle.dumps(client)
                clientsocket.send(objeto)
                resposta = clientsocket.recv(4096)
                print(resposta.decode())
                if resposta.decode() == "Seu cliente foi salvo":
                    # salvar os dados informando em qual cliente salvar
                    clientsocket.send("adddados".encode())
                    bdados = pickle.dumps(dados)
                    clientsocket.send(bdados)
                    objeto1 = pickle.dumps(client)
                    print(client, "sendo enviado")
                    clientsocket.send(objeto1)
                    resposta = clientsocket.recv(4096)
                    print(resposta.decode())
                    # direcionar para a tela de acesso aos próprios dados
                    tela5(nomecliente, senhacliente)

        limpaframe(frame1)
        # aviso sobre os dados
        txt = """
No momento de checar se suas senhas são seguras ou não
precisamos ter dados básicos seus que todos tem acesso (públicos),
Isto para evitar que um hacker que lhe conheça na internet
tenha pistas do que procurar primeiro na sua senha
Por isso vamos evitar essas pistas na hora de criar senhas novas
        """
        messagebox.showinfo("Dados Públicos", txt)
        # pegar dados
        Label(frame1, text="Dados Públicos - (dicas para o hacker)", font=FONT, bg=BG, fg=FG).grid(row=0, columnspan=3)
        entrys = [0, 0, 0, 0, 0]
        txts = ["Data de nascimento", "N° de telefone", "Número importante", "Nome completo", "Nome importante"]
        # criar entrys para cada dado
        for i in range(1, 6):
            entrys[i - 1] = labelentry(frame1, txts[i - 1], [i, 0])

        Button(frame1, text="Continuar", font=FONT, bg=FG, fg=BG,
               command=lambda: continuar()).grid()
        Button(frame2, text="Voltar", font=FONT, bg=FG, fg=BG,
               command=lambda: tela3()).grid()


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
            def deletar2(num, elemento):
                # se o método for 1 ele quer deletar uma senha
                if num == 1:
                    # se elemento for o cofre, ou for vazio ou não estiver no cofre ele interrompe
                    if elemento == "cofre" or elemento == "" or elemento not in client.cofre:
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
                            clientsocket.send("replace".encode())
                            bclient2 = pickle.dumps(client)
                            clientsocket.send(bclient2)
                            txt = clientsocket.recv(4096)
                            print(txt.decode())
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
                        bclient5 = pickle.dumps(client)
                        clientsocket.send(bclient5)
                        txt = clientsocket.recv(4096)
                        print(txt.decode())
                        tela3()
                    # se não volta a tela anterior
                    elif a == 0:
                        tela5(nomecliente, senhacliente)

            def deletar(metodo):
                limpaframe(frame0)
                limpaframe(frame1)
                limpaframe(frame2)
                Label(frame1, text="Qual cadeado você deseja deletar?", font=FONT, bg=BG, fg=FG).grid()
                deletado = Entry(frame1)
                deletado.grid()
                # deletar o cadeado do entry utilizando o método 1 na função deletar2
                Button(frame1, text='deletar', font=FONT, bg=FG, fg=BG,
                       command=lambda: deletar2(metodo, deletado.get())).grid()
                Button(frame1, text="voltar", font=FONT, bg=FG, fg=BG,
                       command=lambda: tela5(nomecliente, senhacliente)).grid()

            def logout():
                # salva cliente
                clientsocket.send("replace".encode())
                bclient3 = pickle.dumps(client)
                clientsocket.send(bclient3)
                txt = clientsocket.recv(4096)
                print(txt.decode())
                # fecha tk e o socket
                clientsocket.send("sair".encode())
                clientsocket.close()
                tk.quit()

            def printdados():
                limpaframe(frame0)
                limpaframe(frame1)
                limpaframe(frame2)
                txt = "Esses são os dados que usamos na hora de checar se suas senhas são seguras ou não:\n"
                txt += str(client.dados)
                Label(frame1, text=txt, font=FONT, bg=BG, fg=FG,).grid()
                Button(frame2, text="voltar", font=FONT, bg=FG, fg=BG,
                       command=lambda: tela5(nomecliente, senhacliente)).grid()

            def add():
                limpaframe(frame1)
                limpaframe(frame2)
                Label(frame1, text="O que você deseja adicionar ou substituir?",  font=FONT, bg=BG, fg=FG)
                addcadeado = labelentry(frame1, "Seu cadeado: ", [0, 0])
                addsenha = labelentry(frame1, "Sua Senha: ", [1, 0])
                # recebe dois valores e ou manda para o troca 3 ou volta para a tela anterior
                Button(frame1, text="adicionar", font=FONT, bg=FG, fg=BG,
                       command=lambda: troca3(addcadeado.get(), addsenha.get())).grid()
                Button(frame2, text="voltar", font=FONT, bg=FG, fg=BG,
                       command=lambda: tela5(nomecliente, senhacliente)).grid()

            #
            # funções do botão check
            #
            def troca3(cadeado3, key2):
                # se chegar aqui é porque a troca é definitiva
                limpaframe(frame1)
                # quando se adiciona uma senha em um cadeado existente ele só substitui a senha
                client.adicionarsenha(cadeado3, key2)
                # salvar o cliente e substituir ele no file json
                clientsocket.send("replace".encode())
                bclient4 = client
                bclientsave = pickle.dumps(bclient4)
                clientsocket.send(bclientsave)
                txt = clientsocket.recv(4096)
                print(txt.decode())
                # voltar a tela de acesso
                tela5(nomecliente, senhacliente)

            def troca2(cadeado2, key):
                limpaframe(frame1)
                # aqui é retornado o nível da senha criada
                nivel, texto = client.checarsenha(key)
                Label(frame1, text=cadeado2 + ":" + key, font=FONT, bg=BG, fg=FG).grid()
                Label(frame1, text=nivel + "\n" + texto, font=FONT, bg=BG, fg=FG).grid()
                # perguntado se quer realmente trocar ou tentar novamente
                Label(frame1, text="Deseja por como a nova senha?", font=FONT, bg=BG, fg=FG).grid()
                # se sim ele realiza a troca mandando para o troca 3
                Button(frame1, text="sim", font=FONT, bg=FG, fg=BG, command=lambda: troca3(cadeado2, key)).grid()
                # se tentar novamente ele manda para a tela de escolhe se cria senha manual ou automático
                Button(frame1, text="tentar novamente", font=FONT, bg=FG, fg=BG, command=lambda: troca(cadeado2)).grid()

            def manual(cadeado1):
                limpaframe(frame1)
                Label(frame1, text="Inserir nova senha:", font=FONT, bg=BG, fg=FG).grid()
                novasenha = Entry(frame1)
                novasenha.grid()
                # manda para o troca2 com uma senha criada manualmente
                Button(frame1, text="avançar", font=FONT, bg=FG, fg=BG,
                       command=lambda: troca2(cadeado1, novasenha.get())).grid()

            def troca(cadeado):
                limpaframe(frame1)
                # escolher se prefere criar a nova senha ou criar automaticamente
                Button(frame1, text="Criar a nova senha", font=FONT, bg=FG, fg=BG,
                       command=lambda: manual(cadeado)).grid()
                # se criar automaticamente ele já manda pro troca dois com uma senha criada de tamanho entre 7 e 12
                Button(frame1, text="Criar automaticamente senha forte", font=FONT, bg=FG, fg=BG,
                       command=lambda: troca2(cadeado, client.criarsenha(randint(7, 12)))).grid()

            def check(cadeadocheck, senhacheck):
                limpaframe(frame1)
                limpaframe(frame2)
                nivel, texto = client.checarsenha(senhacheck)
                # mostrar qual cadeado e qual senha tá checando
                Label(frame1, text=cadeadocheck + ":" + senhacheck, font=FONT, bg=BG, fg=FG).grid()
                # mostrar o nível e o texto que explica o nível
                Label(frame1, text=nivel + "\n" + texto, font=FONT, bg=BG, fg=FG).grid()
                # opção de trocar senha existente depois de receber o feedback
                Button(frame1, text="trocar", font=FONT, bg=FG, fg=BG, command=lambda: troca(cadeadocheck)).grid()
                # retorna pra tela anterior
                Button(frame2, text="voltar", font=FONT, bg=FG, fg=BG,
                       command=lambda: tela5(nomecliente, senhacliente)).grid()

            def definir_metodo(cadeado):
                # retorna um método único para cada botão criado
                return lambda: check(cadeado, client.cofre[cadeado])

            def labelbutton(frame, txtlabel, txtbutton, cadeado, grid):
                # cria um label e um botão do lado
                Label(frame, text=txtlabel, font=FONT, bg=BG, fg=FG).grid(row=grid[0], column=grid[1])
                Button(frame, text=txtbutton, font=FONT, bg=FG, fg=BG,
                       command=definir_metodo(cadeado)).grid(row=grid[0], column=grid[1] + 1)
            #
            # GUI da tela5
            #
            tk.title("Cofre")
            limpaframe(frame0)
            limpaframe(frame1)
            limpaframe(frame2)
            Label(frame0, text="Seja bem vinda %s" % client.user.name, font=FONT, bg=BG, fg=FG).grid()

            # enumerar todas as senhas do cofre e criar um label e um botão para cada uma
            for j2, i2 in enumerate(client.cofre):
                # não criar para o clienteid nem para o nome
                if i2 != "clientid" and i2 != "nome":
                    labelbutton(frame1, "%30s:%35s %15s" % (i2, "", client.cofre[i2]), "check", i2, [j2, 0])

            # botões de manuseio
            Button(frame2, text="Adicionar senha ou substituir senha existente", font=FONT, bg=FG, fg=BG,
                   command=lambda: add()).grid()
            Button(frame2, text="Ver meus dados",  font=FONT, bg=FG, fg=BG,
                   command=lambda: printdados()).grid()
            txtinstrucoes = "\ncadeado: o lugar de onde ele abre, \nsenha: a chave do cadeado"
            Button(frame2, text="Instruções", font=FONT, bg=FG, fg=BG,
                   command=lambda: messagebox.showinfo("instruções", txtinstrucoes)).grid()
            Button(frame2, text="Salvar e sair", font=FONT, bg=FG, fg=BG,
                   command=lambda: logout()).grid()
            Button(frame2, text="Apagar senha", font=FONT, bg=FG, fg=BG,
                   command=lambda: deletar(1)).grid()
            Button(frame2, text="Excluir minha conta",  font=FONT, fg=BG, bg="red",
                   command=lambda: deletar2(0, "")).grid()


# Interface gráfica tkinter
tk = Tk()
tk.title("Key Manager")
tk.geometry("500x600+433+84")
tk.iconbitmap(r"C:\Users\raque\Pictures\chave.png")
tk["bg"] = BG
tk.grid()


def fecharjanela():
    clientsocket.send("sair".encode())
    clientsocket.close()
    tk.quit()


tk.protocol("WM_DELETE_WINDOW", lambda: fecharjanela())

frame0 = Frame(tk, bg=BG)
frame0.grid()
frame1 = Frame(tk, bg=BG)
frame1.grid()
frame2 = Frame(tk, bg=BG)
frame2.grid()

# chamar primeira tela
tela1()
mainloop()

