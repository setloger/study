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

#ex 45
NY = '1 января'
DK = '1 июля'
RO = '25 декабря'

user_day = input('Введите день месяц:  ')
if user_day == NY:
    print('НОВЫЙ ГОД')
elif user_day == DK:
    print('День Канады')
elif user_day == RO:
    print('Рождество')
else:
    print(f'{user_day} - такая дата не попадает на официальный праздник в Канаде')

#ex 46

checkerboard_number = input('Enter the number of the checkerboard (for example \"С4\" \"A1\"): ').lower()
letter = checkerboard_number[0]
number = int(checkerboard_number[1])

black_cage = ('a', 'c', 'e', 'g')
white_cage = ('b', 'd', 'f', 'h')
if letter in black_cage and number % 2 != 0:
    print(f'This checkerboard you entered {checkerboard_number.upper()} is \"BLACK\"')
else:
    print(f'This checkerboard you entered {checkerboard_number.upper()} is \"WHITE\"')

#ex 47

user_month = input('Enter month: ').lower()
user_day = int(input('Enter day: '))

if user_month == 'march' and 20 <= user_day <= 31 or user_month == 'april' or user_month == 'may' or user_month == 'june' and 1 <= user_day <= 20:
    print(f'You entered is {user_day} {user_month}. This is SPRING!')
elif user_month == 'june' and 21 <= user_day <= 30 or user_month == 'july' or user_month == 'august' or user_month == 'september' and 1 <= user_day <= 21 :
    print(f'You entered is {user_day} {user_month}. This is SUMMER!')
elif user_month == 'september' and 22 <= user_day <= 31 or user_month == 'october' or user_month == 'november' or user_month == 'december' and 1 <= user_day <= 20 :
    print(f'You entered is {user_day} {user_month}. This is AUTUMN!')
elif user_month == 'december' and 22 <= user_day <= 30 or user_month == 'january' or user_month == 'february' or user_month == 'march' and 1 <= user_day <= 19 :
    print(f'You entered is {user_day} {user_month}. This is WINTER!')
else:
    print('You entered an invalid value!' )

# ex 48
date_birth = input('Enter your date of birth (for example \"21 december\"): ').lower()
day_month_list = date_birth.split(' ')
day_number = int(day_month_list[0])
month_birth = day_month_list[1]

if month_birth == 'december' and 22 <= day_number <= 31 or month_birth == 'january' and 1 <= day_number <= 19:
    print(f'You Date of Birth: {date_birth}. Zodiac sign is Capricorn!')
elif month_birth == 'january' and 20 <= day_number <= 31 or month_birth == 'february' and 1 <= day_number <= 18:
    print(f'You Date of Birth: {date_birth}. Zodiac sign is Aquarius!')
elif month_birth == 'february' and 19 <= day_number <= 28 or month_birth == 'march' and 1 <= day_number <= 20:
    print(f'You Date of Birth: {date_birth}. Zodiac sign is Pisces!')
elif month_birth == 'march' and 21 <= day_number <= 31 or month_birth == 'april' and 1 <= day_number <= 19:
    print(f'You Date of Birth: {date_birth}. Zodiac sign is Aries!')    
elif month_birth == 'april' and 20 <= day_number <= 30 or month_birth == 'may' and 1 <= day_number <= 20:
    print(f'You Date of Birth: {date_birth}. Zodiac sign is Taurus!')
elif month_birth == 'may' and 21 <= day_number <= 31 or month_birth == 'june' and 1 <= day_number <= 20:
    print(f'You Date of Birth: {date_birth}. Zodiac sign is Gemini!')
elif month_birth == 'june' and 21 <= day_number <= 30 or month_birth == 'july' and 1 <= day_number <= 22:
    print(f'You Date of Birth: {date_birth}. Zodiac sign is Cancer!')
elif month_birth == 'july' and 23 <= day_number <= 31 or month_birth == 'august' and 1 <= day_number <= 22:
    print(f'You Date of Birth: {date_birth}. Zodiac sign is Leo!')
elif month_birth == 'august' and 23 <= day_number <= 30 or month_birth == 'september' and 1 <= day_number <= 22:
    print(f'You Date of Birth: {date_birth}. Zodiac sign is Virgo!')
elif month_birth == 'september' and 23 <= day_number <= 31 or month_birth == 'october' and 1 <= day_number <= 22:
    print(f'You Date of Birth: {date_birth}. Zodiac sign is Libra!')
elif month_birth == 'october' and 23 <= day_number <= 30 or month_birth == 'november' and 1 <= day_number <= 21:
    print(f'You Date of Birth: {date_birth}. Zodiac sign is Scorpius!')
elif month_birth == 'november' and 22 <= day_number <= 31 or month_birth == 'december' and 1 <= day_number <= 21:
    print(f'You Date of Birth: {date_birth}. Zodiac sign is Sagittarius!')
else:
    print(f'You entered {date_birth}. This is not correct!')

#ex 49
chinese_horoscope = {2000: 'Дракона', 2001: 'Змеи', 2002: 'Лошади', 2003: 'Козы', 2004: 'Обезьяны', 2005: 'Петуха', 
                    2006: 'Собаки', 2007: 'Свиньи', 2008: 'Крысы', 2009: 'Быка', 2010: 'Тигра', 2011: 'Кролика'
                    }
year_birth = int(input('Enter your year of birth : '))
if year_birth in chinese_horoscope:
    print(f'Вы ввели год № {year_birth}, это год {chinese_horoscope[year_birth].upper()}!')
elif 2011 <= year_birth :
    print('Вы ввели не правильный год. Повторите попытку!')
elif year_birth not in chinese_horoscope:
    for i in range(year_birth, 2012, 12):
        pass
    print(f'Вы ввели год № {year_birth}, это год {chinese_horoscope[i].upper()}!!!')

#ex 50

user_magnitude = float(input('Enter your value magnitude:'))

if user_magnitude < 2.0:
    print(f'Entered magnitude value {user_magnitude} less than 2.0. Earthquake description - minimal.')
elif 2.0 <= user_magnitude < 3.0:
    print(f'Entered magnitude value {user_magnitude} more than 2.0 and less than 3.0. Earthquake description - very weak.')
elif 3.0 <= user_magnitude < 4.0:
    print(f'Entered magnitude value {user_magnitude} more than 3.0 and less than 4.0. Earthquake description - weak.')
elif 4.0 <= user_magnitude < 5.0:
    print(f'Entered magnitude value {user_magnitude} more than 4.0 and less than 5.0. Earthquake description - intermediate.')
elif 5.0 <= user_magnitude < 6.0:
    print(f'Entered magnitude value {user_magnitude} more than 5.0 and less than 6.0. Earthquake description - moderate.')
elif 6.0 <= user_magnitude < 7.0:
    print(f'Entered magnitude value {user_magnitude} more than 6.0 and less than 7.0. Earthquake description - strong.')
elif 7.0 <= user_magnitude < 8.0:
    print(f'Entered magnitude value {user_magnitude} more than 7.0 and less than 8.0. Earthquake description - very strong.')
elif 8.0 <= user_magnitude < 10.0:
    print(f'Entered magnitude value {user_magnitude} more than 8.0 and less than 10.0. Earthquake description - huge.')    
else:
    print(f'Entered magnitude value {user_magnitude} more than 10.0. Earthquake description - destructive.') 

# ex 51
a = int(input('Enter value a: ')) 
b = int(input('Enter value b: '))
c = int(input('Enter value c: '))
D = b**2 - 4*a*c
if D < 0:
    print('No valid roots')
elif D == 0:
    x = -(b/2*a)
    print('A quadratic equation has one root. Value = %.2f' %(x))
elif 0 < D:
    x1 = (-b + (D**0.5))/2*a 
    x2 = (-b - (D**0.5))/2*a
    print('A quadratic equation has two roots. Values first root = %.2f and second root = %.2f' %(x1, x2))
else:
    print('Bro, something went wrong!!!')

#ex 52

user_grade = input('Enter you letter grade:').upper()

dict_letter_number = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
                    'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3,
                    'D': 1.0, 'F': 0,
                    }
if user_grade in dict_letter_number:
    print(f'Entered value {user_grade}. You\'re grade is {dict_letter_number[user_grade]}')
else:
    print(f'Entered value {user_grade}. Bro you made a mistake!')