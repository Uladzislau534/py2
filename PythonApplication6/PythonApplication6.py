# Ввод количества заказов
n = int(input("Введите количество заказов: "))

# Словарь для хранения информации о заказах
orders = {}

# Обработка каждого заказа
for i in range(n):
    order = input(f"{i + 1}-й заказ: ")
    buyer, pizza, quantity = order.split()
    quantity = int(quantity)

    # Если покупатель уже есть в словаре, добавляем данные
    if buyer in orders:
        if pizza in orders[buyer]:
            orders[buyer][pizza] += quantity
        else:
            orders[buyer][pizza] = quantity
    else:
        orders[buyer] = {pizza: quantity}

# Вывод результатов по покупателям в алфавитном порядке
for buyer in sorted(orders):
    print(f"{buyer}:")
    for pizza, quantity in orders[buyer].items():
        print(f"{pizza}: {quantity}")

