from flask import Flask
from mysql.connector import connect, Error

app = Flask(__name__)

try:
    with connect(
        host="localhost",
        user="root",
        password="",
        database="online_movie_rating",
    ) as connection:
        print(connection)
        with connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            for db in cursor:
                print(db)
except Error as e:
    print(e)




if __name__ == '__main__':
    app.run()