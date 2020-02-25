# class Myclass:
#
#     def __init__(self):
#         print(1,'self in init = {}'.format(id(self)))
#
#     def showself(self):
#         print(2,'self in showself() = {}'.format(id(self)))
#
# c = Myclass()
#
# print(3,'c = {}'.format(id(c)))
# print('-'*30)
# c.showself()

# class Person:
#     age = 30
#     def __init__(self,name):
#         self.name = name
#
#
#
# tom = Person('tom')
#
#
# jerry = Person('jerry')
#
#
# print(tom.name,tom.age)
# print('-'*30)
# print(jerry.name,jerry.age)
#
# print(Person.age)
# print('_**'*20)
# print(Person.__name__)
# print('*-*'*30)
# print(Person.__class__)
# print('!~'*30)
# print(Person.__dict__)
# print('&^'*30)
# print(Person.__qualname__)
# class Person:
#     age = 30
#
#     def __init__(self,name):
#         self.name = name
#
#
# print('---class---')
# print(Person.__class__,type(Person))
#
# print(sorted(Person.__dict__.items()),end = '\n\n')
#
# tom = Person('tom')
# print('--------------instance tom---------------------')
# print(tom.__class__,type(tom))
# print(sorted(tom.__dict__.items()),end = '\n\n\n\n')
# #<class '__main__.Person'> <class '__main__.Person'>
# print('---tom\'s class----')
# print(tom.__class__.__name__)
# print(sorted(tom.__class__.__dict__.items()),end = '\n\n')
#
#
# class Person:
#     age = 30
#     heigth = 175
#
#     def __init__(self,name,age=18):
#         self.name = name
#         self.age = age
#
#
# tom = Person('tom')
# jerry = Person('Jerry',20)
#
# Person.age = 30
#
# print(1,Person.age,tom.age,jerry.age)
#
#
# print(2,Person.heigth,tom.heigth,jerry.heigth)
# print('##__--'* 30)
# jerry.heigth = 170
# print(3,Person.heigth,tom.heigth,jerry.heigth)
# tom.heigth +=10
#
# print(4,Person.heigth,tom.heigth,jerry.heigth)
#
#
# Person.heigth += 15
#
# print(5,Person.heigth,tom.heigth,jerry.heigth)
#
# Person.weigth = 70
# print(6,Person.weigth,tom.weigth,jerry.weigth)
#
# print(7,tom.__dict__['heigth'])
# print(8,tom.__dict__['weigth'])
#
# def add_name(name,cls):
#     cls.NAME = name
#
# def add_name(name):
#     def wrapper(cls):
#         cls.NAME = name
#         return cls
#     return wrapper
#
# @add_name('tom')
# class Person:
#     AGE = 30
#
# print(Person.NAME)


# class Person:
#     """test"""
#     @classmethod
#     def normal_methon(cls):
#         # a = 3
#         print('normal')
#         return 123
#
# Person.normal_methon()
# Person().normal_methon()
#
# print(Person.__dict__)

#
# class Person:
#     """just a test instance"""
#     @classmethod
#     def class_methon(cls):
#         print('class = {0.__name__} ({0})'.format(cls))
#         cls.HEIGTH = 170
#
# Person.class_methon()
# print(Person.__dict__)


# class Person:
#     @classmethod
#     def class_methon(cls):
#         print('class = {0.__name__} ({0})'.format(cls))
#         cls.HEIGHT = 170
#
#     @staticmethod
#     def static_methon():
#         print(Person.HEIGHT)
#
# Person.class_methon()
# Person.static_methon()
# print(Person.__dict__)

# class Person:
#     def methon(self):
#         print("{}'s methon".format(self))
#
#     # def __str__(self):
#     #     return 'test'
#     @classmethod
#     def class_methon(cls):
#         print('class = {0.__name__} ({0})'.format(cls))
#         cls.HEIGHT = 170
#
#     @staticmethod
#     def static_methon():
#         print(Person.HEIGHT)

# print('~~~~~~~~~~~类访问')
# print(1,Person.methon('tom'))
# print(2,Person.class_methon())
# print(3,Person.static_methon())
# print(Person.__dict__)
# print('~~实例访问')
# print('tom~~~~')
#
# tom = Person()
# print(4,tom.methon())
# print(5,tom.static_methon())
# print(6,tom.class_methon())
#
# tom = Person()
# tom.methon()
# Person.methon(tom)
# Person.methon(tom)
# tom.__class__.methon(tom)


# class Person:
#     def __init__(self,name,age=18):
#         self.name = name
#         self.__age =age
#
#     def growup(self,i=1):
#         if i > 0 and i < 150:
#             self.__age +=1
#
#     def getage(self):
#         return self.__age
#
#
# p1 = Person('tom')
# p1.growup(20)
# # p1.age = 130
#
# # print(p1.__age)
# # # print(p1.age)
#
# print(Person('tom').getage())

class Person:

    def __init__(self,name,age = 18):
        self.name = name
        self.__age = age

    def growup(self,i=1):
        if i > 0 and i < 150:
            self.__age += 1

    def getage(self):
        return self.__age

p1 = Person('tom')
p1.growup(20)
p1.__age = 28
print(p1.__age)
print(p1.getage())
print(p1.__age)

print(p1.__dict__)


