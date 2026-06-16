import MySQLdb

def get_orders(user_id):
    db = MySQLdb.connect("localhost", "root", "", "shop")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM orders WHERE user_id=" + str(user_id))
    return cursor.fetchall()

def delete_user(user_id):
    db = MySQLdb.connect("localhost", "root", "", "shop")
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id=" + str(user_id))
    db.commit()
