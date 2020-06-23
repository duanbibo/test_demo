import sqlite3

ccn=sqlite3.connect('film.sqlite3')
cur=ccn.cursor()
#cur.execute('CREATE TABLE jigou( doctor varchar(24),name INTEGER )')
cur.execute('INSERT INTO jigou values ("duan",000)')
cur.execute('SELECT * FROM jigou')
for i in cur.fetchall():
      print(i)

cur.close()
ccn.commit()
ccn.close()

