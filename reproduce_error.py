import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import pandas as pd

# Create sample data to mimic the housing dataset
np.random.seed(42)
X = np.random.rand(1000, 8)  # 1000 samples, 8 features like the housing dataset
y = np.random.rand(1000)     # 1000 target values

# Create a pipeline similar to what the user might be using
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

# Try to reproduce the exact error
try:
    # This is the line that's causing the error in the user's code
    cv_rmse = np.sqrt(-cross_val_score(pipeline, X, y, cv=5, scoring='neg_mean_squared_error'))
    print(f'Cross-validated RMSE: {cv_rmse}')
    print(f'Mean RMSE: {cv_rmse.mean()}')
    
    # Analyze the residuals and their normality
    # This is the next line in the user's code
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    
    # Print detailed error information
    import traceback
    traceback.print_exc()
    
    # Try to debug
    print("\nDebugging information:")
    print(f"X shape: {X.shape}")
    print(f"y shape: {y.shape}")
    print(f"X type: {type(X)}")
    print(f"y type: {type(y)}")
    
    # Check if X or y contain NaN values
    print(f"X contains NaN: {np.isnan(X).any()}")
    print(f"y contains NaN: {np.isnan(y).any()}")
    
    # Try with a simple cross-validation
    try:
        scores = cross_val_score(LinearRegression(), X, y, cv=2)
        print(f"Simple cross-validation works: {scores}")
    except Exception as e2:
        print(f"Simple cross-validation also fails: {type(e2).__name__}: {e2}")