#!/usr/bin/python3

import psycopg2
import cgi
import login

print("Content-type:text/html\r\n\r\n")

connection = None

form = cgi.FieldStorage()

order_noEnc = form.getvalue('order_no')
skuEnc = form.getvalue('sku')
quantidadesProdpoEnc = form.getvalue('quantidades')

try:

    connection = psycopg2.connect(login.credentials)
    connection.autocommit = True
    connection.autocommit = False
    cursor = connection.cursor()

    query = """
    INSERT INTO contains (order_no,sku, qty)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (order_noEnc, skuEnc, quantidadesProdpoEnc))


    connection.commit()
    cursor.close()


except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
    
finally:
    if connection is not None:
        connection.close()