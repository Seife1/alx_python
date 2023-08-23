"""Write a script that lists all cities from the database """
import MySQLdb
import sys


args = sys.argv


def main(username, pw, db):

    mydb = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=pw, db=db, charset="utf8")
    cursor = mydb.cursor()
    query = """ SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC
            """

    cursor.execute(query)

    response = cursor.fetchall()
    for row in response:
        print(row)

if __name__ == "__main__":
    username = args[1]
    pw = args[2]
    db = args[3]

    main(username, pw, db)
