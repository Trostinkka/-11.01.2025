def show_menu():
    print("\nМеню")
    print("1. Показать данные")
    print("2. Добавить или обновить данные")
    print("3. Удалить данные")
    print("4. Выйти")

def show_data(person):
    print("\nДанные о человеке")
    for key, value in person.items():
        print(f"{key}: {value}")

def add_or_update(person):
    key = input("Введите название поля (например: Имя, Фамилия): ").strip()
    value = input(f"Введите значение для {key}: ").strip()
    person[key] = value
    print(f"Поле {key} обновлено")

def delete_data(person):
    key = input("Введите название поля удаления (например: Имя, Фамилия): ").strip()
    if key in person:
        del person[key]
        print(f"Поле {key} удалено")
    else:
        print(f"Поле {key} не найдено")

def main():
    person = {"Имя": "Саша", 
              "Возвраст": "19",
              "Город": "Москва"}
    
    while True:
        show_menu()
        choice = input("\nВыберите действие (1-4): ")

        if choice == "1":
            show_data(person)
        elif choice == "2":
            add_or_update(person)
        elif choice == "3":
            delete_data(person)
        elif choice == "4":
            print("Выход из приложения")
            break
        else:
            print("Неверный выбор попробейте снова")

if __name__ == "__main__":
    main() 

