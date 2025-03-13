import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error
from data_preprocessing import load_and_preprocess_data

X_train, X_test, y_train, y_test = load_and_preprocess_data("../data/student_data.csv")
model = joblib.load("../models/student_model.pkl")

def evaluate_model():
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    
    print(f"Mean Absolute Error: {mae}")
    print(f"Mean Squared Error: {mse}")

if __name__ == "__main__":
    evaluate_model()
