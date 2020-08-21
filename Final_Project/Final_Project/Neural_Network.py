#from pygame.math import Vector2
#import __future__ 
#import tensorflow as tf
#import keras
#import numpy as np
#import matplotlib.pyplot as plt
#from keras.utils import plot_model

#class Neural_Network(object):

#    def __init__(self):
#        tf.keras.backend.clear_session()  # For easy reset of notebook state.
#        print(tf.__version__)
#        #creating a model
#        #model = keras.Sequential
#        #(
#        #    [
#        #        #keras.layers.Flatten(units=2, input_shape=[1]), #making array from 2 dimensional to one dimensional (flat, 28*28)
#        #        #keras.layers.Dense(2, activation= 'sigmoid', use_bias = True),   #in
#        #        #keras.layers.Dense(1, activation= 'softmax')    #out

#        #    ]
#        #)
#        #self.train_inputs = list(int(),int())
#        self.train_inputs = 0
#        #self.train_labels = list(int(),int())
#        self.train_target = 0
#        #self.x = keras.layers.Input(shape=(10,),name='Input')
#        #self.y = keras.layers.Dense(10, activation='sigmoid',name='First_Layer')(self.x)
#        #self.predictions = keras.layers.Dense(1,activation='softmax', name='Output')(self.y)
#        #self.model = keras.Model(inputs=self.x, outputs=self.predictions)
#        self.model = keras.Sequential()
#        self.model.add(keras.layers.Dense(24, input_dim=10, activation='relu'))
#        self.model.add(keras.layers.Dense(24, activation='relu'))
#        self.model.add(keras.layers.Dense(1, activation='linear'))

#        self.model.summary()

#        #plot_model(self.model, to_file="model.png")

#        self.model.compile(keras.optimizers.Adam(0.5), keras.losses.binary_crossentropy, metrics = ['accuracy'])

#    def Display_Object(self):
#        for i in enumerate(self.train_target):
#            print(i)

#    def Load_Weight(self, name):
#        self.model.load_weights(name)

#    def Save_Weight(self, name):
#        self.model.save_weights(name)

#    def Push_Train_Target(self, data):
#        #self.train_target.append(data)
#        self.train_target = data

#    def Push_Train_Inputs(self, data):
#        #self.train_inputs.append(data)
#        self.train_inputs = data

#    def Model_Fit(self):
#        #print(type(self.train_target))
#        self.model.fit(self.train_inputs,self.train_target, batch_size = 1, epochs = 10)
#        #self.model.fit(self.train_inputs, self.train_target ,epochs = 5, batch_size = 10)
#        #self.model.fit(self.train_target ,epochs = 1, batch_size = 10)

#    def Model_Predict(self,data):
#        #self.model.predict(data)
#        predictions = self.model.predict(data)
#        print(predictions[1])
#        #for i in enumerate(predictions):
#        #    print(i)
