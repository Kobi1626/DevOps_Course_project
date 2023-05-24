# Import nesssary modules
from datetime import datetime
import pymysql


######## Establishes a connection to the database with cursor. ########
def connect():
    global conn, cursor  # Access the global variables.
    try:
        conn = pymysql.connect(
            host='sql12.freemysqlhosting.net',
            port=3306,
            user='sql12620885',
            passwd='qrZrbytYKy',
            db='sql12620885'
        )
        conn.autocommit(True)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        return "Connection established !"
    except Exception as e:
        return "an error occurred" + str(e)


######## Closes the connection and cursor as once. ########
def close_connection():
    global conn, cursor
    cursor.close()
    conn.close()


######## Executes the given SQL query and returns the result based on the fetch method. ########
def run_query(sql_query, params=None, fetch_method='one'):
    global cursor
    try:
        cursor.execute(sql_query, params)
        if fetch_method == 'one':
            return cursor.fetchone()
        else:
            return cursor.fetchall()
    except Exception as e:
        return "an error occurred" + str(e)


######## Adds a new user to the database. ########
def add_user(user_id, user_name):
    now = datetime.now()  # Get the current timestamp.
    sql_query = f"INSERT INTO users (user_id,user_name,creation_date)" + "\n" + f"VALUES (%s,%s,%s)"
    val = (int(user_id), user_name, now.strftime("%d/%m/%Y %H:%M"))
    Result = run_query(sql_query, val)
    if "error" not in str(Result):
        return "User has been added successfully"
    else:
        return "an error occurred: " + Result


######## Retrieves the user name associated with the given user ID. ########
def get_user_name_by_user_id(user_id):
    sql_query = "SELECT user_name FROM users WHERE user_id = '%d'"
    result = run_query(sql_query % int(
        user_id))
    if result:
        return result['user_name']
    else:
        return "user_id doesn't exist"


######## Retrieves all the rows from the "users" table. ########
def select_all_from_table():
    sql_query = "SELECT * FROM users"
    userlist = run_query(sql_query, fetch_method='all')
    for user in userlist:
        print(user)


######## Updates the user name for the specified user ID. ########
def update_username(user_id, new_user_name):
    sql_query = "UPDATE users SET user_name=%s WHERE user_id='%s'"
    try:
        run_query(
            sql_query % (new_user_name, int(user_id)))
        return "user_name updated successfully"
    except Exception as e:
        return "an error occurred" + str(e)


######## Deletes the user with the specified user ID from the database. ########
def delete_user(user_id):
    sql_query = "Delete from users WHERE user_id='%s'"  # SQL query to delete a user.
    try:
        run_query(sql_query % user_id)
        return "User deleted successfully"
    except Exception as e:
        return "an error occurred" + str(e)


######## Creates the "users" table if it doesn't already exist in the database. ########
def create_table_if_not_exists():
    sql_query = (
        "CREATE TABLE IF NOT EXISTS users ("
        "user_id INT PRIMARY KEY, "
        "user_name VARCHAR(50) NOT NULL, "
        "creation_date VARCHAR(50) NOT NULL"
        ")"
    )  # SQL query to create the "users" table
    try:
        run_query(sql_query)
        return "Table created successfully or already exists"
    except Exception as e:
        return "An error occurred while creating the table: " + str(e)


def main():
    ################### Main functions ###################
    connect()  # Creating a Connection to the DB
    create_table_if_not_exists()  # Creating table if it doesn't exist

    ################### RunQuereis for Tests ###################
    # user_id = 1001
    # query = "SELECT user_name FROM users WHERE user_id = %s"
    # result = run_query(query, (user_id,))

    ################### All Functions Tests #################
    # User = add_user("1037","TestUser")
    # User = get_user_name_by_user_id(1010)
    # select_all_from_table()
    # print(User)


main()  # Loading Main Functions when Importing Python

# if __name__ == "__main__":
#      main()