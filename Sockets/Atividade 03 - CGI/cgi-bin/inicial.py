#!usr/bin/python

import cgitb
import cgi
import functions
import db_handler

cgitb.enable()

functions.init('Coelho', "Produtos")

print("<h1> Pesquise por um produto </h1>")
functions.formulario(['Produto'], "search.py", "(ex: '500', 'bolo', '12.99')")
todos_produtos = db_handler.read_produtos("*")
for produto in todos_produtos:

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

print("</div>")

functions.end()

