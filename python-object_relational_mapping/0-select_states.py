"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb

mydb = MySQLdb.connect(host="localhost", port=3306, user="alx", passwd="ALXmfBright", db="hbtn_0e_0_usa", charset="utf-8")
cursor = mydb.cursor()

if __name__ == '__main__':
    cursor.execute("SELECT * FROM states ORDER BY states.id")