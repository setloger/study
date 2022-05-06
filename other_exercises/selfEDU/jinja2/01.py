from jinja2 import Template

#1
name = 'Sasha'

tm = Template('Привет {{ name }}')
msg = tm.render(name=name)

print(msg)

#2
name2 = 'Misha'
age2 = 28

tm2 = Template('I am {{age}} and my name {{ name }}')
msg2 = tm2.render(name=name2, age=age2)

print(msg2)

#3 Реализация через класс
class Person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

per = Person('Vlad', 33)

tm = Template('Me {{p.age}} I {{p.name}} ')
msg = tm.render(p=per)

print(msg)

#4 Экранирование строки
link = '''В HTML-документе ссылки определяются так: 
<a href="#">Ссылка</a>'''
 
tm = Template("{{ link | e }}")
msg = tm.render(link = link)
 
print(msg)

#5 выражение for

cities = [{'id': 1, 'city': 'Москва'},
          {'id': 5, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Смоленск'},
          {'id': 11, 'city': 'Калуга'}]

link5 = """<select name='cities'>
{% for c in cities %}
    <option value='{{c['id']}}'>{{c['city']}}</option>
{% endfor %}
</select>"""
tm5 = Template(link5)
msg5 = tm5.render(cities = cities)

print(msg5)
