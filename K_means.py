import numpy as np

# Euclidean distance function
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))  # Squared difference between the coordinates

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
centroid_one = np.array([2, 3], dtype=float)
centroid_two = np.array([7, 6], dtype=float)

# Iterate for a fixed number of times (for simplicity)
for _ in range(10):
    cluster_data = []  # Use a list to store points and their assigned cluster

    # Assign points to the nearest centroid
    for i in range(len(data)):
        dist_centroid_one = euclidean_distance(data[i], centroid_one)
        dist_centroid_two = euclidean_distance(data[i], centroid_two)
        if dist_centroid_one < dist_centroid_two:
            cluster_data.append([data[i][0], data[i][1], 1])  # Append to list
        else:
            cluster_data.append([data[i][0], data[i][1], 2])  # Append to list

    # Convert list to NumPy array for processing
    cluster_data = np.array(cluster_data)

    # Check for convergence
    new_centroid_one = cluster_data[:,:2][cluster_data[:,2] == 1].mean(axis=0)
    new_centroid_two = cluster_data[:,:2][cluster_data[:,2] == 2].mean(axis=0)
    
    if np.allclose(centroid_one, new_centroid_one) and np.allclose(centroid_two, new_centroid_two):
        break

    # Update centroids based on the assigned points
    centroid_one = new_centroid_one
    centroid_two = new_centroid_two

# Print final clusters and their assignments
for i in range(len(data)):
    print(f"{data[i]} cluster {int(cluster_data[i][2])}")
