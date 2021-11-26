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