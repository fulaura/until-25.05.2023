from keras.datasets import mnist
#download mnist data and split into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#Exploratory data analysis
import matplotlib.pyplot as plt
#plot the first image in the dataset
plt.imshow(X_train[0])

#check image shape
X_train.shape

#DATA PRE PROCESSING

#reshape data to fit ,odel
X_train = X_train.reshape(60000,28,28,1)
X_test = X_test.reshape(10000,28,28,1)

#Let's make each output category, and 
# binary variable is inputted for each category
from keras.utils import to_categorical;
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
y_train[0]
#I didn't get this part
array([0.,0.,0.,0.,0.,1.,0.,0.,0.,0.], dtype=float32)