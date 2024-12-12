Day 3 : Multiple Linear Regression
Well, the vectors or rather the end results that we are seeking are not always influenced by just one feature. 
For example, if we are looking to predict the rent prices in different states of a nation, the price itself maybe influenced by factors like Living Cost, Bedrooms, Bathrooms and many others.

Simple Linear Regression: 
    - The model uses one feature and follows the formula: 
        y = mx + c
            y: Predicted outcome (dependent variable)
            x: Independent variable (feature)
            m: Slope, indicating the change in y with respect to x
            c: Intercept, representing the default value of y when x = 0

Multiple Linear Regression:
    - In this case, we consider multiple features (x₁, x₂, ..., xₙ), leading to the formula:
        y = c + m₁x₁ + m₂x₂ + ... + mₙxₙ

Since we factor in multiple features ,the formula that we get is y=c+m1*x1+m2*x2+...+mn*xn. The assumptions that we make are similar to the simple linear regression. They go as follows:
1) Linearity : The features should have linear relationship with the vector. The cases of trigonometric/exponential relations cause underfitting/overfitting cases which causes our model to contain more errors.
2) homoscedasticity : Homoscedasticity describes a situation in which the error term (that is, the “noise” or random disturbance in the relationship between the independent variables and the dependent variable) is the same across all values of the independent variables.
3) Multivariate normality : This is a statistical concept and here we assume that our residual errors or noise are normally distributed.
4) Multicollinearity : Multi collinearity is a relation between the factors x through xn, where value of a feature(x) has some effect on any other features(xn). Such relation must not exist within our data to reduce redundancy.

Common Misconceptions:
A misconception I initially had was that, since simple linear regression uses a 2D line (y = mx + c), the formula for multiple linear regression (y = c + m₁x₁ + m₂x₂ + ... + mₙxₙ) would also represent a 2D system.
I assumed it was simply the sum of multiple features calculated independently. 
However, this is not the case. For n features, the model operates in an n + 1-dimensional space. The relationship between the dependent variable (y) and the independent variables (x₁, x₂, ..., xₙ) is computed collectively, not feature by feature.

Why Visualization Matters
To truly grasp this concept, imagine a 2D line from simple linear regression being extended into higher dimensions:
    - With 2 features (x₁, x₂), the model represents a plane in 3D space.
    - With n features, the model exists in n + 1-dimensional space, which is challenging to visualize but helps explain how all features influence y simultaneously.

A visual representation—such as 3D plots or animations—would make this abstract concept more tangible and easier to understand.
