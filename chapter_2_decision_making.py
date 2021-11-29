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

#ex 41
side_tr_1 = int(input('Введите размер 1-й стороны треугольника: '))
side_tr_2 = int(input('Введите размер 2-й стороны треугольника: '))
side_tr_3 = int(input('Введите размер 3-й стороны треугольника: '))

if side_tr_1 == side_tr_2 and side_tr_1 == side_tr_3 and side_tr_2 == side_tr_3:
    print(f'Сторона 1 = {side_tr_1}, сторона 2 = {side_tr_2}, сторона 3 = {side_tr_3} - это равносторонний треугольник!')
elif side_tr_1 == side_tr_2 and side_tr_1 != side_tr_3 or side_tr_2 == side_tr_3 and side_tr_2 != side_tr_1 or side_tr_1 == side_tr_3 and side_tr_1 != side_tr_2:
    print(f'Сторона 1 = {side_tr_1}, сторона 2 = {side_tr_2}, сторона 3 = {side_tr_3} - это равнобедренный треугольник!')
else:
    print(f'Сторона 1 = {side_tr_1}, сторона 2 = {side_tr_2}, сторона 3 = {side_tr_3} - это разносторонний треугольник!')

#ex 42

C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88
name = input("Введите название ноты в виде буквы и цифры, например C4: ")
note = name[0]
octave = int(name[1])
# Получаем частоту ноты четвертой октавы
if note == "C":
    freq = C4_FREQ
elif note == "D":
    freq = D4_FREQ
elif note == "E":
    freq = E4_FREQ
elif note == "F":
    freq = F4_FREQ
elif note == "G":
    freq = G4_FREQ
elif note == "A":
    freq = A4_FREQ
elif note == "B":
    freq = B4_FREQ
# Адаптируем частоту к конкретной октаве
freq = freq / 2 ** (4-octave)
# Выводим результат
print("Частота ноты", name, "равна", freq)

#ex 43
C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88

note = float(input(''))
if note >= C4_FREQ*0.99 and note <= C4_FREQ*1.01:
    print(f'Нота введенная {note} - это C4')
elif note >= D4_FREQ*0.99 and note <= D4_FREQ*1.01:
    print(f'Нота введенная {note} - это D4')
elif note >= E4_FREQ*0.99 and note <= E4_FREQ*1.01:
    print(f'Нота введенная {note} - это E4')
elif note >= F4_FREQ*0.99 and note <= F4_FREQ*1.01: 
    print(f'Нота введенная {note} - это F4')
elif note >= G4_FREQ*0.99 and note <= G4_FREQ*1.01:
    print(f'Нота введенная {note} - это G4')
elif note >= A4_FREQ*0.99 and note <= A4_FREQ*1.01:
    print(f'Нота введенная {note} - это A4')
elif note >= B4_FREQ*0.99 and note <= B4_FREQ*1.01:
    print(f'Нота введенная {note} - это B4')
else:
    print(f'Частота введенная {note} - не существует.')

#ex44

DV = ['Джоржд Вашингтон', 1]
TJ = ['Томас Джефферсон', 2]
AL = ['Авраам Линкольн', 5]
AG = ['Александр Гамильтон', 10]
ED = ['Эндрю Джексон', 20]
UG = ['Улисс Грант', 50]
BF = ['Бенджамин Франклин', 100]

denomination = int(input('Введите номинал банкноты: '))


if denomination == DV[1]:
    print(f'Вы ввели номинал равный ${denomination}, на нем изображен {DV[0]}')
elif denomination == TJ[1]:
    print(f'Вы ввели номинал равный ${denomination}, на нем изображен {TJ[0]}')
elif denomination == AL[1]:
    print(f'Вы ввели номинал равный ${denomination}, на нем изображен {AL[0]}')
elif denomination == AG[1]:
    print(f'Вы ввели номинал равный ${denomination}, на нем изображен {AG[0]}')
elif denomination == ED[1]:
    print(f'Вы ввели номинал равный ${denomination}, на нем изображен {ED[0]}')
elif denomination == UG[1]:
    print(f'Вы ввели номинал равный ${denomination}, на нем изображен {UG[0]}')
elif denomination == BF[1]:
    print(f'Вы ввели номинал равный ${denomination}, на нем изображен {BF[0]}')
else:
    print('ОШИБКА! Такой банкноты не существует!')