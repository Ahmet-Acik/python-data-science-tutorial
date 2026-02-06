"""
Scikit-learn Introduction: Linear Regression Basics

Scikit-learn is a powerful machine learning library for Python.
This script demonstrates simple linear regression.
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# Create sample data: y = 2x + noise
np.random.seed(42)  # For reproducibility
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = 2 * X.ravel() + np.random.normal(0, 1, size=X.shape[0])  # Add some noise

print("Sample data:")
for i in range(len(X)):
    print(f"X: {X[i][0]}, y: {y[i]:.2f}")

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Print model parameters
print(f"\nSlope (coefficient): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

# Make predictions
X_test = np.array([[11], [12]])
predictions = model.predict(X_test)

print(f"\nPredictions:")
for i in range(len(X_test)):
    print(f"X: {X_test[i][0]}, Predicted y: {predictions[i]:.2f}")

# Evaluate with training data (not ideal, but for demo)
from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"\nModel Evaluation on Training Data:")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

print("\nLinear regression fits a line to the data to predict continuous values.")