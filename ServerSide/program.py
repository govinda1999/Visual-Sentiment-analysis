from sklearn.neural_network import MLPClassifier
from sklearn.utils import shuffle
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

dataset = pd.read_csv("final11.csv")
dataset=dataset.values
np.random.shuffle(dataset)
x=dataset[:,:-1]
y=dataset[:,-1]
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.33, random_state=42)


model=MLPClassifier(activation='relu', alpha=0.001,epsilon=1e-08,hidden_layer_sizes=(200,),learning_rate_init=0.001, max_iter=500000,solver='sgd', tol=0.0001, validation_fraction=0.1)

model.fit(xtrain,ytrain)

#MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,beta_2=0.999, early_stopping=False, epsilon=1e-08,hidden_layer_sizes=(15,), learning_rate='constant',learning_rate_init=0.001, max_iter=2000, momentum=0.9,nesterovs_momentum=True, power_t=0.5, random_state=None,shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,verbose=False, warm_start=False)
test_accuracy = model.score(xtest,ytest)
print(test_accuracy)
train_accuracy = model.score(xtrain,ytrain)
print(train_accuracy)
#print(model.predict([[4.333333,1.039,3.333333,2.888888,2.533333,0.5873,3.1111,4.416666]]))

#print(model.predict([[8.66666,1.4411,10.0,8.0,5.6,0.66666,5.5,5.3333]])) #
print(model.predict([[5.5,1.9354,3.0,7.0,2.6,0.3571,3.0,3.25]]))
