# import matplotlib.pyplot
# show_heigth = 30
# show_width = 40
#
# ascii_charee = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# char_len = len(ascii_charee)
# pic =matplotlib.pyplot.imread("wm.jpg")
#
# pic_heigth,pic_width,_ = pic.shape
#
# gray = 0.2126 * pic[:,:,0] + 0.7152 * pic[:,:,1] + 0.0722 * pic[:,:,2]
#
# for i in range(show_heigth):
#     y = int(i * pic_heigth/ show_heigth)
#     text = ""
#     for j in range(show_width):
#         x = int(j * pic_width/show_width)
#         text += ascii_charee[int(gray[y][x] / 256 * char_len)]
#     print(text)

# def loggre(fn):
#     """wrapper test!!"""
#     def wrapper(*args,**kwargs):
#         """logger test!!"""
#         print('begin')
#         x = fn(*args,**kwargs)
#         print('end')
#         return x
#     return wrapper
#
# @loggre  # add = logger(add)
# def add(x,y):
#     """just test!!"""
#     return x + y
#
# print(add(4,5))
# print(add.__name__,add.__doc__)

import datetime
import time

def logger(fn):
    def wrapper(*args,**kwargs):
        # bengin 功能增加
        print("args={},kwargs={}".format(args,kwargs))
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        duration = datetime.datetime.now() - start
        print("function {} took {}s.".format(fn.__name__,duration.total_seconds()))
        return ret
    return wrapper

@logger
def add(x,y):
    print("=========call add===============")
    time.sleep(2)
    return x + y
print(add(4,y=7))



