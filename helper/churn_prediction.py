import numpy as np

# --- Load Model ---
from tensorflow import keras

# Define the filename you used earlier
model_filename = "helper/telco_churn_prediction_model_V1.0.keras"

# Load the saved model
loaded_model = keras.models.load_model(model_filename)


def predict_new_customer_churn(customer_data, model, threshold=0.5):
    # 1. Convert the list/array to a NumPy array
    data_array = np.array(customer_data, dtype=np.float32)

    # 2. Reshape the array to (1, 46) to match the model's expected input shape (samples, features)
    X_new = data_array.reshape(1, -1)

    # 3. Generate the probability prediction
    probability = model.predict(X_new, verbose=0)[0][0]

    # 4. Apply the classification threshold
    prediction = 1 if probability >= threshold else 0
    class_label = "Churn" if prediction == 1 else "Not Churn"

    

    return prediction, probability, threshold ,class_label




