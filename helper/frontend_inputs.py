from .controllers.rawdataprocessing import *

def streaming_movies_conv(value: str) -> int:
    if value == "Yes":
        StreamingMovies_No = 0
        StreamingMovies_Unknown = 0
        StreamingMovies_Yes = 1
    elif value == "No":
        StreamingMovies_No = 1
        StreamingMovies_Unknown = 0
        StreamingMovies_Yes = 0
    elif value == "Unknown":
        StreamingMovies_No = 0
        StreamingMovies_Unknown = 1
        StreamingMovies_Yes = 0
    return StreamingMovies_No, StreamingMovies_Unknown, StreamingMovies_Yes


def streaming_tv_conv(value: str) -> int:
    if value == "Yes":
        StreamingTV_No = 0
        StreamingTV_Unknown = 0
        StreamingTV_Yes = 1
    elif value == "No":
        StreamingTV_No = 1
        StreamingTV_Unknown = 0
        StreamingTV_Yes = 0
    elif value == "Unknown":
        StreamingTV_No = 0
        StreamingTV_Unknown = 1
        StreamingTV_Yes = 0
    return StreamingTV_No, StreamingTV_Unknown, StreamingTV_Yes


def tech_support_conv(value: str) -> int:
    if value == "Yes":
        TechSupport_No = 0
        TechSupport_Unknown = 0
        TechSupport_Yes = 1
    elif value == "No":
        TechSupport_No = 1
        TechSupport_Unknown = 0
        TechSupport_Yes = 0
    elif value == "Unknown":
        TechSupport_No = 0
        TechSupport_Unknown = 1
        TechSupport_Yes = 0
    return TechSupport_No, TechSupport_Unknown, TechSupport_Yes


def device_protection_conv(value: str) -> int:
    if value == "Yes":
        DeviceProtection_No = 0
        DeviceProtection_Unknown = 0
        DeviceProtection_Yes = 1
    elif value == "No":
        DeviceProtection_No = 1
        DeviceProtection_Unknown = 0
        DeviceProtection_Yes = 0
    elif value == "Unknown":
        DeviceProtection_No = 0
        DeviceProtection_Unknown = 1
        DeviceProtection_Yes = 0
    return DeviceProtection_No, DeviceProtection_Unknown, DeviceProtection_Yes


def online_backup_conv(value: str) -> int:
    if value == "Yes":
        OnlineBackup_No = 0
        OnlineBackup_Unknown = 0
        OnlineBackup_Yes = 1
    elif value == "No":
        OnlineBackup_No = 1
        OnlineBackup_Unknown = 0
        OnlineBackup_Yes = 0
    elif value == "Unknown":
        OnlineBackup_No = 0
        OnlineBackup_Unknown = 1
        OnlineBackup_Yes = 0
    return OnlineBackup_No, OnlineBackup_Unknown, OnlineBackup_Yes


def online_security_conv(value: str) -> int:
    if value == "Yes":
        OnlineSecurity_No = 0
        OnlineSecurity_Unknown = 0
        OnlineSecurity_Yes = 1
    elif value == "No":
        OnlineSecurity_No = 1
        OnlineSecurity_Unknown = 0
        OnlineSecurity_Yes = 0
    elif value == "Unknown":
        OnlineSecurity_No = 0
        OnlineSecurity_Unknown = 1
        OnlineSecurity_Yes = 0
    return OnlineSecurity_No, OnlineSecurity_Unknown, OnlineSecurity_Yes


def monthly_total_charges_conv(monthly_value: float, total_value: float) -> float:
    MonthlyCharges, TotalCharges = MonthlyCharges_TotalCharges_minmaxscaler_calculation(
        monthly_value, total_value
    )
    return MonthlyCharges, TotalCharges


def gender_conv(value: str) -> int:
    # ["Male", "Female","Unknown"]
    if value == "Female":
        gender_Female = 1
        gender_Unknown = 0
    elif value == "Unknown":
        gender_Female = 0
        gender_Unknown = 1
    elif value == "Male":
        gender_Female = 0
        gender_Unknown = 0
    return gender_Female, gender_Unknown


def senior_citizen_conv(value: str) -> int:
    if value == "Yes":
        senior_citizen = 1
    elif value == "No":
        senior_citizen = 0
    return senior_citizen


def phone_service_conv(value: str) -> int:
    if value == "Yes":
        PhoneService = 1
    elif value == "No":
        PhoneService = 0
    return PhoneService


def phone_billing_conv(value: str) -> int:
    if value == "Yes":
        PaperlessBilling = 1
    elif value == "No":
        PaperlessBilling = 0
    return PaperlessBilling


def partner_conv(value: str) -> int:
    if value == "Yes":
        Partner_No = 0
        Partner_Unknown = 0
        Partner_Yes = 1
    elif value == "No":
        Partner_No = 1
        Partner_Unknown = 0
        Partner_Yes = 0
    elif value == "Unknown":
        Partner_No = 0
        Partner_Unknown = 1
        Partner_Yes = 0
    return Partner_No, Partner_Unknown, Partner_Yes


def payment_method_conv(value: str) -> int:
    if value == "Electronic check":
        PaymentMethod_Bank_transfer_automatic = 0
        PaymentMethod_CreditP_card_automatic = 0
        PaymentMethod_Electronic_check = 1
        PaymentMethod_Mailed_check = 0
        PaymentMethod_Unknown = 0
    elif value == "Mailed check":
        PaymentMethod_Bank_transfer_automatic = 0
        PaymentMethod_CreditP_card_automatic = 0
        PaymentMethod_Electronic_check = 0
        PaymentMethod_Mailed_check = 1
        PaymentMethod_Unknown = 0
    elif value == "Bank transfer (automatic)":
        PaymentMethod_Bank_transfer_automatic = 1
        PaymentMethod_CreditP_card_automatic = 0
        PaymentMethod_Electronic_check = 0
        PaymentMethod_Mailed_check = 0
        PaymentMethod_Unknown = 0
    elif value == "Credit card (automatic)":
        PaymentMethod_Bank_transfer_automatic = 0
        PaymentMethod_CreditP_card_automatic = 1
        PaymentMethod_Electronic_check = 0
        PaymentMethod_Mailed_check = 0
        PaymentMethod_Unknown = 0
    elif value == "Unknown":
        PaymentMethod_Bank_transfer_automatic = 0
        PaymentMethod_CreditP_card_automatic = 0
        PaymentMethod_Electronic_check = 0
        PaymentMethod_Mailed_check = 0
        PaymentMethod_Unknown = 1
    return (
        PaymentMethod_Bank_transfer_automatic,
        PaymentMethod_CreditP_card_automatic,
        PaymentMethod_Electronic_check,
        PaymentMethod_Mailed_check,
        PaymentMethod_Unknown,
    )


def internet_service_conv(value: str) -> int:
    if value == "DSL":
        InternetService_DSL = 1
        InternetService_Fiber_optic = 0
        InternetService_No = 0
    elif value == "Fiber optic":
        InternetService_DSL = 0
        InternetService_Fiber_optic = 1
        InternetService_No = 0
    elif value == "No":
        InternetService_DSL = 0
        InternetService_Fiber_optic = 0
        InternetService_No = 1
    return InternetService_DSL, InternetService_Fiber_optic, InternetService_No


def contract_value_conv(value: str) -> int:
    if value == "Month-to-Month":
        Contract_Month_to_Month = 1
        Contract_One_year = 0
        Contract_Two_year = 0
    elif value == "One year":
        Contract_Month_to_Month = 0
        Contract_One_year = 1
        Contract_Two_year = 0
    elif value == "Two year":
        Contract_Month_to_Month = 0
        Contract_One_year = 0
        Contract_Two_year = 1
    return Contract_Month_to_Month, Contract_One_year, Contract_Two_year


def dependents_conv(value: str) -> int:
    if value == "Yes":
        Dependents_No = 0
        Dependents_Unknown = 0
        Dependents_Yes = 1
    elif value == "No":
        Dependents_No = 1
        Dependents_Unknown = 0
        Dependents_Yes = 0
    elif value == "Unknown":
        Dependents_No = 0
        Dependents_Unknown = 1
        Dependents_Yes = 0
    return Dependents_No, Dependents_Unknown, Dependents_Yes


def multiple_lines_conv(value: str) -> int:
    if value == "Yes":
        MultipleLines_No = 0
        MultipleLines_Unknown = 0
        MultipleLines_Yes = 1
    elif value == "No":
        MultipleLines_No = 1
        MultipleLines_Unknown = 0
        MultipleLines_Yes = 0
    elif value == "Unknown":
        MultipleLines_No = 0
        MultipleLines_Unknown = 1
        MultipleLines_Yes = 0
    return MultipleLines_No, MultipleLines_Unknown, MultipleLines_Yes


def tenure_conv(value: int) -> float:
    tenure = tenure_z_score_calculation(value)
    return tenure
