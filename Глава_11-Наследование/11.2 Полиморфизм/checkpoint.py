class Vegetable:
    def __init__(self, vegtype):
        self.__vegtype = vegtype
    
    def message(self):
        print('Я - овощ.')
    def __str__(self):
        return self.__vegtype

class Potato(Vegetable):
    def __init__(self):
        Vegetable.__init__(self, 'Картофель')
    
    def message(self):
        print('Я - картофель.')

v = Vegetable('овощной продукт')
d = Vegetable('Продукт овощной.')

p = Potato()
v.message()
p.message()
print(v)
print(p)
print(d)
print(v)