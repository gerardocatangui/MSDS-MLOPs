from sklearn.metrics import mean_squared_error

def evaluate_model(actuals, predictions):
    return mean_squared_error(actuals, predictions, squared=False)