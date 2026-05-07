from models.client import Client, get_all_clients

def menu_clients():
    while True:
        print("\n=== Клиенты ===")
        print("1. Показать всех клиентов")
        print("2. Добавить клиента")
        print("3. Изменить клиента")
        print("4. Удалить клиента")
        print("0. Назад")
        choice = input("Выберите действие: ")

        if choice == "1":
            clients = get_all_clients()
            print("\nСписок клиентов:")
            for c in clients:
                print(f"{c.id}. {c.name} | {c.phone} | {c.email}")

        elif choice == "2":
            name = input("Имя: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            client = Client(name=name, phone=phone, email=email)
            client.save()
            print("Клиент добавлен.")

        elif choice == "3":
            cid = int(input("ID клиента: "))
            clients = get_all_clients()
            current = next((c for c in clients if c.id == cid), None)
            if not current:
                print("Не найден!")
                continue
            name = input(f"Имя ({current.name}): ") or current.name
            phone = input(f"Телефон ({current.phone}): ") or current.phone
            email = input(f"Email ({current.email}): ") or current.email
            client = Client(id=cid, name=name, phone=phone, email=email)
            client.save()
            print("Обновлено.")

        elif choice == "4":
            cid = int(input("ID клиента для удаления: "))
            client = Client(id=cid)
            client.delete()
            print("Удалён.")

        elif choice == "0":
            break
        else:
            print("Неверный ввод.")