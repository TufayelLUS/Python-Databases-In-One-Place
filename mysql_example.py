import pymysql


host = "localhost"
dbname = "django-db"
user = "root"
password = ""


def createTable():
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=dbname)

    # create table operation
    try:
        with conn.cursor() as curs:
            drop_query = "DROP TABLE IF EXISTS users;"
            curs.execute(drop_query)
            
            create_query = """
CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255),
    is_admin INT
);
"""
            curs.execute(create_query)
            conn.commit()
            print("Table created successfully!")
    except Exception as e:
        print(str(e))
    finally:
        conn.close()


def insertData():
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=dbname)
    # insert operation
    try:
        with conn.cursor() as curs:
            insert_query = "INSERT INTO users (username, password, is_admin) VALUES (%s, %s, %s)"
            values = ("admin", "admin123", 1)
            curs.execute(insert_query, values)
            conn.commit()
            print("Data inserted successfully!")
    except Exception as e:
        print(str(e))
    finally:
        conn.close()


def readData():
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=dbname)
    # select operation
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as curs:
            select_query = "SELECT * FROM users"
            curs.execute(select_query)
            result = curs.fetchall()
            for row in result:
                print(row['username'])
                print(row['password'])
    except Exception as e:
        print(str(e))
    finally:
        conn.close()


def updateData():
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=dbname)
    # update operation
    try:
        with conn.cursor() as curs:
            update_query = "UPDATE users SET password = %s WHERE username = %s"
            values = ("newpassword", "admin")
            curs.execute(update_query, values)
            conn.commit()
            print("Data updated successfully!")
    except Exception as e:
        print(str(e))
    finally:
        conn.close()


def deleteData():
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=dbname)
    # delete operation
    try:
        with conn.cursor() as curs:
            delete_query = "DELETE FROM users WHERE username = %s"
            values = ("admin",)
            curs.execute(delete_query, values)
            conn.commit()
            print("Data deleted successfully!")
    except Exception as e:
        print(str(e))
    finally:
        conn.close()


if __name__ == "__main__":
    createTable()
    insertData()
    readData()
    updateData()
    deleteData()
