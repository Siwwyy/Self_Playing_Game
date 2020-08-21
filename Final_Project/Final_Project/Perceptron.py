import numpy as np
import pygame, sys
import random

class Perceptron(object):
    """description of class"""
    def __init__(self, output):
        self.training_inputs = np.array([[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1]])
        self.training_outputs = output
        self.outputs = 0
        np.random.seed(1)

        self.synaptic_weights = 2 * np.random.random((10,1)) - 1

        for iteration in range(10):

            input_layer = self.training_inputs

            self.outputs = self.sigmoid(np.dot(input_layer, self.synaptic_weights))

            error = self.training_outputs - self.outputs

            adjustments = error * self.sigmoid_derivative(self.outputs)
            self.synaptic_weights += np.dot(input_layer.T, adjustments)


    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def sigmoid_derivative(self,x):
        return x * (1 - x)

    def Get_Output(self):
        return self.outputs

    def Update_training_outputs(self, data):
        training_outputs = data