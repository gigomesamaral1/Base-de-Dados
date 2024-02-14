#!/usr/bin/python3

import psycopg2
import cgi
import login

print("Content-type:text/html\r\n\r\n")


connection = None
form = cgi.FieldStorage()

try:
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()
    tin = form.getvalue('tin')
    

    queryDelDelivery = 'DELETE FROM delivery WHERE TIN = %s'
    dataDelDelivery = (tin,)
    cursor.execute(queryDelDelivery, dataDelDelivery)
    
    queryDelSup = 'DELETE FROM supplier WHERE tin = %s'
    dataDelSup = (tin,)
    cursor.execute(queryDelSup, dataDelSup)


    connection.commit()
    cursor.close()
    
except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))


finally:
    if connection is not None:
        connection.close()
        