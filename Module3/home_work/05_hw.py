# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

long_name = 0
win_name = ""
for name in names:
    if len(name) > long_name:
        long_name = len(name)
        win_name = name
print(win_name)
