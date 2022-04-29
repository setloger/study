#4. Автоматическое вычсление данных
import matplotlib.pyplot as plt

#Создаем точки на графике
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=5)

#Работаем с легендой графика
plt.title('Square numbers', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square of Value', fontsize = 14)

#Назначение размера шрифта делений на осях
plt.tick_params(axis='both', labelsize = 14)

#Назначение диапазона для каждой оси
plt.axis([0, 1100, 0, 1100000])
plt.show()