"""Write a script that lists all cities
selected country from the database """
import MySQLdb
import sys


args = sys.argv


def main(username, pw, db, state):

    mydb = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=pw, db=db, charset="utf8")
    cursor = mydb.cursor()
    query = """ SELECT cities.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC
            """

    cursor.execute(query, (state,))

    response = cursor.fetchall()
    # Extract city names from the response
    city_names = [row[0] for row in response]

    # Print city names, separated by commas
    print(', '.join(city_names))

if __name__ == "__main__":
    username = args[1]
    pw = args[2]
    db = args[3]
    state = args[4]

    main(username, pw, db, state)
