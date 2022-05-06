import re

#1. Вхождение символов
text = ('Карта map и объект bimap - это разные вещи')
match1 = re.findall(r'\bmap\b', text)

#2. Вхождение символов
text2 = 'еда, победа, беда'
match2 = re.findall(r'еда', text2)

#3. Символьные классы
text3 = 'Еда, победа, беда'
match3 = re.findall(r'[еЕ]д[ау]', text3)
text4 = 'Ед1а, поб22еда, б95еда, 76 555 -5'
match4 = re.findall(r'[0-9]', text4)
match5 = re.findall(r'[-0-9][0-9]', text4) # поиск двух символов подряд
match6 = re.findall(r'[а-яА-Я]', text4)

#4. Инверсия шаблона
text7 = 'Ед1а, поб22еда, б95еда, 76 555 -5'
match7 = re.findall(r'[^0-9]', text7)

#5. Квантификаторы {m,n}
text8 = 'Google, Gooogle, Gooooooogle, Gooogle'
match8 = re.findall(r'o{2,6}', text8) # мажорный режим
match9 = re.findall(r'o{2,6}?', text8) #минорный режим

text8 = 'Google, Gooogle, Gooooooogle, Gooogle'
match10 = re.findall(r'Go{5,}gle', text8) 
match11 = re.findall(r'Go{,4}gle', text8) 
# {4,} - от 4х вхождений {,4} - до 4х вхождений

text9, text10 = '79303200815', '793032008'  # проверка на корректность тел-го номера
match12 = re.findall(r'7\d{10}', text9) 
match13 = re.findall(r'7\d{10}', text10)

#Примеры использования
text11 = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
match14 = re.findall(r"\w+\s*=\s*[^;]+", text11)
match15 = re.findall(r"(\w+)\s*=\s*([^;]+)", text11)

#6. Сохраняющие скобки и группировка
text12 = "lat = 5, lon=7"
match16 = re.findall(r'(?:lat|lon)\s*=\s*\d+', text12)
match17 = re.findall(r'(lat|lon)\s*=\s*\d+', text12)
match18 = re.findall(r'((lat|lon)\s*=\s*\d+)', text12)
match19 = re.findall(r'(lat|lon)\s*=\s*(\d+)', text12)

text13 = "Картинка <img src='bg.jpg'> в тексте</p>"
match20 = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']", text13)



# print(f'Выходные данные:\t {match1}')
# print(f'Выходные данные:\t {match2}')
# print(f'Выходные данные:\t {match3}')
# print(f'Выходные данные:\t {match4}')
# print(f'Выходные данные:\t {match5}')
# print(f'Выходные данные:\t {match6}')
# print(f'Выходные данные:\t {match7}')
# print(f'Выходные данные:\t {match8} {match9}')
# print(f'Выходные данные:\t {match10} {match11}')
# print(f'Выходные данные 12:\t {match12} {match13}')
# print(f'Выходные данные:\t {match14}')
# print(f'Выходные данные:\t {match15}')
# print(f'Выходные данные 16:\t 16 {match16} 17 {match17} 18 {match18} 19 {match19}')
print(f'Выходные данные:\t {match20}')