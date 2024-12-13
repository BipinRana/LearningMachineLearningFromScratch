import pandas as pd
import numpy as np
import random
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

# Generate random data with missing values
locations = ['Downtown', 'Suburbs', 'City Center', 'Uptown', 'Riverside']
furnished_options = ['Yes', 'No']

data = {
    'Location': [random.choice(locations) for _ in range(100)],
    'Size (sqft)': [random.randint(800, 2000) if random.random() > 0.1 else np.nan for _ in range(100)],
    'Bedrooms': [random.randint(1, 5) if random.random() > 0.1 else np.nan for _ in range(100)],
    'Bathrooms': [random.randint(1, 3) if random.random() > 0.1 else np.nan for _ in range(100)],
    'Furnished': [random.choice(furnished_options) if random.random() > 0.1 else np.nan for _ in range(100)],
    'Rent (USD)': [random.randint(800, 3000) for _ in range(100)]
}

# Create DataFrame
df = pd.DataFrame(data)

#Handling Missing Values
imputer = SimpleImputer(strategy="median")
processed_features = ['Size (sqft)', 'Bedrooms', 'Bathrooms']
df[processed_features] = imputer.fit_transform(df[processed_features])

#Detecting and Handling Outliers (IQR Method)
def handle_outliers_iqr(df, columns):
    for column in columns:
        Q1 = df[column].quantile(0.25)  # First quartile (25%)
        Q3 = df[column].quantile(0.75)  # Third quartile (75%)
        IQR = Q3 - Q1  # Interquartile range

        # Define bounds for outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Clip outliers to the bounds
        df[column] = df[column].clip(lower_bound, upper_bound)
    return df

#Applying outlier handling to numerical features
numerical_features = ['Size (sqft)', 'Bedrooms', 'Bathrooms', 'Rent (USD)']
df = handle_outliers_iqr(df, numerical_features)

#Label Encoding
df['Furnished_Label'] = LabelEncoder().fit_transform(df['Furnished'])
df.drop(columns=['Furnished'], inplace=True)
# OneHot Encoding
onehot_encoder = OneHotEncoder(sparse_output = False)  
location_encoded = onehot_encoder.fit_transform(df[['Location']])
location_encoded_df = pd.DataFrame(location_encoded, columns=onehot_encoder.get_feature_names_out(['Location']))

# Concatenate OneHotEncoded columns to the DataFrame
df = pd.concat([df, location_encoded_df], axis=1)
df.drop(columns=['Location'], inplace=True)

#Feature Scaling
#1. Min-Max Scaling
df_minmax_scaled = MinMaxScaler().fit_transform(df)
df_minmax_scaled = pd.DataFrame(df_minmax_scaled, columns=df.columns)

#2. Standardization
df_standard_scaled = StandardScaler().fit_transform(df)
df_standard_scaled = pd.DataFrame(df_standard_scaled, columns=df.columns)

#Splitting Data for Model Training
X = df.drop(columns=['Rent (USD)'])
y = df['Rent (USD)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Output Sections
print("Original Data after Outlier Handling:")
print(df.head())
print("\nMin-Max Scaled Data:")
print(df_minmax_scaled.head())
print("\nStandardized Data:")
print(df_standard_scaled.head())
print("\nTraining Data (Features):")
print(X_train.head())
print("\nTraining Data (Target):")
print(y_train.head())
