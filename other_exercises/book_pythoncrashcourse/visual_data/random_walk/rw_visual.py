import matplotlib.pyplot as plt
from random_walk import RandomWalk


#Построение случайного блуждания и нанесение точек на диаграмму
rw = RandomWalk()
rw.fill_walk()
#Назначение размера области просмотра
plt.figure(figsize=(10,6))
point_numbers = list(range(rw.num_points))

plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
    edgecolors='none' ,s=5)

#Выделяем первую и последнюю точки на графике
plt.scatter(0, 0, c='green', edgecolors='none' ,s=40)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none' ,s=40)

#Удаление осей - не работает    -TO DO проверить синтаксис
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)

plt.show()
