from models.order import Order, get_all_orders
from models.client import get_all_clients, get_client_by_id
from models.equipment import get_equipment_by_client, get_equipment_by_id
from database.db_manager import get_all_masters
from datetime import datetime

STATUSES = ["В работе", "Готово", "Закрыта"]

def menu_orders():
    while True:
        print("\n=== Заявки ===")
        print("1. Показать все заявки")
        print("2. Добавить заявку")
        print("3. Изменить статус заявки")
        print("4. Удалить заявку")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            orders = get_all_orders()
            print("\nСписок заявок:")
            for o in orders:
                client = get_client_by_id(o.client_id)
                equipment = get_equipment_by_id(o.equipment_id)
                client_name = client.name if client else "—"
                equipment_model = equipment.model if equipment else "—"

                masters = get_all_masters()
                master_name = "—"
                for m in masters:
                    if m[0] == o.master_id:
                        master_name = m[1]
                        break

                print(f"{o.id}. Дата: {o.receipt_date} | Статус: {o.status} | Мастер: {master_name} | Клиент: {client_name} | Техника: {equipment_model}")

        elif choice == "2":
            print("\n=== Создание новой заявки ===")
            print("\nДоступные клиенты (ID - Имя):")
            clients = get_all_clients()
            for c in clients:
                print(f"{c.id}. {c.name}")
            client_id = int(input("Введите ID клиента: "))

            print("\nТехника клиента:")
            equipment_list = get_equipment_by_client(client_id)
            if not equipment_list:
                print("У клиента нет зарегистрированной техники. Сначала добавьте технику.")
                continue
            for e in equipment_list:
                print(f"{e.id}. {e.model} (S/N: {e.serial_number})")
            equipment_id = int(input("Введите ID техники: "))

            print("\nДоступные мастера (ID - Имя - Специализация):")
            masters = get_all_masters()
            for m in masters:
                print(f"{m[0]}. {m[1]} ({m[2]})")
            master_id = int(input("Введите ID мастера: "))

            order = Order(
                receipt_date=datetime.now().strftime("%Y-%m-%d"),
                status="В работе",
                master_id=master_id,
                client_id=client_id,
                equipment_id=equipment_id
            )
            order.save()
            print("Заявка создана.")

        elif choice == "3":
            id_to_edit = int(input("Введите ID заявки для изменения статуса: "))
            orders = get_all_orders()
            current = next((o for o in orders if o.id == id_to_edit), None)
            if not current:
                print("Заявка не найдена!")
                continue
            print(f"\nТекущий статус: {current.status}")
            print("Доступные статусы:")
            for i, s in enumerate(STATUSES, 1):
                print(f"{i}. {s}")
            st_choice = int(input("Выберите новый статус (1-3): "))
            if 1 <= st_choice <= 3:
                current.status = STATUSES[st_choice - 1]
                current.save()
                print("Статус обновлён.")
            else:
                print("Неверный выбор статуса.")

        elif choice == "4":
            id_to_delete = input("Введите ID заявки для удаления: ")
            order = Order(id=int(id_to_delete))
            order.delete()
            print("Заявка удалена.")

        elif choice == "0":
            break
        else:
            print("Неверный ввод.")