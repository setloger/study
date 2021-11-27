# ex 35

from typing import NewType

from chapter_1_Introduction_to_programming import A


my_integer = int(input('Введите целое число: '))
if my_integer % 2 == 0:
    print(f'Вы ввели четное число: {my_integer}')
else:
    print(f'Вы ввели нечетное число: {my_integer}')

# ex 36

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

# ex 37
vowels = ('A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y' )
#consonants = ('B', 'C', 'D', 'F', 'G', 'H', 'J',\
#            'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z')      

input_letter = input('Введите букву: ')

if input_letter in vowels:
    print(f'Это гласная буква: {input_letter}')
else:
    print(f'Это согласная буква: {input_letter}')

#ex 38
input_user = int(input('Введите кол-во сторон для поиска фигуры от 3-х до 10-ти'))
if input_user == 3:
    print('триугольник')
elif input_user == 4:
    print('квадрат')
elif input_user == 5:
    print('пятиугольник')
elif input_user == 6:
    print('шестиугольник')
elif input_user == 7:
    print('семиугольник')
elif input_user == 8:
    print('восьмиугольник')
elif input_user == 9:
    print('девятиугольник')
elif input_user == 10:
    print('правильный десятиугольник')
else:
    print('Вы ввели число не попадающее в диапазон от 3-х до 10-ти')

#ex 39 
user_month = input('Введите месяц: ')

if user_month.lower() == 'январь':
    print(f'31 день в {user_month}')
elif user_month.lower() == 'февраль':
    print(f'28 день в {user_month}')
elif user_month.lower() == 'март':
    print(f'31 день в {user_month}')
elif user_month.lower() == 'апрель':
    print(f'30 день в {user_month}')
elif user_month.lower() == 'май':
    print(f'31 день в {user_month}')
elif user_month.lower() == 'июнь':
    print(f'30 день в {user_month}')
elif user_month.lower() == 'июль':
    print(f'31 день в {user_month}')
elif user_month.lower() == 'август':
    print(f'30 день в {user_month}')
elif user_month.lower() == 'сентябрь':
    print(f'30 день в {user_month}')
elif user_month.lower() == 'октябрь':
    print(f'31 день в {user_month}')
elif user_month.lower() == 'ноябрь':
    print(f'30 день в {user_month}')
elif user_month.lower() == 'декабрь':
    print(f'31 день в {user_month}')
else:
    print('Вы ввели не те данные')

#ex 40

vol4 = (107, 130)
vol3 = (71, 106)
vol2 = (41, 70)
vol1 = (0, 40)

volume_noizy = int(input('Введите уровень шума, дБ: '))

if volume_noizy >= vol4[0] and volume_noizy <= vol4[1]: 
    print(f'Вы ввели - {volume_noizy} это между {vol4[0]} ... {vol4[1]}. Отбойный молоток')
elif volume_noizy >= vol3[0] and volume_noizy <= vol3[1]:
    print(f'Вы ввели - {volume_noizy} это между {vol3[0]} ... {vol3[1]}. Газовая газонокосилка')
elif volume_noizy >= vol2[0] and volume_noizy <= vol2[1]:
    print(f'Вы ввели - {volume_noizy} это между {vol2[0]} ... {vol2[1]}. Будильник')
elif volume_noizy >= vol1[0] and volume_noizy <= vol1[1]:
    print(f'Вы ввели - {volume_noizy} это между {vol1[0]} ... {vol1[1]}. Тихая комната')
else:
    print(f'Вы ввели - {volume_noizy}. Что-то не так!')
