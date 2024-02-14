#!/usr/bin/python3

import psycopg2
import cgi
import login

print("Content-type:text/html\r\n\r\n")

connection = None

form = cgi.FieldStorage()

nome_produto = form.getvalue('name')
descricao_produto = form.getvalue('description')
preco = form.getvalue('price')
sku = form.getvalue('sku')
ean = form.getvalue('ean')

forn_tin =form.getvalue('TIN')
forn_nome =form.getvalue('nameforn')
forn_morada = form.getvalue('addresss')

try:
    
    connection = psycopg2.connect(login.credentials)
    connection.autocommit = True
    connection.autocommit = False
    cursor = connection.cursor()

    query = """
    INSERT INTO product (name, description, price, sku, ean) 
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nome_produto, descricao_produto, preco, sku, ean))

    queryforn = """
    INSERT INTO supplier (tin, name, address, sku, date)
    VALUES (%s,%s,%s,%s, CURRENT_DATE)
    """
    
    cursor.execute(queryforn, (forn_tin, forn_nome, forn_morada, sku))


    connection.commit()
    cursor.close()


except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(str(e)))


finally:
    if connection is not None:
        connection.close()
        
        
