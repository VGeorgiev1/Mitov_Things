import numpy as np
import matplotlib.pyplot as plt
import random as random

x = np.random.random((100, 1)) * 100
print(x)

#print(x_ones)
w0 = 1.
w1 = 2.
#w = np.array(([w0],[w1]))
y = np.array([x * w1 + w0 for x in x])
errs = []
ws = [-2,-1,-0,1,2,3,4,5,6]
for w in ws:
    wDelta = np.array([0,w])
    errs.append(np.sum(((wDelta.dot(np.vstack((np.ones(100),x))) - y) / 100) **2 ))
    plt.plot(wDelta.dot(np.vstack((np.ones(100), np.arange(100) ))))
    plt.plot(x,y,"bo")
    plt.show()
print(errs)
##plt.plot(ws, errs)
#plt.show()
#print(predictions.shape)
#print(predictions)
def fit(times, inputs, outputs , learn_rate):
    ws = np.array(([20.],[10.]))
    print(ws) 
    x_ones = np.hstack((np.ones((100,1)), inputs))
    #print(x_ones)
    while 1:
        predictions = x_ones.dot(ws)
        
        #print(predictions)
        deltaw0 = learn_rate / 100 * np.sum( predictions - outputs )
        deltaw1 = learn_rate / 100 * np.sum( (predictions - outputs) * inputs )
    #    print(deltaw0)
        ws[0][0] = ws[0][0] - deltaw0
        ws[1][0] = ws[1][0] - deltaw1

