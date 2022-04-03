# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами. 

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число
# Предполагаю, что второе число включительно
i = 0
my_list = range(first_number, second_number + 1)

for number in my_list:
    if number % 3 == 0:
        print(number)
    else:
        var = ()
    i += 1

