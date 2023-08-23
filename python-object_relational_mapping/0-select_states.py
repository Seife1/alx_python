"""script that lists all states
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


user = sys.argv
username = user[1]
password = user[2]
db = user[3]


def main(username, password, db):

    mydb = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db, charset="utf8")
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)
if __name__ == "__main__":

    main(username, password, db)
