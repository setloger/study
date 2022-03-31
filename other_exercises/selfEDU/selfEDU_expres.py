#selfEDU № 54

# применяются для больших значений тк не хранятся все в памяти. формируется последовательно
from operator import le
from pickle import FALSE
from webbrowser import get


a = (x**2 for x in range(6))
list(a)
sum((x**2 for x in range(6)))
max((x**2 for x in range(6)))
gen_list = (x for x in range(10000))


for x in gen_list:
    print(x, end = ' ')
    if x > 50:
        break


#selfEDU № 55

def get_list():
    for i in range(1,10):
        a = range(i,11)
        yield sum(a) / len(a)


a = get_list()
print(list(a))

#selfEDU № 56

# функция map возвращает итерируемый генератор

s = map(int, input().split())
a = list(s)
print(a)


#selfEDU № 57
# функция фильтр - filter

c = list(range(1,11))
b = filter(lambda x: x % 2 == 0, c)
lst = tuple(b)
print(lst)


lst2 = ['Москва', 'Рязань1', 'Смоленск', 'Тверь2', 'Томск']
d = filter(str.isalpha, lst2)
print(list(d))


#selfEDU № 58
# функция zip

a = [1,2,3,4,5]
b = [3,5,7,9,11,13,15]
z = zip(a, b)
for x in z:
    print(x)


#нет необходимость приобразовывать к списку или кортежу, тк увеличивает расход памяти
df = tuple(zip(a,b))
print(df)


#selfEDU № 60
a = [4,3,-10,1,7,12]
b = sorted(a, key=lambda x: x%2)
print(b)


#selfEDU № 61

#isinstance and type

data = (4.5, 8.7, True, 'book', 8, 10 -11, [True, False])

s = 0

for x in data:
    if isinstance(x, float):
        s += x 

print(s)

#проще через фильтр
s = sum(filter(lambda x: isinstance(x, float), data)) #учитывает булевые значения 
s = sum(filter(lambda x: type(x)is float, data)) #не учитывает булевые значения 
