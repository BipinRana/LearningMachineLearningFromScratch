import numpy as np

# Euclidean distance function
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2,axis=1))  # Squared difference between the coordinates

# Data points
data = np.array([
    [1, 2],
    [3, 4],
    [3, 3],
    [7, 8],
    [7, 7],
    [5, 6],
    [3, 3]
])

# Initial centroids
centroid_one = np.array([4.0, 3.0])
centroid_two = np.array([7.0, 6.0])
k=10
for i in range(k):
    cluster_one = euclidean_distance(data,centroid_one) < euclidean_distance(data,centroid_two)
    cluster_two = ~cluster_one #will only work for models with two centroids
    
    new_centroid_one = np.mean(data[cluster_one],axis=0)
    new_centroid_two = np.mean(data[cluster_two],axis=0)
    
    if ((np.allclose(centroid_one,new_centroid_one)) and (np.allclose(centroid_two,new_centroid_two))):
        break
    
    centroid_one = new_centroid_one
    centroid_two = new_centroid_two

print("Final Cluster Assignments:")
for idx, point in enumerate(data):
    print(f"Point {point} is assigned to Cluster {cluster_two[idx]+1}")#This code will also work for model with only two centroids

