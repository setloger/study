import shelve
from person import Person
fieldnames = ('name', 'age', 'job', 'pay')

db = shelve.open('class-shelve')
while True:
    key = input('\nKey? => ')
    if not key: break
    if key in db:
        record = db[key]                    #изменить существующую
    else:                                   # или создать новую
        record = Person(name='?', age='?')  # для eval: строки в кавычках
    for field in fieldnames:
        currval = getattr(record, field)
        newtext  = input('\t[%s]=%s\n\t\tnew?=>' %(field, currval))
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record
    db.close()
    