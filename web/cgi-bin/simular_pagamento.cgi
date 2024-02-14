#!/usr/bin/python3

import psycopg2
import cgi
import login

print("Content-type:text/html\r\n\r\n")

form = cgi.FieldStorage()
connection = None

connection = psycopg2.connect(login.credentials)
cursor = connection.cursor()

num_client = form.getvalue('cust_no')
num_encomenda = form.getvalue('order_no')

try:

    query = """INSERT INTO pay (order_no, cust_no) 
    VALUES (%s, %s)
    """
    cursor.execute(query, (num_encomenda,num_client))
    
    connection.commit()
    cursor.close()
    
    
except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
    
finally:
    if connection is not None:
        connection.close()
