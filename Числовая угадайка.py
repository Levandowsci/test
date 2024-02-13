from random import randint

def is_valid(user_num):
    if user_num.isdigit() and 1 <= int(user_num) <= 100:
        return True
    else:
        return False
    

right_border = input("Добро пожаловать в числовую угадайку, введите границу: ")

rand_num = randint(1, int(right_border))

user_num = ""
numbers_of_attempts = 0

while user_num != rand_num:
    user_num = input("Введите число от 1 до " + right_border + ": ")
    if is_valid(user_num):
        if int(user_num) > rand_num:
            print("Ваше число больше загаданного, попробуйте еще разок")
            numbers_of_attempts += 1
        elif int(user_num) < rand_num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            numbers_of_attempts += 1
        else:
            print("Вы угадали, поздравляем!")
            print("Количество попыток:", numbers_of_attempts)
            break
            
            
new_game = input("Хотите сыграть еще раз? (да/нет) ").lower()
            
while new_game not in ["да", "нет"]:
    if new_game == "да":
        print("check")
    elif new_game == "нет":
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
        break
    else:
        print("Нужно ввести 'да' или 'нет'")


        print("Нужно ввести целое число от 1 до", right_border)
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")


