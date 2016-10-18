'''

file: bibtex.py
purpose: format data from a MySQL database to the bibtex format
by: Per Thykjaer Jensen

MySQL QQUERY
Based on these notes: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html

'''

import mysql.connector
from mysql.connector import errorcode

# query
query = ("SELECT forfatter, titel, anno, lit_id, udgiver FROM litrev ORDER BY forfatter")

# connect
try:
  cnx = mysql.connector.connect(user='root',password='mojndo', database='litrev')
  cursor = cnx.cursor()

  # the query
  cursor.execute(query)

  # compile to the bibtex format
  for row in cursor:
      print "@book{wp_" + str(row[3]) + ","
      print "author=\"" + row[0] + "\","
      print "publisher=\"" + row[4] + "\","
      print "title=\"" + row[1] + "\","
      print "year=" + str(row[2]) 
      print "}"
      print ""

      cnx.close()
     
  
# error handling
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
