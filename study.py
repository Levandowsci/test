# n = int(input())
# last_digit = n % 10
# while n != 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit < last_digit:
#             digit = last_digit
#     n //= 10
# if last_digit == 0:
#     print("NO")
# else:
#     print(last_digit)

# for _ in range(3):
#     for _ in range(5):
#         print('*' * 7)

#     print()


# # объявление функции
# def print_digit_sum(num):
    
# def hypotenuse(x, y):
#     from math import hypot
#     return hypot(x, y)

# x = int(input())
# y = int(input())
# print(hypotenuse(x, y))

# объявление функции
# def get_days(month):
#     list_month = [31,28,31,30,31,30,31,31,30,31,30,31]
#     return list_month[month - 1]

# # считываем данные
# num = int(input())

# # вызываем функцию
# print(get_days(num))

# объявление функции
# объявление функции
# def merge(list1, list2):
#     list3 = list1 + list2
#     list3.sort()
#     return list3

# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]

# # вызываем функцию
# print(merge(numbers1, numbers2))


# # объявление функции
# def is_valid_triangle(side1, side2, side3):
#     if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
#         return True
#     else:
#         return False

# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# print(is_valid_triangle(a, b, c))


# объявление функции
# def is_prime(num):
#     if num % 2 == 0 and num > 2 or num == 1:
#         return False
#     for i in range(3, int(num ** 0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     else:
#         return True

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(is_prime(n))

# объявление функции
# def get_next_prime(num):
#     # if num == 1:
#     #     return False    
#     # for i in range(2, int(num ** 0.5) + 1):
#     #     if num % i == 0:
#     #         return False     
#     # return True
#     for i in range(num + 1, num * 2 + 1):
#         if i > 1:
#             for j in range(2, int(i ** 0.5) + 1):
#                 if i % j == 0:
#                     break
#             else:
#                 return i

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_next_prime(n))


# # объявление функции
# def get_month(language, number):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    
#     if language == "ru":
#         return lng_ru[number - 1]
#     else:
#         return lng_en[number - 1]

# # считываем данные
# lan = input()
# num = int(input())

# # вызываем функцию
# print(get_month(lan, num))

# объявление функции
# объявление функции
# def is_pangram(text):
#     if len(set(text.lower().replace(" ", ""))) == 26:
#         return True
#     else:
#         return False
    

# # считываем данные
# text = input()

# # вызываем функцию
# print(is_pangram(text))

for i in range(1, 601):
    print(i)