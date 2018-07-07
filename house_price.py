import csv
import re as re
import numpy as np
import matplotlib.pyplot as plt
import random as random
from random import uniform
from sklearn import preprocessing

last =  preprocessing.normalize(np.array([[1 ,0.04741,   0.00,  11.930,  0,  0.5730,  6.0300,  80.80,  2.5050,   1,  273.0,  21.00, 396.90,   7.88]]))
#print(last)
with open('housing.data', 'rb') as file:
    rows = file.read().splitlines()
    #rows = file.split("\\n")
    all_rows = []
    for row in range(0,500):
        all_rows.append(list(map(lambda x: float(x), rows[row].decode("utf-8").split())))
    all_rows = np.array(all_rows)
x = all_rows[:,0:13]
x = np.hstack((np.ones((500,1)), x))
w = np.ones((14,1))
old_delta = np.ones((14,1))
y = np.array(all_rows[:,13:])
learning_rate = 0.1
iteration = 0
errs = []
plt.figure(221)
old_error = 0
alr = 0.05
epochs = 100000

big = np.hstack((x, y))
np.random.shuffle(big)
x = preprocessing.normalize(big[:,0:14])
y = preprocessing.normalize(big[:,14:])
mumentum = 0.001

train_row = int(0.5 * 500)
test_row = int(0.25 * 500)
cross_road = int(0.25 * 500)
train_x = x[:train_row]
test_x =  x[train_row:test_row + train_row]
cross_x = x[train_row + test_row:test_row + train_row + cross_road]
train_y  = y[:train_row]
test_y = y[train_row:test_row + train_row]
cross_y = y[train_row + test_row:test_row + train_row + cross_road]
for _ in range(0,epochs):
    iteration+=1
    prediction = train_x.dot(w)
    prediction1 = cross_x.dot(w)
    mape_cross = np.sum(np.abs((cross_y - prediction1) / cross_y)) * 100 / 125 
    print(mape_cross)
    mape_train = np.sum(np.abs((train_y - prediction) / train_y)) * 100 / 250 
    prediction -= train_y
    delta = prediction.T.dot(train_x)
    w-= learning_rate / 250 * (delta.T + mumentum * old_delta)
    old_delta = w
prediction = test_x.dot(w)
mape_test = np.sum(np.abs((test_y - prediction) / test_y)) * 100 / 125
prediction_end = last.dot(w)
print(prediction_end)
#print(mape_test)