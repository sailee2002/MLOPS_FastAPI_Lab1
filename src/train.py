from sklearn.ensemble import RandomForestClassifier
import joblib
from data import load_data, split_data
from pathlib import Path

def fit_model(X_train, y_train):
    """
    Train a Random Forest Classifier and save the model to a file.
    Args:
        X_train (numpy.ndarray): Training features.
        y_train (numpy.ndarray): Training target values.
    """
    # creating and fitting model
    rf_classifier = RandomForestClassifier(
        n_estimators=100,       # number of trees
        max_depth=None,         
        random_state=12
    )
    rf_classifier.fit(X_train, y_train)

    # saving the model in src/model/iris_model.pkl
    model_path = Path(__file__).resolve().parent / "model" / "iris_model.pkl"
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(rf_classifier, model_path)
    print(f"Model trained and saved to: {model_path}")

if __name__ == "__main__":
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    fit_model(X_train, y_train)

