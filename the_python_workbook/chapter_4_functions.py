#exercise 85 (23 strings)
import math

a = int(input(''))
b = int(input(''))

def hypotenuse_length():    
    c = math.sqrt((a**2) + (b**2))
    print('%.2f' %c)

hypotenuse_length()

#exercise 86 (22 strings)
BASE = 4
OVER = 0.25 # 140 meters trip
user_distatnce = int(input('Enter distance trip in km: '))

def total_sum():        
    us_dis_metr = user_distatnce*1000
    over_base = (us_dis_metr/140)*OVER
    total_price = BASE+over_base
    print(f'Your distance is {user_distatnce} km. Total PRICE: ${total_price:.2f}')
total_sum()

#ver 2
BASE = 4
OVER = 0.25 # 140 meters trip

def total_sum():
    user_distatnce = int(input('Enter distance trip in km: '))        
    us_dis_metr = user_distatnce*1000
    over_base = (us_dis_metr/140)*OVER
    total_price = BASE+over_base
    print(f'Your distance is {user_distatnce} km. Total PRICE: ${total_price:.2f}')
total_sum()

#exercise 87 (23 strings)
def all_price():
    number_goods = int(input('Enter number of goods: '))
    total_price = (number_goods - 1)* 2.95 + 10.95
    print(f'Numbers of goods {number_goods}. The amount of goods is: ${total_price:.2f}')
all_price()

#exercise 88 (43 strings)
import statistics

def median_user():
    user_data_list = []
    user_data = input('')
    while user_data != '':        
        user_data_list.append(int(user_data))
        user_data = input('')
    return statistics.median(user_data_list)
median_user()

#exercise 89 (47 strings)
def trans_numder():
    user_num = int(input('Число от 1-го до 10'))
    while 1<=user_num<=10: 
        if user_num == 1:
            return print('Первый')
        elif user_num == 2:
            return print('Второй')
        elif user_num == 3:
            return print('Третий')
        elif user_num == 4:
            return print('Четвертый')
        elif user_num == 5:
            return print('Пятый')
        elif user_num == 6:
            return print('Шестой')
        elif user_num == 7:
            return print('Седьмой')
        elif user_num == 8:
            return print('Восьмой')
        elif user_num == 9:
            return print('Девятый')
        elif user_num == 10:
            return print('Десятый')
        else:
            print('Вы ввели не то число. Попробуйте еще раз')        
        
trans_numder()

