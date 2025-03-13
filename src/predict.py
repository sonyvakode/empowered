import joblib
import pandas as pd

def predict_skill_score(input_data):
    model = joblib.load("../models/student_model.pkl")
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return prediction[0]

if __name__ == "__main__":
    sample_input = {'study_hours': 5, 'project_experience': 3, 'attendance': 90}
    predicted_score = predict_skill_score(sample_input)
    print(f"Predicted Skill Score: {predicted_score}")
