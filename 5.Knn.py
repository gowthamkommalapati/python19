# K-Nearest neighbor implementation

import math
 
# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(n1-1):
        distance += (row1[i] - row2[i])**2
    return math.sqrt(distance)
 
# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    print('distances from neighbors to given data point')
    print(distances)
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
     
    return neighbors
 
# Make a classification prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    print('Neighbors of given data point are\n')
    print(neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction
 
dataset=[];
n=int(input('enter no of data points'));
n1=int(input('enter no of dimensions in a dataset along with class label attribute'));
print('attr1,aatr2,.....attrn(class label)')
for i in range(n):
    print('enter attribute values for point',i);
    dataset.append([]);
    counter=0;
    while counter<n1:
        b=float(input('enter value for each dimension'));
        counter=counter+1;
        dataset[i].append(b);
print('Given points in data set are')
print(dataset);
print('Enter a new data point to assign a label')
p=[];
i=0
n=n1-1
while i<n:
    k=float(input('enter data point elements'))
    p.append(k)
    i=i+1
print('Enter K no.of neighbors')
k=int(input())
prediction = predict_classification(dataset,p, k)
print('The assigned label for the given data point is is',prediction)
