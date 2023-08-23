"""script that lists all states
from the database hbtn_0e_0_usa
"""
import MySQLdb


def main(username, password, db):
    
    mydb = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db, charset="utf8")
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)

if __name__ == "__main__":
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    db = input("Enter database name: ")
    main(username, password, db)