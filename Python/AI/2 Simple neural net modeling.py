from numpy import exp, array, random, dot
#XOR table we use as input to train neurons
training_set_inputs = array ([[0,0,0],[1,1,1],[1,0,1],[0,1,1]])
#XOR table OUTPUT to complete logics
training_set_outputs = array ([[0,1,1,0]]).T
random.seed(1)
#Random initial weights.
#We assign random weights to a 3 x 1 matrix, with values in the 
# range -1 to 1 # and mean 0
synaptic_weights=2*random.random((3,1))-1
#Train neural net to Logic
for iteration in range(10000):
    #sigmoid formula
    output=1/(1+exp(-(dot(training_set_inputs,synaptic_weights))))
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs-output)*output*(1-output))
print(1/(1+exp(-(dot(array([1,0,0]),synaptic_weights)))))    