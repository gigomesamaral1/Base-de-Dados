#!/usr/bin/python3

import psycopg2
import cgi
import login

print("Content-type:text/html\r\n\r\n")

connection = None

form = cgi.FieldStorage()


nome_forn = form.getvalue('name')
tin_forn = form.getvalue('tin')
morada_forn = form.getvalue('address')
sku_forn = form.getvalue('sku')
data_forn = form.getvalue('date')


try:

    connection = psycopg2.connect(login.credentials)
    connection.autocommit = True
    connection.autocommit = False
    cursor = connection.cursor()


    query = """
    INSERT INTO supplier (name,tin,address,sku,date)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nome_forn, tin_forn, morada_forn, sku_forn, data_forn))

    connection.commit()
    cursor.close()


except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
    
finally:
    if connection is not None:
        connection.close()
        
