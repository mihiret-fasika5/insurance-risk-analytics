## Models to Implement
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


def evaluate_regression(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)

    return {
        "model": model.__class__.__name__,
        "RMSE": rmse,
        "R2": r2
    }

