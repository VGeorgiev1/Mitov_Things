import random as random
import matplotlib.pyplot as plt
import numpy as np
import math as math
points = 100
mu, sigma = 1, 0.50 # mean and standard deviation
mu1, sigma1 = 2.5, 0.50
learning_rate = 0.4
momentum = 0.9
dist = max(mu,mu1)
s1 = np.random.normal(mu, sigma, points)
s2 = np.random.normal(mu, sigma, points)
s3 = np.random.normal(mu1,sigma1, points)
s4 = np.random.normal(mu1,sigma1, points)
class Class:
    def __init__(self,mu,sigma, points):
        self.x1 = np.random.normal(mu, sigma, points)
        self.x2 = np.random.normal(mu, sigma, points)
class Model:   
    def __init__(self,points,classes, scale, draw_err= True, draw_graph = True):
        self.points = points
        self.classes = classes
        self.__gen_x()
        self.__get_y()
        self.__gen_w()
        self.cur_error = float('inf')
        self.scale = scale
        self.draw_err = draw_err
        self.draw_graph = draw_graph

    def __gen_x(self):
        start_x1 = np.concatenate((self.classes[0].x1, self.classes[1].x1))
        start_x2 = np.concatenate((self.classes[0].x2, self.classes[1].x2))
        for i in range(2,len(self.classes)):
            start_x1 = np.concatenate((start_x1, classes[i].x1))
            start_x2 = np.concatenate((start_x2, classes[i].x2))
        self.x =  np.hstack((np.ones((points * len(classes),1)),np.vstack((start_x1,start_x2)).T))

    def __get_y(self):
        y = []
        for c in range(0,len(self.classes)):
            zeroes = []
            for i in range(0, c * int(self.points / len(self.classes))):
                zeroes.append(0)
            ones = []
            for i in range(0,int(self.points / len(self.classes))):
                ones.append(1)
            zeroes1 = []
            for i in range(0, (len(self.classes) - (c + 1)) * int(self.points / len(self.classes)) ):
                zeroes1.append(0)    
            new_axes = np.array([[y] for y in np.hstack((np.hstack((zeroes,ones)), zeroes1))])
            if(len(y) == 0): 
                y = np.array(new_axes)
            else:
                y = np.hstack((y,new_axes))
        self.y = y
    def __gen_w(self):
        w = [10.,20.,30.]
        self.w = np.array([[w[c] for i in range(0,len(self.classes))] for c in range(0,3)] ) 
    def __sigmoid(self,x):
        return 1 / (1 + math.exp(-x))
    def fit(self,epochs,learning_rate,batch_size):
        err_points = []
        vec_sig = np.vectorize(self.__sigmoid)
        for i in range(1,epochs):
            predictions = vec_sig(self.x.dot(self.w))
            self.__calc_error(predictions)
            print(self.cur_error)
            err_points.append(self.cur_error)
            if self.draw_err:
                self.__draw_err(err_points, i)
            self.w-= learning_rate * self.__calcdelta(predictions, batch_size) / self.points
            #if self.draw_graph:
            #    self.__draw_graph(learning_rate)
    def __calcdelta(self,predictions,batch_size):
        indexes = (np.floor((np.random.random(batch_size) * self.points))).astype(int)
        random_preds = np.array([predictions[indexes[index]] for index in range(0,batch_size)])
        random_y = np.array([self.y[indexes[index]] for index in range(0,batch_size)])
        random_x = np.array([self.x[indexes[index]] for index in range(0,batch_size)])
        random_preds -= random_y
        delta = random_preds.T.dot(random_x)
        return delta.T
    def __calc_error(self,predictions):
        self.cur_error = -1/self.points*np.sum(self.y * np.log(predictions) + (1 - self.y)*np.log(1 - predictions))
    def __draw_err(self, err_points, iteration):
        #if self.draw_err:
        #    plt.subplot(211)
        plt.plot(np.arange(iteration),err_points, 'r')
        plt.draw()
    def __draw_graph(self, learning_rate):
        #if self.draw_graph:
        #    plt.subplot(212)
        r = np.arange(0,2*self.scale,learning_rate)
        for i in range(0,len(self.classes)):
            plt.plot(r, [(-self.w[i][0] - self.w[i][0] * t) / self.w[i][0] for t in r])
            plt.plot(self.classes[i].x1, self.classes[i].x2, 'o')
            plt.draw()
        plt.pause(0.1)
        plt.clf()


mu = [1, 3,4]
sigma = [0.5,0.5,0.5]
classes = [Class(x, 0.5, 100) for x in mu]
gauss = Model(len(classes) * 100,classes, max(mu[0],mu[1],mu[2]), draw_graph= True)
gauss.fit(10000,0.4,200)
print(gauss.y.shape)
print(gauss.x.shape)
print(gauss.w.shape)