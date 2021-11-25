# ex 1

from typing import NewType

from chapter_1_Introduction_to_programming import A


my_integer = int(input('Введите целое число: '))
if my_integer % 2 == 0:
    print(f'Вы ввели четное число: {my_integer}')
else:
    print(f'Вы ввели нечетное число: {my_integer}')

# ex 2

my_year = int(input('Введите возраст, лет: '))
if my_year == 0:
    print(f'Вы ввели: {my_year} лет, введите корректное значение!')
elif my_year < 0:
    print('Вы не ошиблись?')  
elif my_year <= 2:
    dog_age = my_year*10.5
    print(f'Введенное значение: {my_year},\
    что равняется возрасту собаки: {dog_age}') 
elif my_year < 25:
    dog_age = 2*10.5 + ((my_year - 2)*4)
    print(f'Введенное значение: {my_year},\
    что равняется возрасту собаки: {dog_age}')   
else:
    print('Не может быть!')