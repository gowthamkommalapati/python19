# ANN implementation
from random import seed
from random import random
import math
 
# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
    network = list()
    hidden_layer = [{'weights':[random() for i in range(n_inputs+1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'weights':[random() for i in range(n_hidden+1)]} for i in range(n_outputs)]
    network.append(output_layer)
    return network
 
# Calculate neuron activation for an input
def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i] * inputs[i]
    return activation
 
# Transfer neuron activation
def transfer(activation):
    return 1.0 / (1.0 + math.exp(-activation))
 
# Forward propagate input to a network output
def forward_propagate(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = transfer(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs
 
# Calculate the derivative of an neuron output
def transfer_derivative(output):
    return output * (1.0 - output)
 
# Backpropagate error and store in neurons
def backward_propagate_error(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = list()
        if i != len(network)-1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += (neuron['weights'][j] * neuron['delta'])
                errors.append(error)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(neuron['output'] - expected[j])
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])
 
# Update network weights with error
def update_weights(network, row, l_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i - 1]]
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron['weights'][j] -= l_rate * neuron['delta'] * inputs[j]
            neuron['weights'][-1] -= l_rate * neuron['delta']
 
# Train a network for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
    for epoch in range(n_epoch):
        sum_error = 0
        for row in train:
            outputs = forward_propagate(network, row)
            expected = [0 for i in range(n_outputs)]
            expected[row[-1]] = row[-1]
            sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
            backward_propagate_error(network, expected)
            update_weights(network, row, l_rate)
        print('\nAt Iteration=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
 
# Training backprop algorithm
seed(1)
print('\n Details of Intialized Neural Network Structure\n')
#Buys_computer data set
#dataset=[[1,0,0,0,0],[0,1,0,0,1]]
# play tennis data set
dataset=[[1,0,0,0,0], [1,0,0,1,0], [0.5,0,0,0,1], [0,0.5,0,0,1], [0,1,1,0,1], [0,1,1,1,0], [0.5,1,1,1,1], [1,0.5,0,0,0], [1,0.5,1,0,1], [0,0.5,1,0,1], [1,0.5,1,1,1], [0.5,0.5,0,1,1], [0.5,1,1,0,1]]
#wheat classificatio ndata set
#dataset = [[2.7810836,2.550537003,0],[1.465489372,2.362125076,0],[8.675418651,-0.242068655,1],[7.673756466,3.508563011,1]]
n_inputs = len(dataset[0])-1
print('Neurons at input layer',n_inputs)
n_hidden=2
print('Neurons at hidden layer',n_hidden)
output1_values1=set([row[-1] for row in dataset])
n_outputs = len(set([row[-1] for row in dataset]))
print('Neurons at output layer',n_outputs)
print('\n The output values in the training examples',output1_values1)
print('\n')
network = initialize_network(n_inputs, n_hidden, n_outputs)
print('\n Intialized weights')

i= 1
for layer in network:
    j=1
    for sub in layer:
        print("\n Layer[%d] Node[%d]:\n" %(i,j),sub) 
        j=j+1
    i=i+1


lrate=0.5

n_iter=10
print('\n Intialized weights')  


print('\n')
print('learning rate and error values at each iteration')
train_network(network, dataset, lrate,n_iter, n_outputs)
print('\n')
print('\n Results of updated Weights,Outputs, delta(ERROR) values at each node of layer in ANN after training \n')
i= 1
for layer in network:
    j=1
    for sub in layer:
        print("\n Layer[%d] Node[%d]:\n" %(i,j),sub) 
        j=j+1
    i=i+1

sample=[]
print("\n enter the sample values in the given order\n Oulook,Temp,Humidity,Wind\n")
test=list(int(i) for i in input().split())
sample.append(test)
    
        
def train_network1(network, train, l_rate=0.9, n_epoch=1, n_outputs=2):
    for epoch in range(n_epoch):
        sum_error = 0
        print(train)
        for row in train:
            outputs = forward_propagate(network, row)
            print(outputs)
            if max(outputs)==outputs[1]:
              print("Assigned labelled for ",row,"is YES")
            else:
               print("Assigned labelled for ",row,"is NO")

train_network1(network, sample)  
