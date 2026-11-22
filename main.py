from order import Order

def menu():
    user = input("Ваше имя: ")
    while True:
        print(f"\nПривет, {user}!")
        print("1. Заказать такси")
        print("2. Профиль")
        print("0. Выход")
        choice = input("Выбор: ")

        if choice == "1":
            if not Order.available_cars:
                print("Свободных машин нет.")
            else:
                o = Order(user, input("Откуда: "), input("Куда: "))
                if o.create():
                    print(f"Заказ принят. Машина: {o.car}")
                    input("Нажмите Enter, когда доедете...")
                    o.finish()
                    print("Поездка завершена.")
                else:
                    print("Ошибка заказа.")

        elif choice == "2":
            active = [o for o in Order.all_orders if o.name == user and o.status == "В пути"]
            if active:
                o = active[0]
                print(f"Активный заказ: {o.start} -> {o.end} | {o.car}")
            else:
                print("Активных заказов нет.")
            history = [o for o in Order.all_orders if o.name == user and o.status == "Готово"]
            if history:
                print("История:")
                for trip in history:
                    print(f"{trip.start} -> {trip.end} | {trip.car}")
            else:
                print("История пуста.")
            input("Enter...")

        elif choice == "0":
            break

if __name__ == "__main__":
    menu()