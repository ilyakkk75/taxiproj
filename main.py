from order import Order
import os

def load_users():
    d = {}
    if os.path.exists("users.txt"):
        with open("users.txt") as f:
            for line in f:
                if ":" in line:
                    n, c = line.strip().split(":")
                    d[n] = int(c)
    return d

def save_users(d):
    with open("users.txt", "w") as f:
        for n, c in d.items():
            f.write(f"{n}:{c}\n")

def load_orders():
    o = []
    if os.path.exists("orders.txt"):
        with open("orders.txt") as f:
            for line in f:
                if "|" in line:
                    n, s, e, c, st = line.strip().split("|")
                    ob = Order(n, s, e)
                    ob.car = c
                    ob.status = st
                    o.append(ob)
    return o

def save_orders(l):
    with open("orders.txt", "w") as f:
        for ob in l:
            f.write(f"{ob.name}|{ob.start}|{ob.end}|{ob.car}|{ob.status}\n")

users_data = load_users()
Order.all_orders = load_orders()
current_user = None

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Таксопарк ===")

        if not current_user:
            print("1. Войти")
            print("2. Регистрация")
            print("0. Выход")
            choice = input("Выбор: ")

            if choice == "1":
                if users_data:
                    print("Выберите пользователя:")
                    u_list = list(users_data.keys())
                    for i, u in enumerate(u_list, 1):
                        print(f"{i}. {u}")
                    sel = input("Номер: ")
                    if sel.isdigit() and 1 <= int(sel) <= len(u_list):
                        current_user = u_list[int(sel) - 1]
            elif choice == "2":
                name = input("Имя: ").strip()
                if name and name not in users_data:
                    users_data[name] = 0
                    save_users(users_data)
            elif choice == "0":
                save_orders(Order.all_orders)
                break
        else:
            print(f"Привет, {current_user}!")
            print("1. Заказать такси")
            print("2. Посмотреть профиль")
            print("3. Сменить пользователя")
            print("0. Выход")
            choice = input("Выбор: ")

            if choice == "1":
                if not Order.available_cars:
                    print("Свободных машин нет.")
                else:
                    o = Order(current_user, input("Откуда: "), input("Куда: "))
                    if o.create():
                        Order.all_orders.append(o)
                        users_data[current_user] += 1
                        save_users(users_data)
                        save_orders(Order.all_orders)
                        print(f"Заказ принят. Машина: {o.car}")
                        input("Нажмите Enter, когда доедете...")
                        o.finish()
                        print("Поездка завершена.")
                    else:
                        print("Ошибка заказа.")
                input("Нажмите Enter...")

            elif choice == "2":
                print(f"Всего заказов: {users_data[current_user]}")
                for trip in Order.all_orders:
                    if trip.name == current_user and trip.status == "Готово":
                        print(f"{trip.start} -> {trip.end} | {trip.car}")
                input("Нажмите Enter...")

            elif choice == "3":
                current_user = None
            elif choice == "0":
                save_orders(Order.all_orders)
                break

if __name__ == "__main__":
    menu()