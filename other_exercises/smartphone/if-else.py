#1
numb = int(input())

if numb < 0:
    print('-1')
elif numb > 0:
    print('1')
else:
    print('0')


#2
numb = int(input())

if numb % 2 == 0:
    print('Четное')
else:
    print('нечетное')


#3
numb1 = int(input())
numb2 = int(input())
numb3 = int(input())

if numb2 <= numb1 >= numb3:
    print(f'{numb1} number 1 is max')
elif numb1 <= numb2 >= numb3:
    print(f'{numb2} number 2 is max')
elif numb1 <= numb3 >= numb2:
    print(f'{numb3} number 3 is max')


#4
numb1 = int(input())
numb2 = int(input())

if numb1 % numb2 == 0:
    print('Yes!')
else:
    rest = numb1 % numb2
    print(rest)


#5
tempr = input()
sign = tempr[-1]
t = int(tempr[:-1])

if sign == 'C' or 'c':
    tempr_cel = (t * (9/5)) + 32
    print(f'Температура в Фаренгейтах = {tempr_cel}')
elif sign == 'F' or 'f':
    tempr_faren = (t - 32) * (5 / 9)
    print(f'Температура в Цельсиях = {tempr_faren}')
else:
    ('Введено неверное значение')

t = input() 
sign = t[-1] 
t = int(t[:-1]) 
if sign == 'C' or sign == 'c': 
    t = round(t * (9 / 5) + 32) 
    print(str(t) + 'F') 
elif sign == 'F' or sign == 'f': 
    t = round((t - 32) * (5 / 9)) 
    print(str(t) + 'C')