from die import Die
import pygal

#Создаем кубик с 6-ю гранями 
die1 = Die()
die2 = Die()

#Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)
#print(results)

freque = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    freq = results.count(value)
    freque.append(freq)
print(freque)

#Визуализация результатов
hist = pygal.Bar()
hist._title = 'Результаты выбрасываний кубика 6 граней, 1000 мудуляций'
hist.x_labels = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
hist._x_title = 'Результат'
hist._y_title = 'Частота выпадания'
hist.add('D6 + D6', freque)
hist.render_to_file('die_visual.svg')




