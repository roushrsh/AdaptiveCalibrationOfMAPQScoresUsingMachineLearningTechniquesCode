import numpy
import tensorflow as tf
import random as rn
#from numpy.random import seed
import os
os.environ['PYTHONHASHSEED'] = '0'

#Need to set up seeds before importing as per keras manual else your results won't be reproducible. I lost many results due to this. Also multicore has to be changed to single thread for the same reason, also a point of error that has to be controlled.
numpy.random.seed(178)
rn.seed(178)

session_conf = tf.ConfigProto(intra_op_parallelism_threads=1, inter_op_parallelism_threads=1)
from keras import backend as K
tf.set_random_seed(178)
sess = tf.Session(graph=tf.get_default_graph(), config=session_conf)
K.set_session(sess)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras import regularizers

#file to write to
toWriteTo = open("NNDLResults.txt", "w")

#ToLearn
dataset = numpy.loadtxt("50MToLearnFrom13Features.csv", delimiter=",")
X = dataset[:,0:13]
Y = dataset[:,13]

#ToTest
dataset2 = numpy.loadtxt("13of10MToTestOn.csv",delimiter=",")
X2 = dataset2[:,0:13]
Y2 = dataset2[:,13]

#Actual network. Here we start with 14, three hidden layers of 9, with one output of sigmoid 0 : 1
model = Sequential()
model.add(Dense(14, input_dim=13, activation='relu'))
model.add(Dense(9, activation='relu'))
model.add(Dense(9, activation='relu'))
model.add(Dense(9, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


#Below are some extra settings I've tested.

#model.add(Dense(14, input_dim=13, kernel_regularizer=regularizers.l2(0.01), activity_regularizer=regularizers.l1(0.01)))
#model = Sequential()
#model.add(Embedding(13, 64))
#model.add(LSTM(100))
#model.add(Dropout(0.5))
#model.add(Dense(1, activation='sigmoid'))
#model.compile(loss='binary_crossentropy', optimizer='adam', #metrics=['accuracy'])


# Compile model
model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])
# Fit the model Epochs and batch size vary results greatly
model.fit(X, Y, epochs=5, batch_size=32)

#actual prediction
prediction = (model.predict(X2))

#write file
for x in prediction:
	toWriteTo.write(str(x))
	toWriteTo.write("\n")

