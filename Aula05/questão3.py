"""
3.Escrever uma função chamada sed que recebe 4 argumentos: uma string padrão, uma string de
substituição e dois arquivos. O primeiro arquivo deve ser lido e caso a string padrão seja
encontrada, deve ser substituída pela string de substituição e o conteúdo escrito no segundo
arquivo.
"""


def sed(file, file2, str1, str2):
    with open(file, "r+") as f:
        a = f.read()
        if a.count(str1) > 0:
            a = a.replace(str1, str2)
            with open(file2, "r+") as h:
                h.write(a)
            with open(file, "r+") as g:
                with open(file2, "r+") as h:
                    print("cópia:\n", h.read(), "\nfile:\n", g.read())
        else:
            print("string não encontrada")


sed("arquivo.txt", "substituto.txt", "amor", "maracuja")
