import matplotlib.pyplot as plt
import math as m
import random as r
i = 0
x = [a for a in range(1,1000+1,1)]
while i < len(x):
    x[i] = x[i]/1000
    i+=1
y = [m.sin(a)+r.gauss(0.5, 1) for a in x]
f1 = plt.figure(1)
plt.plot(x, y)
plt.grid()
w = int(20)
i = int(w/2)-1
y_new = y
s = 0
count = 0
while i < len(x)-w/2-1:
    left = int(i-w/2+1)
    right = int(i+w/2)
    for j in range(left, right+1, 1):
        s += y[j]
        count += 1
    y_new[i] = s/w
    s = 0
    i += 1

#f2 = plt.figure(2)
#plt.plot(x,y_new)
#plt.grid()
#plt.show()
n = len(x)
check = (n - w)*w
print('Size of x: ', len(x))
print('Count of iterations: ', count)
print("Check: ", check)