class A:
    """test"""
    X = 1
    __slots__ = ('x','y','z')

    def __init__(self):
        self.y = 5
        self.z = 6

    def show(self):
        print(self.X,self.y,self.z)
a = A()
# a.newx = 5
a.show()
print('A',A.__dict__)
print(a.__slots__)

class B(A):
    pass

print('B',B().__dict__)