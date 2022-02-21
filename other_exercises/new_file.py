a = [f'{x}*{y} = {x*y}'
    for x in range(1, 10)
    for y in range(1, 10)]

print(a)

matrix = [[1,2,3], [4,5,6], [7,8,9,10]]
a = [x
    for row in matrix
    for x in row
    ]
print(a)