import sys
import xml.dom.minidom
import re
import mysql.connector
import csv

document = xml.dom.minidom.parse(sys.argv[1])
tableElements = document.getElementsByTagName('table')

print ("exchange,symbol,company,volume,price,change")
trElements = tableElements[2].getElementsByTagName('tr')
for tr in trElements[1:]:
    data = []
    for a in tr.getElementsByTagName('a'):
        for node in a.childNodes:
            if node.nodeType == node.TEXT_NODE:
                start = (node.nodeValue).find( '(' )
                end =(node.nodeValue).find( ')' )
                if start != -1 and end != -1:
                      result = (node.nodeValue)[start+1:end]
                data.append("NYSE")
                data.append(result)
            if node.nodeType == node.TEXT_NODE:
                start = (node.nodeValue).find( '' )
                end =(node.nodeValue).find( '(' )
                if start != -1 and end != -1:
                      result = (node.nodeValue)[start:end-1]
                data.append(result)    
    tdElements = []
    for td in tr.getElementsByTagName('td'):
        for node in td.childNodes:
            tdElements.append(node)
    for node in tdElements[1:-1]:            
        if node.nodeType == node.TEXT_NODE:
            if node.nodeValue == '\n':
                continue
            elif node.nodeValue != '\n':
                node.nodeValue = re.sub('[!,@#$]', '', node.nodeValue)
                data.append(node.nodeValue)
                
    print(','.join(data))



# Open database connection
cnx = mysql.connector.connect(host='localhost',
    user='root',
    passwd='henil202',
    db='demo')
cursor = cnx.cursor()


# prepare a cursor object using cursor() method
cnx.commit()

# Drop table if it already exist using execute() method.
cursor.execute("DROP DATABASE IF EXISTS demo;")

cursor.execute("CREATE DATABASE demo;")

cursor.execute("USE demo;")


# Create table as per requirement


sql = """CREATE TABLE cs288(
    exchange VARCHAR(10),
    symbol VARCHAR(20),
    company VARCHAR(50),
    volume VARCHAR(50),
    price VARCHAR(50),
    change1 VARCHAR(50)
    );"""

cursor.execute(sql)

h=sys.argv[2]

cr = csv.reader(open(h, 'rb'))
i = 1
cr.next()
for row in cr:
    print row
    cursor.execute('INSERT INTO cs288 VALUES (%s,%s,%s,%s,%s,%s)', row )
    cnx.commit()
    i=i+1

# disconnect from server
cnx.close()