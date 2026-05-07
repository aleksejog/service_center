from database.db_manager import get_connection
from datetime import datetime

class Order:
    def __init__(self, id=None, receipt_date=None, status="Принята", master_id=None, client_id=None, equipment_id=None):
        self.id = id
        self.receipt_date = receipt_date
        self.status = status
        self.master_id = master_id
        self.client_id = client_id
        self.equipment_id = equipment_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute(
                "INSERT INTO orders (receipt_date, status, master_id, client_id, equipment_id) VALUES (?, ?, ?, ?, ?)",
                (self.receipt_date, self.status, self.master_id, self.client_id, self.equipment_id)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE orders SET receipt_date = ?, status = ?, master_id = ?, client_id = ?, equipment_id = ? WHERE id = ?",
                (self.receipt_date, self.status, self.master_id, self.client_id, self.equipment_id, self.id)
            )
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM orders WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()

def get_all_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, receipt_date, status, master_id, client_id, equipment_id FROM orders")
    rows = cursor.fetchall()
    conn.close()
    return [Order(id=r[0], receipt_date=r[1], status=r[2], master_id=r[3], client_id=r[4], equipment_id=r[5]) for r in rows]

def get_order_by_id(order_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, receipt_date, status, master_id, client_id, equipment_id FROM orders WHERE id = ?", (order_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Order(id=row[0], receipt_date=row[1], status=row[2], master_id=row[3], client_id=row[4], equipment_id=row[5])
    return None