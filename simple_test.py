import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Create sample data
X = np.random.rand(100, 5)
y = np.random.rand(100)

# Create a pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

# Try cross-validation
try:
    cv_rmse = np.sqrt(-cross_val_score(pipeline, X, y, cv=5, scoring='neg_mean_squared_error'))
    print(f'Cross-validated RMSE: {cv_rmse}')
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")