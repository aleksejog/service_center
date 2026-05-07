import sqlite3
from config import DB_NAME
from datetime import datetime

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Таблица Сотрудники
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        email TEXT
    )
    ''')

    # Таблица Мастера
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS masters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER,
        specialization TEXT,
        FOREIGN KEY (employee_id) REFERENCES employees(id)
    )
    ''')

    # Таблица Клиенты
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        email TEXT
    )
    ''')

    # Таблица Техника
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS equipment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        serial_number TEXT NOT NULL,
        model TEXT,
        manufacturer TEXT,
        client_id INTEGER,
        FOREIGN KEY (client_id) REFERENCES clients(id)
    )
    ''')

    # Таблица Заявки
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        receipt_date TEXT,
        status TEXT DEFAULT 'Принята',
        master_id INTEGER,
        client_id INTEGER,
        equipment_id INTEGER,
        FOREIGN KEY (master_id) REFERENCES masters(id),
        FOREIGN KEY (client_id) REFERENCES clients(id),
        FOREIGN KEY (equipment_id) REFERENCES equipment(id)
    )
    ''')

    # Добавляемs сотрудников
    cursor.execute("SELECT COUNT(*) FROM employees")
    if cursor.fetchone()[0] == 0:
        employees = [
            ("Иванов Иван", "+79001112233", "ivanov@mail.ru"),
            ("Петров Пётр", "+79004445566", "petrov@mail.ru"),
            ("Сидоров Сергей", "+79007778899", "sidorov@mail.ru")
        ]
        cursor.executemany("INSERT INTO employees (name, phone, email) VALUES (?, ?, ?)", employees)

        cursor.execute("SELECT id FROM employees")
        emp_ids = [row[0] for row in cursor.fetchall()]

        masters = [
            (emp_ids[0], "Бытовая техника"),
            (emp_ids[1], "Мобильные устройства"),
            (emp_ids[2], "Компьютеры")
        ]
        cursor.executemany("INSERT INTO masters (employee_id, specialization) VALUES (?, ?)", masters)

    conn.commit()
    conn.close()

def get_all_masters():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT masters.id, employees.name, masters.specialization
    FROM masters
    JOIN employees ON masters.employee_id = employees.id
    ''')
    rows = cursor.fetchall()
    conn.close()
    return rows




    



