import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import sys

print(f"Python version: {sys.version}")
print(f"NumPy version: {np.__version__}")
try:
    import sklearn
    print(f"scikit-learn version: {sklearn.__version__}")
except ImportError:
    print("scikit-learn not installed")

# Create sample data - make it a bit more complex
X = np.random.rand(100, 5)  # 100 samples, 5 features
y = np.random.rand(100)     # 100 target values

# Create a pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

# Try cross-validation with different CV values
for cv in [2, 3, 5]:
    try:
        print(f"\nTrying cross-validation with cv={cv}")
        cv_rmse = np.sqrt(-cross_val_score(pipeline, X, y, cv=cv, scoring='neg_mean_squared_error'))
        print(f'Cross-validated RMSE: {cv_rmse}')
        print(f'Mean RMSE: {cv_rmse.mean()}')
    except Exception as e:
        print(f"Error with cv={cv}: {type(e).__name__}: {e}")
        
# Try with different scoring metrics
for scoring in ['neg_mean_squared_error', 'neg_mean_absolute_error', 'r2']:
    try:
        print(f"\nTrying cross-validation with scoring='{scoring}'")
        scores = cross_val_score(pipeline, X, y, cv=3, scoring=scoring)
        print(f'Scores: {scores}')
        print(f'Mean score: {scores.mean()}')
    except Exception as e:
        print(f"Error with scoring='{scoring}': {type(e).__name__}: {e}")

# Try without pipeline
print("\nTrying cross-validation without pipeline")
try:
    cv_rmse = np.sqrt(-cross_val_score(LinearRegression(), X, y, cv=5, scoring='neg_mean_squared_error'))
    print(f'Cross-validated RMSE: {cv_rmse}')
    print(f'Mean RMSE: {cv_rmse.mean()}')
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")