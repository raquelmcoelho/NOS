import cgitb
import cgi
import functions
import db_handler

cgitb.enable()
form = cgi.FieldStorage()
atributo = form.getvalue('Produto')

functions.init('Search', "Produtos")
if atributo:

    resultado_busca = db_handler.busca("*", str(atributo))
    if resultado_busca:
        for produto in resultado_busca:

            print(f"""
            <hr>
            <div>
            <p>Código: {produto[0]}</p>
            <p>Categoria: {produto[3]}</p>
            <p>Descrição: {produto[4]}</p>
            <p>Preço: {produto[1]}</p>
            <p>Estoque: {produto[2]}</p>
            </div>
            <hr>""")
    else:
        functions.paragrafo("Nenhum resultado encontrado")

else:
    functions.paragrafo("Você não inseriu nada")

functions.botao("inicial.py", "Voltar")
functions.end()
