from models.equipment import Equipment, get_all_equipment
from models.client import get_all_clients

def menu_equipment():
    while True:
        print("\n=== Техника ===")
        print("1. Показать всю технику")
        print("2. Добавить технику")
        print("3. Изменить технику")
        print("4. Удалить технику")
        print("0. Назад")
        choice = input("Выберите действие: ")

        if choice == "1":
            items = get_all_equipment()
            print("\nСписок техники:")
            for e in items:
                print(f"{e.id}. S/N: {e.serial_number} | {e.model} | {e.manufacturer} | Клиент ID: {e.client_id}")

        elif choice == "2":
            serial = input("Серийный номер: ")
            model = input("Модель: ")
            manufacturer = input("Производитель: ")
            print("Клиенты:")
            for c in get_all_clients():
                print(f"{c.id}. {c.name}")
            client_id = int(input("ID клиента: "))
            eq = Equipment(serial_number=serial, model=model, manufacturer=manufacturer, client_id=client_id)
            eq.save()
            print("Техника добавлена.")

        elif choice == "3":
            eid = int(input("ID техники: "))
            items = get_all_equipment()
            current = next((e for e in items if e.id == eid), None)
            if not current:
                print("Не найдено!")
                continue
            serial = input(f"Серийный номер ({current.serial_number}): ") or current.serial_number
            model = input(f"Модель ({current.model}): ") or current.model
            manufacturer = input(f"Производитель ({current.manufacturer}): ") or current.manufacturer
            client_id = input(f"ID клиента ({current.client_id}): ") or current.client_id
            eq = Equipment(id=eid, serial_number=serial, model=model, manufacturer=manufacturer, client_id=int(client_id))
            eq.save()
            print("Обновлено.")

        elif choice == "4":
            eid = int(input("ID техники для удаления: "))
            eq = Equipment(id=eid)
            eq.delete()
            print("Удалено.")

        elif choice == "0":
            break
        else:
            print("Неверный ввод.")