import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)

    # Handling missing values
    df.fillna(df.mean(), inplace=True)

    # Encoding categorical variables
    df = pd.get_dummies(df, drop_first=True)

    # Splitting data into train and test sets
    X = df.drop(columns=['skill_score'])
    y = df['skill_score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test
