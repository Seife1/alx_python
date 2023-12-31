"""script that lists all states with
a name starting with N from the database
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
    query = """ SELECT *
                FROM states
                WHERE name LIKE 'N%' COLLATE utf8_bin
                ORDER BY states.id ASC
            """
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
if __name__ == "__main__":

    main(username, password, db)
