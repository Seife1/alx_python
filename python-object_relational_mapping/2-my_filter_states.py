"""script that lists all states with
a name given from the database
"""
import MySQLdb
import sys


user = sys.argv
username = user[1]
password = user[2]
db = user[3]
name = user[4]


def main(username, password, db, name):

    mydb = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db, charset="utf8")
    cursor = mydb.cursor()
    query = """ SELECT *
                FROM states
                WHERE name LIKE '{}' COLLATE utf8_bin
                ORDER BY states.id ASC
            """.format(name)
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
if __name__ == "__main__":

    main(username, password, db, name)
