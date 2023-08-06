import numpy as np

def MAPE(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def RMSE(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

def evaluate(origin, forecast):
    """Calculate RMSE and MAPE

    Args:
        origin (np.array): true value
        forecast (np.array): predicted value
    """
    print("RMSE", RMSE(origin, forecast))
    print("MAPE", MAPE(origin, forecast))