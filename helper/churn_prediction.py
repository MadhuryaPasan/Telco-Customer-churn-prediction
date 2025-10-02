import numpy as np

# --- Load Model ---
from tensorflow import keras

# Define the filename you used earlier
mlp_model_filename = "helper/telco_churn_prediction_model_V1.0.keras"

# Load the saved model
loaded_model_mlp = keras.models.load_model(mlp_model_filename)



import joblib
LogisticRegression_model_filename = 'helper/logistic_regression_model.joblib'
loaded_model_LogisticRegression = joblib.load(LogisticRegression_model_filename)

def predict_new_customer_churn_mlp(customer_data, threshold=0.5):
    # 1. Convert the list/array to a NumPy array
    data_array = np.array(customer_data, dtype=np.float32)

    # 2. Reshape the array to (1, 46) to match the model's expected input shape (samples, features)
    X_new = data_array.reshape(1, -1)

    # 3. Generate the probability prediction
    probability = loaded_model_mlp.predict(X_new, verbose=0)[0][0]

    # 4. Apply the classification threshold
    prediction = 1 if probability >= threshold else 0
    class_label = "Churn" if prediction == 1 else "Not Churn"

    

    return prediction, probability, threshold ,class_label




def predict_new_customer_churn_LogisticRegression(customer_data, threshold=0.5):
    import numpy as np
    # Convert input to numpy array
    data_array = np.array(customer_data, dtype=np.float32).reshape(1, -1)

    # Get churn probability (probability of class 1)
    probability = loaded_model_LogisticRegression.predict_proba(data_array)[:, 1][0]

    # Apply threshold
    prediction = 1 if probability >= threshold else 0
    class_label = "Churn" if prediction == 1 else "Not Churn"


    return prediction, probability, threshold ,class_label