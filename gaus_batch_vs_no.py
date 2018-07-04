import random as random
import matplotlib.pyplot as plt
import numpy as np
import math as math
points = 100
mu, sigma = 1, 0.50 # mean and standard deviation
mu1, sigma1 = 2.5, 0.50
learning_rate = 0.1
batch_size = 200
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
ws1 = np.array([[10.], [20.], [30.]])
y = np.vstack((np.zeros((points,1)), np.ones((points,1))))
def sigmoid(x):
  return 1 / (1 + math.exp(-x))
old_delta = np.array([[10.], [20.], [30.]])
delta = np.array([[10.], [20.], [30.]])
delta1 = np.array([[10.], [20.], [30.]])
iteration = 0
plt.figure(300)
err_points = []
iterations = []
err_points1 = []
old_error = 0
for i in range(0,1000):
    predictions = np.array([[sigmoid(xi)] for xi in x_big.dot(ws)])
    predictions1 = np.array([[sigmoid(xi)] for xi in x_big.dot(ws1)])
    error = -1/points*np.sum(y * np.log(predictions) + (1 - y)*np.log(1 - predictions))
    error1 = -1/points*np.sum(y * np.log(predictions1) + (1 - y)*np.log(1 - predictions1))
    old_error = error
    err_points.append(error)
    iterations.append(i)
    err_points1.append(error1)
    plt.figure(300)
    plt.plot(iterations,err_points, 'r')
    plt.plot(iterations,err_points1, 'b')
    plt.draw()
    plt.pause(0.1)

    
    delta1[0][0] = learning_rate / points * 2 * np.sum(predictions1 - y)
    delta1[1][0] = learning_rate / points * 2 * np.sum((predictions1 - y) * x_big[:,1].reshape(points * 2,1))
    delta1[2][0] = learning_rate / points * 2 * np.sum((predictions1 - y) * x_big[:,2].reshape(points * 2,1))
    
    ws1[0][0] -= delta1[0][0]
    ws1[1][0] -= delta1[1][0]
    ws1[2][0] -= delta1[2][0]