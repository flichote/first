
list
# def fib(n):
#     a,b = 0,1
#     for i in range(n-1):
#         a,b = b,a+b
#     return b
#
# print(fib(55))

# a,b = b , a+b

def fib(n):
    a = 0
    b = 1
    c = 1
    a,b, c= a,a+b,b +c
    return c
print(fib(54))


