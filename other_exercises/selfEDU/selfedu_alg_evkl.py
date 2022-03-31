import time


#version 1


def get_nod(a, b):
    """Вычисляется НОД по алгоритму Евклида
    a: первое натуральное число
    b: второе натуральное число
    return: НОД
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def test_nod(func):
    # --- тест № 1 ----
    a = 28
    b = 35
    result = func(a, b)
    if result == 7:
        print('#test 1 - ok')
    else:
        print('#test 1 - fail')

    # --- тест № 2 ---
    a = 100
    b = 1
    result = func(a, b)
    if result == 1:
        print('#test2 = ok')
    else:
        print('#test2 - fail')

    # --- тест № 3 ---    
    a = 2
    b = 100000000
    st = time.time()
    result = func(a, b)
    et = time.time()
    dt = et - st
    if result == 2 and dt < 1:
        print(f'#test3 - ok, time = {dt}')
    else:
        print(f'#test3 - fail, time = {dt}')


test_nod(get_nod)


#version 2 algorithm Euclid

def get_nod(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def test_nod(func):
    # --- тест № 1 ----
    a = 28
    b = 35
    result = func(a, b)
    if result == 7:
        print('#test 1 - ok')
    else:
        print('#test 1 - fail')

    # --- тест № 2 ---
    a = 100
    b = 1
    result = func(a, b)
    if result == 1:
        print('#test2 = ok')
    else:
        print('#test2 - fail')

    # --- тест № 3 ---    
    a = 2
    b = 15646458
    st = time.time()
    result = func(a, b)
    et = time.time()
    dt = et - st
    if result == 2 and dt < 1:
        print(f'#test3 - ok, time = {dt}')
    else:
        print(f'#test3 - fail, time = {dt}')


test_nod(get_nod)