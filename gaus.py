import random as random
import matplotlib.pyplot as plt
import numpy as np
import math as math
points = 100
mu, sigma = 1, 0.50 # mean and standard deviation
mu1, sigma1 = 2.5, 0.50
learning_rate = 0.5
dist = max(mu,mu1)

s1 = np.random.normal(mu, sigma, points)
s2 = np.random.normal(mu, sigma, points)
s3 = np.random.normal(mu1,sigma1, points)
s4 = np.random.normal(mu1,sigma1, points)

plt.plot(s1,s2, 'o')
plt.plot(s3,s4, 'o')
plt.show()
x_big = np.hstack((np.ones((points * 2,1)),np.vstack((np.concatenate((s1,s3)),np.concatenate((s2,s4)))).T))
ws = np.array([[10.], [20.], [30.]])
y = np.vstack((np.zeros((points,1)), np.ones((points,1))))
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

while 1:
    
    prediction = np.array([[sigmoid(xi)] for xi in x_big.dot(ws)])
    deltaw0 = learning_rate / points * 2 * np.sum(prediction - y)
    deltaw1 = learning_rate / points * 2 * np.sum((prediction - y) * x_big[:,1].reshape(points * 2,1))
    deltaw2 = learning_rate / points * 2 * np.sum((prediction - y) * x_big[:,2].reshape(points * 2,1)) 
    ws[0][0] -= deltaw0
    ws[1][0] -= deltaw1
    ws[2][0] -= deltaw2
    range = np.arange(0,2*dist,learning_rate)
    plt.plot(range, [(-ws[0][0] - ws[1][0] * t) / ws[2][0] for t in range])
    plt.plot(s1,s2, 'o')
    plt.plot(s3,s4, 'o')
    plt.draw()
    plt.pause(0.1)
    plt.clf()