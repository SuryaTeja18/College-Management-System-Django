import MySQLdb as mdb

db = mdb.connect(host="localhost",user="teja",passwd="1234")

cur = db.cursor()

cur.execute("create database onlinedb")