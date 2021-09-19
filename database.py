import pymysql


class Database:
    def connect(self):
        # return pymysql.connect("phonebook-mysql", "dev", "dev", "crud_flask")

        return pymysql.connect(host="localhost", user="root", password="", database="online_movie_rating", charset='utf8mb4')

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM movie_name")
            else:
                cursor.execute("SELECT * FROM movie_name where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return "not found"
        finally:
            con.close()

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO movie_name(name, rating) VALUES(%s, %s)",
                           (data['name'], data['rating'],))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
