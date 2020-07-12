# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

someList = [7, 5, 3, 3, 2]

selector = True
while selector:
    newValue = input("Введите натуральное число. Если вы хотите закончить наберите Домой\n")
    if newValue == "Домой":
        selector = not selector
    else:
        try:
            newValue = int(newValue)
            someList.append(newValue)
            someList.sort(key=int, reverse=True)
            print(f"Новый результат {someList}")
        except:
            print("Вы вводите не натуральное число")
