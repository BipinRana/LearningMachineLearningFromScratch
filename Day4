Day4: More on Data Preprocessing

1. Handling Outliers and Anomalies: Outliers and Anomalies are similar concept. Anomalies are unknown data that are impossible. Lets I usually live in NewYork and I last logged in at 8pm. If there is a login request at 8:15pm from Somalia,
                                    that would be physically impossible and hence it is an anomaly. Outliers however are extreme conditions but possible. In a neighborbood of middle class people with salary of 50k usd, there may also reside
                                    a rich business man who earns 5million usd a month. It is possible but it still skews the data variables like mean, variance, standard variation and mean square error. Thus. it is a good idea to deal with 
                                    them during the preprocessing stage. The ways of detecting them are by visualizing them through scatterplots,box plots or through statistical measures.
                                    There are also several ways of dealing with them. They are:
                                        -Remove Outliers: We can delete outliers if they are due to data entry errors or irrelevant to our analysis. but removing legitimate data can also reduce model robustness.
                                        -Transform the Data:We can apply logarithmic, square root, or Box-Cox transformations to compress extreme values.
                                        -Cap/Floor Values: By applying a limit to the extreme values
                                        -Impute Outliers: We can replace outliers with the mean, median, or mode of the feature.
                                        -Use Robust Models: We can use some algorithms, like Decision Trees and Random Forests, which are less sensitive to outliers.

2. Feature Engineering: Feature engineering refers to the method of choosing and creating the correct features. We can explore techniques to create new features from existing ones, such as polynomial features, 
                        logarithmic transformations, or interaction terms that might improve our regression model. or, We can use algorithms to remove/ add features from already existing features which are 
                        Forward Selection, Backward Elimination, Combined algorithms. Whereas some regression model like Lasso algorithm already come with techniques to engineer the features

3. Feature Scaling: Scaling or feature scaling is the methodology that is used to ensure that independent variables are taken within the same range so that they can have the same contributions to the models. 
                    It helps to improve the performance of the model and the convergence rate by bringing the feature values to a common scale. Algorithms such as Min-Max Scaling and Standardization are more relevant particularly for SVMs 
                    and K-Means algorithms that are sensitive to the magnitude of features. This area of study would be good to research in order to establish how it affects various types of models and datasets.

4. Encoding Categorical Variable: Categorical variables are the non numerical variables which cannot be directly used in the model since they certainly donot have the numeric value. They are of two types: Ordinal and Non-Ordinal.
                                  Ordinal categorical variables can be ordered in ascending/descending while the non-ordinal cannot be. Furthermore two of the most prominent encoding methods are Label Encoding and One Hot Encoding.
                                  Label Encoding is a method where the variables assigned a numerical value. Suppose the categorical variables are New York,New Delhi,Beijing,Colombo, then they will be represented by 1,2,3,4 respectively.
                                  It is efficient, however there can be slight error as there is implication that Colombo>Beijing>New Delhi>New Yerk due to numeric value assigned. This is fixed by OneHot Encoding as it creates each variable
                                  to new column. If the location is New Delhi for data1, then the column New Delhi has value 1 and the others have 0. This makes OneHot Encoding a better choice for non-ordinal categorical variables as it 
                                  avoids introducing any unintended order or hierarchy among the categories. However, it comes at the cost of increased dimensionality, especially when there are a large number of categories. 
                                  Each category adds a new column, potentially leading to a sparse dataset, which can increase computational complexity and memory usage.
                                    -Label Encoding is simpler and works well for ordinal variables, where the inherent order is meaningful.
                                    -OneHot Encoding is preferred for non-ordinal variables to avoid introducing false relationships, albeit at the expense of increased dimensionality.

