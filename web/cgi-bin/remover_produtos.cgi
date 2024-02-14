#!/usr/bin/python3

import psycopg2
import cgi
import login

print("Content-type:text/html\r\n\r\n")

connection = None

form = cgi.FieldStorage()
sku = form.getvalue('sku')
    
try:

    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    queryDelCot = 'DELETE FROM contains WHERE sku = %s'
    cursor.execute(queryDelCot, (sku,))
    
    queryDelSupp = 'DELETE FROM supplier WHERE sku = %s'
    cursor.execute(queryDelSupp, (sku,))
    
    queryDelProd = 'DELETE FROM product WHERE sku = %s'
    cursor.execute(queryDelProd, (sku,))
    
    connection.commit()
    cursor.close()
    

except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))


finally:
    if connection is not None:
        connection.close()
        
