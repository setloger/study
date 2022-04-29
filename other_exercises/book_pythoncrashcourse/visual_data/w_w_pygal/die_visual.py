from die import Die
import pygal

#Создаем кубик с 6-ю гранями 
die = Die()

#Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
#print(results)

freque = []
for value in range(1, die.num_sides+1):
    freq = results.count(value)
    freque.append(freq)
print(freque)

#Визуализация результатов
hist = pygal.Bar()
hist._title = 'Результаты выбрасываний кубика 6 граней, 1000 мудуляций'
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist._x_title = 'Результат'
hist._y_title = 'Частота выпадания'
hist.add('D6', freque)
hist.render_to_file('die_visual.svg')




