from database.db_manager import initialize_db
from ui.menu import show_main_menu
from ui.menu_clients import menu_clients
from ui.menu_equipment import menu_equipment
from ui.menu_orders import menu_orders

def main():
    initialize_db()
    while True:
        choice = show_main_menu()
        if choice == "1":
            menu_clients()
        elif choice == "2":
            menu_equipment()
        elif choice == "3":
            menu_orders()
        elif choice == "0":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    main()