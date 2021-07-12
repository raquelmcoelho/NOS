#!usr/bin/python

import cgitb, cgi
import functions

cgitb.enable()

functions.init('Sobre', "Sobre")
functions.paragrafo("Site integrado a banco de dados tendo como utilidade o READ da entidade Produto.<br><br>"
                    "Desenvolvido com objetivo de aprendizado de CGI complementado a python, html e css.<br>"
                    "Aqui no lado temos botões de acesso ao site, ou seja, seu menu.<br><br>"
                    "Na aba Produtos você pode pesquisar por atributos como preço, estoque, descrição, categoria e"
                    " código do produto no banco de dados<br><br><br>"
                    "<adress>desenvolvido por @raquelmcoelho</adress>")
functions.end()
