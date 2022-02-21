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

#exercise 90 (52 strings) ПОЛНЫЙ ПИ
##
# Отображаем полный текст песни The Twelve Days of Christmas.
#
from chapter_4_functions import trans_numder

## Отображаем один куплет песни The Twelve Days of Christmas
# @param n – куплет для отображения
# @return (None)
def displayVerse(n):
    print("On the", trans_numder(n), "day of Christmas")
    print("my true love sent to me:")
    if n >= 12:
        print("Twelve drummers drumming,")
    if n >= 11:
        print("Eleven pipers piping,")
    if n >= 10:
        print("Ten lords a–leaping,")
    if n >= 9:
        print("Nine ladies dancing,")
    if n >= 8:
        print("Eight maids a–milking,")
    if n >= 7:
        print("Seven swans a–swimming,")
    if n >= 6:
        print("Six geese a–laying,")
    if n >= 5:
        print("Five golden rings,")
    if n >= 4:
        print("Four calling birds,")
    if n >= 3:
        print("Three French hens,")
    if n >= 2:
        print("Two turtle doves,")
    if n == 1:
        print("A", end=" ")
    else:
        print("And a", end=" ")
print("partridge in a pear tree.")
print()
# Отображаем все 12 куплетов песни
def main():
    for verse in range(1, 13):
        displayVerse(verse)
# Вызываем основную функцию
main()

#exercise 93 (29 strings) ver 1

def str_center():
    s = input('')
    w = int(input(''))      
    if len(s) >= w:
        print(s)
    else:
        print('#'*w)
        ls_new = (w-len(s))//2
        print(' '*ls_new + s)
        print('#'*w)
        #print(ls_new)
    #print(s, type(s))
    #print(w, type(w))

str_center()    

#exercise 93 (29 strings) ver 2
w = 62
def str_center(s, w):
         
    if len(s) >= w:
        return s
    else:
        print('#'*w)        
        return ' '*((w-len(s))//2) + s     
    
def main():
    print(str_center("Alexander Ivanov", w))
    print(str_center("New character", w))
    print(str_center("My ball", w))    
    
main()

#exercise 94 (33 strings)

def triangle(str1, str2, str3):
    print(f'Сторона 1: {str1}, сторона 2: {str2}, сторона {str3}')    
    if str1 and str2 and str3 > 0:   
        if (str1+str2 <= str3) or (str2+str3 <= str1) or (str3+str1 <= str2):        
            print('Not OK')
        else:        
            print('ok')
    else:
        print('False')
def main():
    triangle(3,4,5)  
    triangle(10,10,10) 
    triangle(1,1,5)  
    triangle(-1,0,5)
main()

a = 2
b = 5
res = a+10 if a > b else b+2
print(res)


