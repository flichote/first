# class Student:
#     def __init__(self,name,gender):
#         self.__name = name
#         self.__gender = gender
#
#     def get_gender(self):
#         return self.__gender
#
#     def set_gender(self):
#         self.__gender = gender
#
#
#
#
# tom = Student('tom','man')
# print(tom.get_gender())
# # tom.get_g?er()

# class Animal(object):
#     def run(self):
#         print('Animal is running')
#
# class Dog(Animal):
#     def run(self):
#         print('Dog is running')
#     def eat(self):
#         print('Dog is eating')
#
#
# class Cat(Animal):
#     pass
# d = Dog()
# # print(d.run())
# cat = Cat()
# cat.run()
#
# d.eat()
#
# a = list()
# b = Animal()
# c = Dog()
#
# print(isinstance(a,list))
# print(isinstance(b,Animal))
# print(isinstance(c,Dog))
#
# print(isinstance(c,Animal))
# print(isinstance(b,Dog))


# class Myobject(object):
#     def __init__(self):
#         self.x = 9
#
#     def power(self):
#         return self.x * self.x
#
# obj = Myobject()
#
# print(hasattr(obj,'x'))
# print(obj.x)
# print(hasattr(obj,'y'))
# setattr(obj,'y',19)
# print(hasattr(obj,'y'))
# print(obj.y)
# print('-'*10)
# print(getattr(obj,'y'))

#
# class Fib:
#     def __getitem__(self, n):
#         a,b = 1,1
#         for x in range(n):
#             a,b = b,a+b
#         return a
#
# f = Fib()
#
#
# print(f[100])
#
# print(list(f[100])[:])



import sys
print(sys.modules,sep='\n')