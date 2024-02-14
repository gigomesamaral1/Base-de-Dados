#!/usr/bin/python3

import psycopg2
import cgi
import login

print("Content-type:text/html\r\n\r\n")

connection = None

form = cgi.FieldStorage()


connection = psycopg2.connect(login.credentials)
cursor = connection.cursor()
    
novo_preco = form.getvalue('price')
sku = form.getvalue('sku')

try:
    query = """UPDATE product 
    SET price= %s 
    WHERE sku= %s
    """
    cursor.execute(query, (novo_preco, sku))
    
    connection.commit()
    cursor.close()
    
except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
    
finally:
    if connection is not None:
        connection.close()
        
