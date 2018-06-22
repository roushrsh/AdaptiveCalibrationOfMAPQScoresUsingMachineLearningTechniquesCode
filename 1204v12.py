import numpy
import tensorflow as tf
import random as rn

#from numpy.random import seed
import os
os.environ['PYTHONHASHSEED'] = '0'

numpy.random.seed(66)
rn.seed(66)

session_conf = tf.ConfigProto(intra_op_parallelism_threads=1, inter_op_parallelism_threads=1)
from keras import backend as K
tf.set_random_seed(66)
sess = tf.Session(graph=tf.get_default_graph(), config=session_conf)
K.set_session(sess)


from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras import regularizers






#import pandas as pd

toWriteTo = open("DeepPercents1204v12.txt", "w")

#ToLearn
dataset = numpy.loadtxt("13of1MToLearnFrom.csv", delimiter=",")
X = dataset[:,0:13]
Y = dataset[:,13]

#ToTest
dataset2 = numpy.loadtxt("13of10MToTestOn.csv",delimiter=",")
X2 = dataset2[:,0:13]
Y2 = dataset2[:,13]


model = Sequential()
model.add(Dense(14, input_dim=13, activation='relu'))
model.add(Dropout(0.6))
model.add(Dense(9, activation='relu'))
model.add(Dropout(0.6))
#model.add(Dropout(0.5))
model.add(Dense(9, activation='relu'))
model.add(Dropout(0.6))
model.add(Dense(9, activation='relu'))
model.add(Dropout(0.6))
model.add(Dense(1, activation='sigmoid'))




# Compile model
model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])
#model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
#model.compile(loss='binary_crossentropy', optimizer='Adagrad', metrics=['accuracy'])

# Fit the model
model.fit(X, Y, epochs=1, batch_size=8)

# evaluate the model
#scores = model.evaluate(X2, Y2)
#print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

prediction = (model.predict(X2))
for x in prediction:
	toWriteTo.write(str(x))
	toWriteTo.write("\n")


##Results on Training Set
#Epoch 150
#with 1x8 hidden layers got 98.90% accurracy
#with 2x8 hidden layers got 98.91% accurracy
#with 3x8 hidden layers got 98.91% accurracy

#Epoch 150
#with 2x10 hidden layers got 98.38% accurracy


##Results on Testing Set

#Epoch 150
#with 2x8 hidden layers got 99.00% Accurracy
#with 3x8 hidden layers got 99.00% Accurracy

