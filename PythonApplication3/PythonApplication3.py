
# Ввод списка
numbers = [1, 4, -3, 0, 10]

# Сортировка вставками
for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    # Перемещаем элементы, которые больше key, на одну позицию вперед
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1
    # Вставляем key в правильную позицию
    numbers[j + 1] = key

# Вывод отсортированного списка
print("Отсортированный список:", numbers)
