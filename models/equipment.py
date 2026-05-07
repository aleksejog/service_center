from database.db_manager import get_connection

class Equipment:
    def __init__(self, id=None, serial_number=None, model=None, manufacturer=None, client_id=None):
        self.id = id
        self.serial_number = serial_number
        self.model = model
        self.manufacturer = manufacturer
        self.client_id = client_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute(
                "INSERT INTO equipment (serial_number, model, manufacturer, client_id) VALUES (?, ?, ?, ?)",
                (self.serial_number, self.model, self.manufacturer, self.client_id)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE equipment SET serial_number = ?, model = ?, manufacturer = ?, client_id = ? WHERE id = ?",
                (self.serial_number, self.model, self.manufacturer, self.client_id, self.id)
            )
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM equipment WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()

def get_all_equipment():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, serial_number, model, manufacturer, client_id FROM equipment")
    rows = cursor.fetchall()
    conn.close()
    return [Equipment(id=r[0], serial_number=r[1], model=r[2], manufacturer=r[3], client_id=r[4]) for r in rows]

def get_equipment_by_id(eq_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, serial_number, model, manufacturer, client_id FROM equipment WHERE id = ?", (eq_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Equipment(id=row[0], serial_number=row[1], model=row[2], manufacturer=row[3], client_id=row[4])
    return None

def get_equipment_by_client(client_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, serial_number, model, manufacturer, client_id FROM equipment WHERE client_id = ?", (client_id,))
    rows = cursor.fetchall()
    conn.close()
    return [Equipment(id=r[0], serial_number=r[1], model=r[2], manufacturer=r[3], client_id=r[4]) for r in rows]