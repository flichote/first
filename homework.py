# # import math
# #
# #
# #
# # for i in range(1,10,1):
# #     for j in range(1,10,1):
# #         if i >= j:
# #             print(str(j) + '*' + str(i) + '=' + str(i*j),end=' ')
# #     print()
# # print('_' * 30)
# #
# #
#
# for i in range(1,8,2):
#     # if i % 2 == 1:
#     print(' '*int((10-i)/2 -1) + '*'*i)
#     # print('*'*i)
# for j in range(5,0,-2):
#     print(' '*int((10-j)/2 -1) + '*'*j)
#
#


# ,1,1,2,3,5,8,13,21,34
#
# a = 0 +1
# a1 = a + 1
# a2 = a1 + a
# a3 = a2 + a1
#
#
# 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34
#
#
# i = 101
# for i in range(0,100,(100-i)):
#     print(i)

print(0)
print(1)
a = 0
b = 1
count = 0
while True:
    c = a + b
    # if c > 10000000000000: break
    a = b
    b = c
    count += 1
    if count == 100: break
    print(c)

from collections import namedtuple
