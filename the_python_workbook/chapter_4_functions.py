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
