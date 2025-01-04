#More depth on feature scaling
import numpy as np
a=np.array([[5,60000],[9,90000],[2,30000],[1,20000],[7,50000],[1,15000],[6,50000],[2,35000],[3,25000],[8,60000],[4,40000]],dtype=float) #Sample data for now

a[:,0] = (a[:,0] - a[:,0].mean())/a[:,0].std()
a[:,1] = (a[:,1] - a[:,1].mean())/a[:,1].std()
print(a)

a=np.array([[5,60000],[9,90000],[2,30000],[1,20000],[7,50000],[1,15000],[6,50000],[2,35000],[3,25000],[8,60000],[4,40000]],dtype=float) #Sample data for now

#Now by creating a function for generalizing the process for n number of columns
def standardscaling(array_name):
    for  i in range (array_name.shape[1]):
        array_name[:,i] = (array_name[:,i] - array_name[:,i].mean())/array_name[:,i].std()
    return array_name
print(standardscaling(a))

#Let's use the sklearn's standard scaler to transform the data now
from sklearn.preprocessing import StandardScaler
new_a = StandardScaler().fit_transform(a)
print(new_a)

# Now we will also see the effects of StandardScaler and also why it is important.

import pandas as pd

# Load the data
df = pd.read_csv('Social_Network_Ads.csv')

# Extract features and target
X = df[['Age', 'EstimatedSalary']]
Y = df['Purchased']

# Split the data
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)


# Initialize the scaler and fit on the training data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

# Transform the data
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

print('Mean of scaled X_train: ',np.mean(X_train_scaled,axis=0))
print('Std of scaled X_train: ',np.std(X_train_scaled,axis=0))
print('Mean of scaled X_test: ',np.mean(X_test_scaled,axis=0))
print('Std of scaled X_test: ',np.std(X_test_scaled,axis=0))
# By the result of above, we will be able to see that the result of standardization will result in mean=0 and standard_deviation = 1.
# Now, let's train the **Support Vector Classifier (SVC)** model on both the original (unscaled) data and the scaled data to compare the performance of the models.
# We chose SVC model since it is more sensitive to feature scaling
from sklearn.svm import SVC
Model = SVC()  
Model_Scaled = SVC()  

# Fit the models
Model.fit(X_train, Y_train) 
Model_Scaled.fit(X_train_scaled, Y_train)  

# Make predictions
y_pred = Model.predict(X_test)  
y_pred_scaled = Model_Scaled.predict(X_test_scaled) 

# Now, we will compare the accuracy of the two models (with and without scaling).
from sklearn.metrics import accuracy_score
print('Accuracy Without Scaling: ', accuracy_score(Y_test, y_pred))
print('Accuracy With Scaling: ', accuracy_score(Y_test, y_pred_scaled))
