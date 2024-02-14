#!/usr/bin/python3

import psycopg2
import cgi
import login

print("Content-type:text/html\r\n\r\n")

connection = None

form = cgi.FieldStorage()


nome_client = form.getvalue('name')
email_client = form.getvalue('email')
tel_client = form.getvalue('phone')
morada_client = form.getvalue('address')
num_client = form.getvalue('cust_no')
    
try:

    connection = psycopg2.connect(login.credentials)
    connection.autocommit = True
    connection.autocommit = False
    cursor = connection.cursor()

    query = """
    INSERT INTO customer (name,email,phone,address,cust_no) 
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (nome_client, email_client, tel_client, morada_client, num_client))
    
    connection.commit()
    cursor.close()
    
except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
    
finally:
    if connection is not None:
        connection.close()
