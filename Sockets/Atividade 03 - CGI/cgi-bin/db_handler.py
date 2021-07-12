import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="Raquel",
    password="12345678",
    database="sor"
)

cursor = db.cursor()


def busca(what, atributo):
    try:
        sql = f"""
        SELECT {what}
        FROM sor.produto
        WHERE (codigo = {int(atributo)}
        OR preco = {float(atributo)}
        OR estoque = {int(atributo)})
        """

    except:
        sql = f"""
            SELECT {what}
            FROM sor.produto
            WHERE (categoria LIKE '%{atributo}%' 
            OR descricao LIKE '%{atributo}%'
            )
            """
    cursor.execute(sql)
    return cursor.fetchall()


def read_produtos(what):
    sql = f"""
    SELECT {what}
    FROM sor.produto       
    ORDER BY codigo"""

    cursor.execute(sql)
    return cursor.fetchall()


def read_produto(what, codigo):
    sql = f"""
    SELECT {what}
    FROM sor.produto
    WHERE codigo = %s 
    ORDER BY codigo """

    values = (codigo,)
    cursor.execute(sql, values)
    return cursor.fetchone()


def comprar(codigo):
    sql = """ 
    UPDATE sor.produto
    SET estoque = %s
    WHERE codigo = %s"""

    estoque = read_produto("estoque", codigo)[0]
    estoque -= 1

    values = (estoque, codigo)
    cursor.execute(sql, values)
    db.commit()
