# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.
import random
number = int(input("Введите число элементов списка: "))
my_list = [random.randint(-100, 100) for _ in range(number)]
print(my_list)
print(sum([e for e in my_list if (e > 0 and e % 2 == 0)]))
