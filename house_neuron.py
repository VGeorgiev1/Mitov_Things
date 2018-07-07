import csv
import re as re
import numpy as np
import matplotlib.pyplot as plt
import random as random
from random import uniform
from sklearn import preprocessing
import math as math
last =  preprocessing.normalize(np.array([[1 ,0.04741,   0.00,  11.930,  0,  0.5730,  6.0300,  80.80,  2.5050,   1,  273.0,  21.00, 396.90,   7.88]]))
#print(last)
with open('housing.data', 'rb') as file:
    rows = file.read().splitlines()
    #rows = file.split("\\n")
    all_rows = []
    for row in range(0,506):
        all_rows.append(list(map(lambda x: float(x), rows[row].decode("utf-8").split())))
    all_rows = np.array(all_rows)
x = preprocessing.normalize(all_rows[:,0:13])
x =  np.hstack((np.ones((506,1)), x))

w1 = np.random.random_sample((14,20))
w2 = np.random.random_sample((21,1))
y = preprocessing.normalize(np.array(all_rows[:,13:]))
learning_rate = 0.1
alr = 0.05
epochs = 100000
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
sig = np.vectorize(sigmoid)
while 1:
    a1 = np.hstack((np.ones((506,1)),x.dot(w1)))
    p = sig(a1.dot(w2))
    err =  np.sum((p - y)**2) / 2 * 506
    print(err)
    mape = 100 * (np.abs(np.sum((p - y)/p)))
    delta2 = p - y
    w2d = np.array(a1.T.dot(delta2))[1:]
    der = a1[:,1:] * (1 - a1[:,1:])
    delta1 = ((w2d.dot(delta2.T)).T) * der
    w1d = (x.T).dot(delta1)
    w1 -= w1d * learning_rate
    w2[1:] -= w2d * learning_rate