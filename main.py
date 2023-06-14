# # def sq1(x):
#     print(x ** 2)
#
#
# print(sq1(10))
#
# def sq2(x):
#     return x ** 2
#
#
# print(sq2(20))

# def c(x):
#     return x ** 3
#
#
# some_list = [1, 2, 3, 4, 5]
#
# new_list = []
#
# for el in some_list:
#     new_list.append(c(el))
#
# print(new_list)

# def c(x):
#     return x ** 3


# some_list = [1, 2, 3, 4, 5]
# new_list = list(map(lambda x: x ** 2 if x % 2 == 0 else x ** 3, some_list))
# print(new_list)

#def even(a):
#     return a % 2 == 0


# some_list = [1, 2, 3, 4, 5]

# new_list = list(filter(lambda a: a % 2 == 0, some_list))
# print(new_list)

# import random
#
# some_list = []
# for _ in range(100):  # 0, 1, 2, 3, 4, 5, 6, 7... 99
#     number = random.randint(1, 10)
#     if number % 2 == 0:
#         some_list.append(number)
#
#
# some_list = [random.randint(1, 10) for _ in range(100)]
#
# some_list = [int(input()) for _ in range(int(input()))]

#orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def s(x):
#     if x[0] == x[1]:
#         return 0
#     return x[0] * x[1]

# mult = list(map(s, orbits))
# print(mult)
# maxx = mult.index(max(mult))
# print(orbits[maxx])

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# print(list(filter(lambda y: y[0] * y[1] == max(list(map(lambda x: x[0] * x[1] if x[0] != x[1] else 0, orbits))), orbits))[0])

#Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
#     print(‘same’)
# else:
#     print(‘different’)
#
# def same_by(characteristic, objects):
#     new_objects = list(filter(characteristic, objects))
#     if len(objects) == len(new_objects) or len(new_objects) == 0:
#         return True
#     return False
    

# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

#Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не 
# настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного 
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в 
# порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#    **Вывод:** Парам пам-пам  

'''
sentense = input('Введите фразу для проверки: ') +' '
list = [] 
count = 0
for el in sentense:
    if el not in ' ' and el in 'а':
        count = count + 1
    elif el in ' ':
        list.append(count)
        count = 0
print(list)
if len(set(list)) == 1:
        print('Парам пам-пам')
else: 
    print('Пам парам')
'''
#Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает
#  в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и 
# num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией 
# называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.    
# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

'''
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        print()
        for j in range(1, num_columns+1):
            print(operation(i,j), end=' ')

print_operation_table(lambda x, y: x*y, 6, 6)
'''