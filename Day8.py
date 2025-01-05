# Cross-validation is a technique used to assess the performance and generalization ability of a machine learning model. It involves splitting the dataset into multiple subsets (folds), 
# training the model on some folds, and testing it on the remaining folds. This process is repeated for each fold, and the results are averaged to provide a more reliable estimate of the model's performance. 
# It helps prevent overfitting and ensures that the model performs well on unseen data.
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Prepare for cross-validation
cv = KFold(n_splits=5, shuffle=True, random_state=42)

# List to store the mean accuracy for each k value
k_values = range(1, 21)  # Test k values from 1 to 20
mean_accuracies = []

# Loop through different values of k
for k in k_values:
    # Initialize the k-NN classifier with the current k
    knn = KNeighborsClassifier(n_neighbors=k)
    
    # Perform cross-validation and calculate the mean accuracy
    cv_scores = cross_val_score(knn, X, y, cv=cv, scoring='accuracy')
    mean_accuracies.append(np.mean(cv_scores))

# Plot the accuracy vs. k
plt.figure(figsize=(8, 6))
plt.plot(k_values, mean_accuracies, marker='o', linestyle='-', color='b')
plt.title("Effect of k on Accuracy in k-NN (Iris Dataset)")
plt.xlabel("Number of Neighbors (k)")
plt.ylabel("Mean Cross-Validation Accuracy")
plt.grid(True)
plt.show()
