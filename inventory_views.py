from django.http import JsonResponse
from django.contrib.auth.models import User
import MySQLdb

def get_inventory(request, warehouse_id):
    db = MySQLdb.connect("localhost", "root", "", "inventorydb")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM inventory WHERE warehouse_id=" + str(warehouse_id))
    items = cursor.fetchall()
    return JsonResponse({"items": items})

def update_stock(request, item_id, quantity):
    db = MySQLdb.connect("localhost", "root", "", "inventorydb")
    cursor = db.cursor()
    cursor.execute("UPDATE inventory SET quantity=" + str(quantity) + " WHERE id=" + str(item_id))
    db.commit()
    return JsonResponse({"status": "updated"})

def delete_item(request, item_id):
    user = User.objects.get(id=request.user.id)
    db = MySQLdb.connect("localhost", "root", "", "inventorydb")
    cursor = db.cursor()
    cursor.execute("DELETE FROM inventory WHERE id=" + str(item_id))
    db.commit()
    return JsonResponse({"status": "deleted"})
