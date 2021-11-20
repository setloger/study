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