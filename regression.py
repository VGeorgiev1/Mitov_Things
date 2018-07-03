import numpy as np
import matplotlib.pyplot as plt
import random as random
from random import uniform

x = np.random.random((100, 1))
w0 = 100
w1 = 700
print(x)

y = np.array([x * w1 + w0 + uniform(-50,50) for x in x])
print(y)
plt.plot(x,y,'o')
plt.show()
ws = np.array([[0.], [1.]])

samples = np.hstack((np.ones(x.shape), x))
learning_rate = 0.4

while 1:
    prediction = samples.dot(ws)
    deltaw0 = learning_rate / 100 * np.sum(samples.dot(ws) - y)
    deltaw1 = learning_rate / 100 * np.sum((samples.dot(ws) - y) * x) 
    ws[0][0] -= deltaw0
    ws[1][0] -= deltaw1
    plt.plot(x,y, 'o')
    range = np.arange(0,1.5,learning_rate)
    plt.plot(range, [ws[0][0] + ws[1][0] * x for x in range])
    plt.draw()
    plt.pause(0.1)
    plt.clf()
