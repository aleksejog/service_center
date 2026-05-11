from models.order import Order, get_all_orders
from models.client import get_all_clients
from models.equipment import get_equipment_by_client
from database.db_manager import get_all_masters
from datetime import datetime

STATUSES = ["В работе", "Готова", "Закрыта"]

def menu_orders():
    while True:
        print("\n=== Заявки ===")
        print("1. Показать все заявки")
        print("2. Добавить заявку")
        print("3. Изменить статус заявки")
        print("4. Удалить заявку")
        print("0. Назад")
        choice = input("Выберите действие: ")

        if choice == "1":
            orders = get_all_orders()
            print("\nСписок заявок:")
            for o in orders:
                print(f"{o.id}. Дата: {o.receipt_date} | Статус: {o.status} | Мастер ID: {o.master_id} | Клиент ID: {o.client_id} | Техника ID: {o.equipment_id}")

        elif choice == "2":
            print("Клиенты:")
            clients = get_all_clients()
            for c in clients:
                print(f"{c.id}. {c.name}")
            client_id = int(input("ID клиента: "))

            print("Техника клиента:")
            equipment_list = get_equipment_by_client(client_id)
            for e in equipment_list:
                print(f"{e.id}. {e.model} (S/N: {e.serial_number})")
            equipment_id = int(input("ID техники: "))

            print("Мастера:")
            masters = get_all_masters()
            for m in masters:
                print(f"{m[0]}. {m[1]} ({m[2]})")
            master_id = int(input("ID мастера: "))

            order = Order(
                receipt_date=datetime.now().strftime("%Y-%m-%d"),
                status="Принята",
                master_id=master_id,
                client_id=client_id,
                equipment_id=equipment_id
            )
            order.save()
            print("Заявка создана.")

        elif choice == "3":
            oid = int(input("ID заявки: "))
            orders = get_all_orders()
            current = next((o for o in orders if o.id == oid), None)
            if not current:
                print("Не найдена!")
                continue
            print("Статусы:")
            for i, s in enumerate(STATUSES, 1):
                print(f"{i}. {s}")
            st = int(input(f"Текущий: {current.status}. Новый статус (1-5): "))
            current.status = STATUSES[st-1]
            current.save()
            print("Статус обновлён.")

        elif choice == "4":
            oid = int(input("ID заявки для удаления: "))
            order = Order(id=oid)
            order.delete()
            print("Удалена.")

        elif choice == "0":
            break
        else:
            print("Неверный ввод.")