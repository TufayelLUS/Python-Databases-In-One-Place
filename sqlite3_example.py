import sqlite3


database = "django-db.sqlite"


def createTable():
    conn = sqlite3.connect(database)

    # create table operation
    try:
        with conn:
            drop_old_table_query = "DROP TABLE IF EXISTS users;"
            conn.execute(drop_old_table_query)
            create_query = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        is_admin INTEGER
    );
    """
            conn.execute(create_query)
            conn.commit()
            print("Table created successfully!")
    except Exception as e:
        print(str(e))
    finally:
        conn.close()


def insertData():
    conn = sqlite3.connect(database)
    # insert operation
    try:
        with conn:
            insert_query = "INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)"
            values = ("admin", "admin123", 1)
            conn.execute(insert_query, values)
            conn.commit()
            print("Data inserted successfully!")
    except Exception as e:
        print(str(e))
    finally:
        conn.close()


def readData():
    conn = sqlite3.connect(database)
    # select operation
    try:
        with conn:
            select_query = "SELECT * FROM users"
            curs = conn.execute(select_query)
            result = curs.fetchall()
            for row in result:
                print(row[1])  # username
                print(row[2])  # password
    except Exception as e:
        print(str(e))
    finally:
        conn.close()


def updateData():
    conn = sqlite3.connect(database)
    # update operation
    try:
        with conn:
            update_query = "UPDATE users SET password = ? WHERE username = ?"
            values = ("newpassword", "admin")
            conn.execute(update_query, values)
            conn.commit()
            print("Data updated successfully!")
    except Exception as e:
        print(str(e))
    finally:
        conn.close()


def deleteData():
    conn = sqlite3.connect(database)
    # delete operation
    try:
        with conn:
            delete_query = "DELETE FROM users WHERE username = ?"
            values = ("admin",)
            conn.execute(delete_query, values)
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
