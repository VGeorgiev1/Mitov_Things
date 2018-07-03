import numpy as np
import matplotlib.pyplot as plt
import random as random
from random import uniform
points = 100
learning_rate = 0.1

w0 = 27
w1 = 39
w2 = 1000



x = np.random.random((points, 1))
for i in range(0,50):
    x[i] = -x[i]
x = np.hstack((np.array([x[0]**2 for x in x]).reshape((points,1)), x))


y = np.array([[w1 * x[1] + w2 * x[0] + w0] for x in x])
plt.plot(x[:,1],y, 'o')
plt.show()
ws = np.array([[0.5], [1.], [2.]])
samples = np.hstack((np.ones((points,1)), x))
while 1:
    prediction = np.array([samples.dot(ws)])
    
    deltaw0 = learning_rate / points * np.sum(prediction - y)
    deltaw1 = learning_rate / points * np.sum((prediction - y) * samples[:,1].reshape(points,1))
    deltaw2 = learning_rate / points * np.sum((prediction - y) * samples[:,2].reshape(points,1)) 
    ws[0][0] -= deltaw0
    ws[1][0] -= deltaw1
    ws[2][0] -= deltaw2
    range = np.arange(-1,1,learning_rate)
    plt.plot(range, [ws[0][0] + ws[1][0] * x**2 + ws[2][0] * x for x in range])
    plt.plot(x[:,1],y, 'o')
    plt.draw()
    plt.pause(0.1)
    plt.clf()
