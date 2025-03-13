import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Create sample data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([2, 4, 6, 8, 10])

# Create a pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

# Try cross-validation
try:
    cv_rmse = np.sqrt(-cross_val_score(pipeline, X, y, cv=5, scoring='neg_mean_squared_error'))
    print(f'Cross-validated RMSE: {cv_rmse}')
    print(f'Mean RMSE: {cv_rmse.mean()}')
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    
    # Try to debug
    print("\nDebugging information:")
    try:
        # Try with a simpler cross-validation
        scores = cross_val_score(LinearRegression(), X, y, cv=2)
        print(f"Simple cross-validation works: {scores}")
    except Exception as e2:
        print(f"Simple cross-validation also fails: {type(e2).__name__}: {e2}")