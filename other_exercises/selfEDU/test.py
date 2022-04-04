from operator import ge


class Class1:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def method_for_all(self):
        return 2*(self.w + self.h)


class Class2:
    def __init__(self, a):
        self.a = a

    def method_for_all(self):
        return 4 * self.a


class Class3:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def method_for_all(self):
        return self.a + self.b + self.c 


geom = [Class1(1, 2), Class1(3, 4),
        Class2(10), Class2(20),
        Class3(1, 2, 3), Class3(4, 5, 6)
        ]       

for g in geom:
    print(g.method_for_all()) 

#print(r1.method1(), r2.method1())
#print(s1.method2(), s2.method2())

