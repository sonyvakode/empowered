import joblib
from sklearn.ensemble import RandomForestRegressor
from data_preprocessing import load_and_preprocess_data

X_train, X_test, y_train, y_test = load_and_preprocess_data("../data/student_data.csv")

def train_model():
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save the trained model
    joblib.dump(model, "../models/student_model.pkl")
    print("Model training completed and saved.")

if __name__ == "__main__":
    train_model()
