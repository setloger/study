#1. Построение простого графика
from re import S
import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth = 5)


#2. Назначение заголовка диаграммы и меток осей
import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]

#Работаем с легендой графика
plt.plot(squares, linewidth = 5)
plt.title('Square numbers', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square of Value', fontsize = 14)

#Назначение размера шрифта делений на осях
plt.tick_params(axis='both', labelsize = 14)
plt.show()


#3. Переопределение начала отображения графика
import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

#Работаем с легендой графика
plt.plot(input_values ,squares, linewidth = 5)
plt.title('Square numbers', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square of Value', fontsize = 14)

#Назначение размера шрифта делений на осях
plt.tick_params(axis='both', labelsize = 14)
plt.show()


#3. Нанесение дополнительных точек
import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

#Создаем точки на графике
x_values = (1, 2, 3, 4)
y_values = (2, 3, 5, 6)
plt.scatter(x_values, y_values, s=100)

#Работаем с легендой графика
plt.plot(input_values ,squares, linewidth = 5)
plt.title('Square numbers', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square of Value', fontsize = 14)

#Назначение размера шрифта делений на осях
plt.tick_params(axis='both', labelsize = 14)
plt.show()


#4. Автоматическое вычсление данных
import matplotlib.pyplot as plt

#Создаем точки на графике
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, edgecolor='none', c='green', s=5)
# отображает градиентом plt.scatter(x_values, y_values, edgecolor='none', c=y_values, cmap=plt.cm.Blues, s=5)

#Работаем с легендой графика
plt.title('Square numbers', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square of Value', fontsize = 14)

#Назначение размера шрифта делений на осях
plt.tick_params(axis='both', labelsize = 14)

#Назначение диапазона для каждой оси
plt.axis([0, 1100, 0, 1100000])
plt.show()



