# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
fru = ['Яблоко', 'Банан', 'Киви', 'Арбуз', 'Манго', 'Груша', 'Помидор', 'Дыня']
fru.sort()
for i, item in enumerate(fru):
    print(str(i + 1) + '.' + item)
# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
t2 = [1, 2, 23, 11, 2, 5, 22, 77, 8]
s = []
for i in t2:
       if i not in t:
          s.append(i)
print(max(s))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
first_list = [2, 7, 5, 6, 9, 15, 33, 333, 44444, 4444]
new_list = []
last_name = len(first_list)
for i in range(last_name):
    if first_list[i] % 2 == 0:
        new_list.append(first_list[i] / 5)
    else:
        new_list.append(first_list[i] * 2)
print(new_list[0::2])
