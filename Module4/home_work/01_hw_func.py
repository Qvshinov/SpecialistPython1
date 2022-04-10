# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    lst = list(str(ticket_number))
    if len(lst) == 6:
        summa1 = int(lst[0]) + int(lst[1]) + int(lst[2])
        summa2 = int(lst[3]) + int(lst[4]) + int(lst[5])
        return summa1 == summa2


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
