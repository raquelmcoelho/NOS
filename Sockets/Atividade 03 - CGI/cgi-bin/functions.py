def init(title, page_ativa):
    if page_ativa == "Sobre":
        page_ativa = """
        <li><a href="../index.html">Home</a></li>
        <li><a class="active" href="sobre.py">Sobre</a></li>
        <li><a href="inicial.py">Produtos</a></li>"""

    elif page_ativa == "Produtos":
        page_ativa = """
        <li><a  href="../index.html">Home</a></li>
        <li><a href="sobre.py">Sobre</a></li>
        <li><a class="active" href="inicial.py">Produtos</a></li>"""

    print(f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <link rel="stylesheet" href="../style.css">
        <title>{title}</title>
    </head>
    <body>
    
    <ul>
        {page_ativa}
    </ul>
    
    <div style="margin-left:25%;padding:1px 16px;height:700px; background: white">""")


def header(content):
    print(f"""<header>{content}</header>""")


def formulario(whats, where, placeholder):
    print(f"""
    <div> 
    <form action="{where}" method="post">
    """)

    for what in whats:
        print(f"""
        <label for="{what}"></label>
        <input type="text" placeholder="{placeholder}" id="{what}" name="{what}">
        """)

    print("""<button type="submit">Ir</button></form></div>""")


def paragrafo(content):
    print(f"<p style='font-size:1.5em; text-align: left;'>{content}</p><br>")


def botao(where, text):
    print(
        f"""<button><a href="{where}">{text}</a></button>"""
    )


def footer(content):
    print(f"""<footer>{content}</footer>""")


def end():
    print("""
    </div>
    </body>
    </html>
    """)
