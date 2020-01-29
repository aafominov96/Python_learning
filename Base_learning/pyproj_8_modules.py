import math
import time as t
import os
import random as rand
import pyproj_test_1 as calc
import matplotlib.pyplot as mpl

x = [math.cos(a) for a in range(1, 100, 1)]
y = [math.sin(a) for a in range(1, 100, 1)]
print('cos(x) x = 0:100:1 ', x)
print('Секунд с сотворения мира: ', t.time())
print('Рабочая папка ', os.getcwd())
print('Операционная система ', os.name)
a = os.environ
a = str(a)
new_file = str()
for bukva in a:
    new_file = new_file + bukva
    if bukva == ",":
        new_file = new_file + "\n"
print(new_file)
print(rand.randint(1, 10))
figure1 = mpl.figure(1)
mpl.plot(x, y)
mpl.show()
figure2 = mpl.figure(2)
mpl.plot(x, x)
mpl.show()