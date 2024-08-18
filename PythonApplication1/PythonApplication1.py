
num_of_cards = int(input("Количество видеокарт: "))

# Ввод списка видеокарт
cards = []
for i in range(num_of_cards):
    card = int(input(f"Видеокарта {i + 1}: "))
    cards.append(card)

# Вывод старого списка видеокарт
print(f"Старый список видеокарт: {cards}")

# Нахождение максимального значения
max_card = max(cards)

# Создание нового списка без максимальных значений
new_cards = [card for card in cards if card != max_card]

# Вывод нового списка видеокарт
print(f"Новый список видеокарт: {new_cards}")