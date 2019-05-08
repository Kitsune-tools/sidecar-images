import MySQLdb
import os
import time
import datetime
dt=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
file1 = open("/scripts/post-thaw.log","a+" )
try:
	os.remove('/tmp/freeze_snap.lock')
	time.sleep(2)
except Exception, e:
	print e
try:
	conn = MySQLdb.connect ('localhost' , 'root' , 'password' )
	cur = conn.cursor()
	cur.execute ("select version()")
	data = cur.fetchone()
	file1.write (dt)
	file1.write ("-------------------------------------------\n")
	file1.write ("-------------------------------------------\n")
	file1.write ("\t MySQL version is %s: "%data)
	file1.write ("-------------------------------------------\n")
	file1.write ("-------------------------------------------\n")
	cur.close()
	conn.close()
except:
	file1.write (dt)
	file1.write("\t unable to connect to MySQL server\n")

try:
	file1.write (dt)
	file1.write ("\t executing query to unquiesce the database \n")
	cur.execute ("unlock tables")
	file1.write (dt)
	file1.write ("\t Database is in unquiesce mode now \n")
except:
	file1.write(dt)
	file1.write( "\n unexpected error from MySQL, unable to unlock tables. Please check MySql error logs for more info \n")


