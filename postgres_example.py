import psycopg2
import psycopg2.extras


host = "localhost"
dbname = "django-db"
user = "postgres"
password = "root"


def createTable():
    conn = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password)

    # create table operation
    try:
        with conn:
            with conn.cursor() as curs:
                create_query = """
    DROP table IF EXISTS users;
    CREATE table IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username varchar(255),
        password varchar(255),
        is_admin int
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
    conn = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password)
    # insert operation
    try:
        with conn:
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
    conn = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password)
    # select operation
    try:
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:
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
    conn = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password)
    # update operation
    try:
        with conn:
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
    conn = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password)
    # delete operation
    try:
        with conn:
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
