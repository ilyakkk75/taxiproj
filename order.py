class Order:
    available_cars = ["Kia Rio", "Hyundai Solaris", "Skoda Rapid"]
    all_orders = []

    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        self.car = None
        self.status = "Ожидание"

    def create(self):
        if not Order.available_cars:
            return False
        self.car = Order.available_cars.pop(0)
        self.status = "В пути"
        Order.all_orders.append(self)
        return True

    def finish(self):
        if self.status == "В пути":
            self.status = "Готово"
            Order.available_cars.append(self.car)
            return True
        return False