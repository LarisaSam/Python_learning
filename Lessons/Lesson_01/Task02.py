# Задание 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

try:
    value: int = int(input("введите время в секундах >>\n"))
    print("{:>02}:{:>02}:{:>02}".format(
        int((value//(60*60))),
        int((value//60%60)),
        int((value%60)))
    )
except:
    print("Вы ввели не корректные данные")