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
