import pandas as pd
import pickle


with open("helper/controllers/tenure_zscore_scaler.pkl", "rb") as f:
    tenure_scaler = pickle.load(f)
with open("helper/controllers/charges_minmax_scaler.pkl", "rb") as f:
    charges_scaler = pickle.load(f)


def tenure_z_score_calculation(value: float) -> float:

    tenure_df = pd.DataFrame({"tenure": [value]})
    final = tenure_scaler.transform(tenure_df)[0][0]
    return final


def MonthlyCharges_TotalCharges_minmaxscaler_calculation(
    MonthlyCharges_value: float, TotalCharges_value: float
) -> float:
    MonthlyCharges_TotalCharges_df = pd.DataFrame(
        {"MonthlyCharges": [68.61], "TotalCharges": [205.83]}
    )
    MonthlyCharges_final = charges_scaler.transform(MonthlyCharges_TotalCharges_df)[0][
        0
    ]
    TotalCharges_final = charges_scaler.transform(MonthlyCharges_TotalCharges_df)[0][1]
    return MonthlyCharges_final, TotalCharges_final
