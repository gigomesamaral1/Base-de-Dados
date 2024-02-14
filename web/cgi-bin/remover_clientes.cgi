#!/usr/bin/python3

import psycopg2
import cgi
import login

print("Content-type:text/html\r\n\r\n")

connection = None
form = cgi.FieldStorage()

connection = psycopg2.connect(login.credentials)
cursor = connection.cursor()

cust_no = form.getvalue('cust_no')
order_no = form.getvalue('order_no')
try:
    queryDelOrdPrc = 'DELETE FROM process WHERE order_no = %s'
    dataDelOrdPrc = (order_no,)
    cursor.execute(queryDelOrdPrc, dataDelOrdPrc)

    queryDelOrdCtns = 'DELETE FROM contains WHERE order_no = %s'
    dataDelOrdCtns = (order_no,)
    cursor.execute(queryDelOrdCtns, dataDelOrdCtns)

    queryDelOrdOrd = 'DELETE FROM orders WHERE order_no = %s'
    dataDelOrdOrd = (order_no,)
    cursor.execute(queryDelOrdOrd, dataDelOrdOrd)
    
    queryDelOrdPay = 'DELETE FROM pay WHERE order_no = %s'
    dataDelOrdPay = (order_no,)
    cursor.execute(queryDelOrdPay, dataDelOrdPay)
    
    queryDelCust = 'DELETE FROM customer WHERE cust_no = %s'
    dataDelCust = (cust_no,)
    cursor.execute(queryDelCust, dataDelCust)

    connection.commit()
    cursor.close()
    
    
    
except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))


finally:
    if connection is not None:
        connection.close()
        
