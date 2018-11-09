#!/usr/bin/python
# -*- coding: utf-8 -*-

# pour GitHub

import MySQLdb as mdb
import sys

con=mdb.connect(host="localhost",user="philippe",passwd="bitagenou",db="elevage")

cur = con.cursor()
cur.execute("SELECT VERSION()")

ver = cur.fetchone()
    
print("Database version : %s " % ver)
	  

	 # SQL query string

#    	sqlQuery = "describe questions_section"   

    	# Execute the sqlQuery

#    	cur.execute(sqlQuery)
