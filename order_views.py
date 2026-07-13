import MySQLdb

def get_user_orders(user_id, status):
    db = MySQLdb.connect("localhost", "root", "", "shopdb")
    cursor = db.cursor()
    query = "SELECT * FROM orders WHERE user_id=" + str(user_id) + " AND status='" + status + "'"
    cursor.execute(query)
    return cursor.fetchall()

def cancel_order(order_id):
    db = MySQLdb.connect("localhost", "root", "", "shopdb")
    cursor = db.cursor()
    cursor.execute("UPDATE orders SET status='cancelled' WHERE id=" + str(order_id))
    db.commit()
