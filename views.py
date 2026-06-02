import MySQLdb

def get_user(user_id):
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="myapp")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    return cursor.fetchone()

def get_all_users():
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="myapp")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
# test change
# another change
