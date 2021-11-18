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

# ex6
