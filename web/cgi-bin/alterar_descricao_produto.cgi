#!/usr/bin/python3

import psycopg2
import cgi
import login

print("Content-type:text/html\r\n\r\n")

connection = None

form = cgi.FieldStorage()

connection = psycopg2.connect(login.credentials)
cursor = connection.cursor()
    
nova_descricao = form.getvalue('description')
sku =form.getvalue('sku')

try:
    query = """UPDATE product 
    SET description=%s 
    WHERE sku= %s
    """
    cursor.execute(query, (nova_descricao,sku))
    
    connection.commit()
    cursor.close()
    
except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
    
finally:
    if connection is not None:
        connection.close()
