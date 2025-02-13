# KNN(K nearest neighbor) is a supervised machine learning technique. It classifies a data based on its peer. In other words, by using the closest k data rows, it uses the label
# of the mode's(highest frequency). The closest data as I have said is calculated based on the Euclidean distance.
# One of it's limitation is that Taking a large k causes underfitting as the model the decision becomes less influenced by specific nearby points and more by the overall 
# majority class in the neighborhood. With a small 𝑘(e.g., 𝑘=1, the model makes predictions based solely on the single nearest neighbor.
#If this point is an outlier or noisy, the prediction will reflect that error.
import numpy as np
X_train = np.array([
    [2,3],
    [1,1],
    [2.5,2],
    [6,6],
    [7,7],
    [5.5,5.5]
])

y_train = np.array([0,0,0,1,1,1])

x_new = np.array([5,6])

def euclidean_distance(x1,x2):
    return np.sqrt(np.sum((x1 - x2)**2))

def get_neighbours(X,Y,X_new,k):
    distances = []
    for i in range(len(X)):
        dist= euclidean_distance(X[i],X_new)
        distances.append((dist,Y[i]))

    distances.sort(key =lambda x:x[0])
    neighbors = [distances[i][1] for i in range(k)]
    return neighbors

def predict(X,y,X_new,k):
    neighbors = get_neighbours(X,y,X_new,k)
    counts = np.bincount(neighbors)
    return np.argmax(counts)
    

print(predict(X_train,y_train,x_new,3))

import matplotlib.pyplot as plt

for label in np.unique(y_train):
    plt.scatter(X_train[y_train==label][:,0],X_train[y_train == label][:,1],label=f"Class {label}")

plt.scatter(x_new[0],x_new[1],color='red',label='New Point',marker='x',s=100)
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.show()
