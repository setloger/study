# ex1
a = print('Ivanov Ivan Ivanovich')
b = print('Chapaeva, 10')
с = print('Ф.И.О. - %s и МОЙ АДРЕС %s' %(a, b))

# ex2
c2 = input('Введите имя ')
d2 = print('Привет, %s' %c2)
d3 = print('Привет, {}'.format(c2))

# ex3
l = float(input('Введите длину комнаты в метрах: '))
w = float(input('Введите ширину комнаты в метрах: '))
s_float = l * w 
print('Площадь комнаты составила: %.2f м.' %s_float)

# ex4
l = float(input('Введите длину комнаты в футах: '))
w = float(input('Введите ширину комнаты в футах: '))
acr = 43560
s_site = l * w
s_site_acr = s_site / acr 
print('Площадь садового участка составила: %.2f кв. ф., что равняется - %.2f кв.акр' %(s_site, s_site_acr))

# ex5
amount_less_liter = float(input('Введите количество бутылок меньше литра: '))
amount_more_liter = float(input('Введите количество бутылок больше литра: '))
price_less_liter = 0.10
price_more_liter = 0.25

price_less_liter = amount_less_liter * price_less_liter 
price_more_liter = amount_more_liter * price_more_liter
all_price = price_less_liter + price_more_liter

print('Общая сумма за бутылки составит:')
print('->> бутылки до 1 литра, кол-во - %i, стоимость - $%.2f'%(amount_less_liter, price_less_liter))
print('->> бутылки свыше 1 литра, кол-во - %i, стоимость - $%.2f'%(amount_more_liter, price_more_liter))
print('->> Общая сумма за общее кол-во бутылок - $%.2f' %(all_price))

# ex 6
sum_order = float(input('Введите сумму заказа для расчета: '))
tax = 0.2
tips = 0.18
sum_tax = sum_order * tax
sum_tips = sum_order * tips
all_sum_order = sum_order + sum_tax + sum_tips
print('\tИТОГО ПО ЗАКАЗУ:\n \tсумма заказа - $%.2f \n \tналог - $%.2f \n \tчаевые - $%.2f \n --------------------------- \n \tИТОГО: $%.2f' %(sum_order, sum_tax, sum_tips, all_sum_order))

# ex 7
n = int(input('Введите натуральное целое число: '))
sum = int(((n)*(n+1)) / 2)
print('Сумма первых {} натуральных чисел = {}'.format(n, sum))

# ex 8
souvenir_data_input = int(input('Введите кол-во сувениров: '))
bauble_data_input = int(input('Введите кол-во безделушек: '))
weight_souvenir = 75
weight_bauble = 112
all_weight_souvenir = souvenir_data_input * weight_souvenir
all_weight_bauble = bauble_data_input * weight_bauble
all_weight = all_weight_souvenir + all_weight_bauble

print('Общий вес посылки составил: {} гр.'.format(all_weight))

# ex 9

deposit = float(input('Введите сумму депозита $: '))
annual_percentage = 0.04
first_year_summ = float(deposit * (1+annual_percentage))
second_year_summ = float(first_year_summ * (1+annual_percentage))
third_year_summ = float(second_year_summ * (1+annual_percentage))

print('Ваша сумма депозита с учетом процентов на конец 3-го года составила: $ %.2f '%third_year_summ)

# ex 10

import math 
a = int(input())
b = int(input())
sum_a_b = print(a+b)
minus_a_b = print(a-b)
pr_a_b = print(a*b)
ch_a_b = print(a//b)
ost_a_b = print(a%b)
math.log10(a)
stp_a_b = print(a**b)
# ex 11

mpg = float(input('Введите расход топлива для США: '))
lpk = (100*3.785) / (mpg*1.609)
print('Расход (л/100км) %.2f' %lpk)

# ex 12
import math
dot_t1 = math.radians(int(input('Координаты первой точки, широта: ')))
dot_g1 = math.radians(int(input('Координаты первой точки, долгота: ')))
dot_t2 = math.radians(int(input('Координаты второй точки, широта: ')))
dot_g2 = math.radians(int(input('Координаты второй точки, долгота: ')))

distance = 6371.01 * (math.acos(math.sin(dot_t1)*math.sin(dot_t2) + math.cos(dot_t1)*math.cos(dot_t2)*math.cos(dot_g1-dot_g2)))
print(distance)

#ex 13

# ex 14
heigt_f = int(input('Введите рост в футах: '))
heigt_d = int(input('Введите рост в дюймах: '))
p_f = heigt_f * 12
height_cm = (p_f + heigt_d)*2.54
print('Ваш рост составляет %.2f см.' %height_cm)

#ex 15

ras = int(input('Введите расстояние: '))
DY = 12
YARD = 0.333333
MILS = 0.000189394
ras_d = ras*DY
ras_ya = ras*YARD
ras_ml = ras*MILS
print('Расстояние в %.0f футов, равняется %.0f дюймам, %.4f ярдам, %.4f милям.' %(ras, ras_d, ras_ya, ras_ml))

#ex 16
import math
r = int(input('Введите радиус круга: '))
area = math.pi * r**2
volume = 4/3*math.pi*r**3
print('Площадь круга: %.2f, радиусом %.0f, объем шара: %.2f' %(area, r, volume))

#ex 17

#ex 18
import math
r = int(input('Введите радиус цилиндра: '))
h = int(input('Введите высоту цилиндра: '))
area = math.pi * r**2
volume = area * h
print('Площадь цилиндра: %.2f, радиусом %.2f и высотой %.2f объем цилиндра: %.1f' %(area, r, h, volume))

#ex 19
import math
h = int(input('Высота: '))
A = 9.8
speed = math.sqrt(2*A*h)
print(speed)

#ex 20

#ex 21
b = int(input('Введите длину основания: '))
h = int(input('Введите высоту: '))
area = b*h/2
print('Длина основания %.2f треугольника, высота треугольника %.2f, площадь треугольника %.2f.' %(b, h, area))

#ex 22
import math
s1 = int(input('Введите длину стороны № 1: '))
s2 = int(input('Введите длину стороны № 2: '))
s3 = int(input('Введите длину стороны № 3: '))
s = (s1+s2+s3)/2
area = math.sqrt(s*(s - s1)*(s - s2)*(s - s3))
print('Длина стороны № 1 %.2f треугольника, lлина стороны № 2 %.2f, lлина стороны № 3 %.2f, площадь треугольника %.2f.' %(s1, s2, s3, area))

#ex 22
import math
s1 = int(input('Введите длину стороны № 1: '))
s2 = int(input('Введите длину стороны № 2: '))
s3 = int(input('Введите длину стороны № 3: '))
s = (s1+s2+s3)/2
area = math.sqrt(s*(s - s1)*(s - s2)*(s - s3))
print('Длина стороны № 1 %.2f треугольника, lлина стороны № 2 %.2f, lлина стороны № 3 %.2f, площадь треугольника %.2f.' %(s1, s2, s3, area))

#ex 23
import math
PI = math.pi
s = int(input('Введите длину стороны: '))
n = int(input('Введите количество сторон: '))
tang = math.tan(PI/n)
area = (n*s**2)/(4*math.tan(PI/n))
print('Длина стороны  %.2f, кол-во сторон %.2f, площадь %.2f , pi - %.6f, тангенс - %.6f' %(s, n, area, PI, tang))

#ex24
min1 = 60
hour = int(input('Часы: '))
minut = int(input('Минуты: '))
seconds = int(input('Секунды: '))
all_seconds = (hour*min1*60) + (minut*min1) + seconds
print(all_seconds)

#ex25
D = 60 * 60 * 24
H = 60 * 60
M = 60

i = int(input('Время: '))
dd = int(i // D)
hh = int((i - (dd*D)) // H)
mm = int((i - (dd*D) - (hh*H)) // M)
ss = int(i - (dd*D) - (hh*H)- (mm*M))
print(f'{dd}: {hh}: {mm}: {ss}')
print("Длительность:", \
    "%d:%02d:%02d:%02d." % (dd, hh, mm, ss))

##
# Переводим секунды в дни, часы, минуты и секунды
#
SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
# Запрашиваем у пользователя длительность в секундах
seconds = int(input("Введите количество секунд: "))
# Переводим введенное значение в дни, часы, минуты и секунды
days = seconds / SECONDS_PER_DAY
seconds = seconds % SECONDS_PER_DAY
hours = seconds / SECONDS_PER_HOUR
seconds = seconds % SECONDS_PER_HOUR
minutes = seconds / SECONDS_PER_MINUTE
seconds = seconds % SECONDS_PER_MINUTE
# Отобразим результат в требуемом формате
print("Длительность:", \
"%d:%02d:%02d:%02d." % (days, hours, minutes, seconds))

#26
import time
time.asctime()