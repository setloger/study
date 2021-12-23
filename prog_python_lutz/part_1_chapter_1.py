#work with dictionaries

bob = dict(pay=30000, job='dev', age=42, name='Bob Smith')
sue = dict(pay=40000, job='hr', age=45, name='Sue Jones')

people = [bob, sue]

for i in people:
    print(i['name'], i['pay'], sep=', ')

for i in people:
    if i['name']=='Bob Smith':
        print(i['pay'])

names = [i['name'] for i in people] 
list(map((lambda x: x['name']), people)) #тоже самое
sum(person['pay'] for person in people) #сумма всех окладов

for person in people:
    print(person['name'].split()[-1]) # проход по фамилии
    person['pay'] *= 1.2 #повышаем оклад
for person in people: print(person['pay'])

## page 52
bob = dict(pay=30000, job='dev', age=42, name='Bob Smith')
sue = dict(pay=40000, job='hr', age=45, name='Sue Jones')
db = {}
db['bob'] = bob
db['sue'] = sue
db['sue']['pay'] = 50000

## page 54
for rec in db.values(): print(rec['name'], rec['pay'])
db['tom'] = dict(name='Tom Pollen', age=37, job=None, pay=0)
list(db.keys()) # список ключей
list(db.values()) # список значений
len(db)

## page 55 create file initdata.py
bob = dict(pay=30000, job='dev', age=42, name='Bob Smith')
sue = dict(pay=40000, job='hr', age=45, name='Sue Jones')
tom = dict(age=37, job=None, name='Tom Pollen', pay=0)
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n ', db[key])
        


