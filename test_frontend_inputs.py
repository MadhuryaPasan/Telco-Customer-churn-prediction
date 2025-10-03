import pytest
from helper.frontend_inputs import *
# ------------------------
# StreamingMovies Conversion
# ------------------------
@pytest.mark.parametrize("input_value,expected", [
    ("Yes", (0, 0, 1)),
    ("No", (1, 0, 0)),
    ("Unknown", (0, 1, 0)),
])
def test_streaming_movies_conv(input_value, expected):
    assert streaming_movies_conv(input_value) == expected


# ------------------------
# StreamingTV Conversion
# ------------------------
@pytest.mark.parametrize("input_value,expected", [
    ("Yes", (0, 0, 1)),
    ("No", (1, 0, 0)),
    ("Unknown", (0, 1, 0)),
])
def test_streaming_tv_conv(input_value, expected):
    assert streaming_tv_conv(input_value) == expected


# ------------------------
# Gender Conversion
# ------------------------
@pytest.mark.parametrize("input_value,expected", [
    ("Female", (1, 0)),
    ("Unknown", (0, 1)),
    ("Male", (0, 0)),
])
def test_gender_conv(input_value, expected):
    assert gender_conv(input_value) == expected


# ------------------------
# Senior Citizen Conversion
# ------------------------
@pytest.mark.parametrize("input_value,expected", [
    ("Yes", 1),
    ("No", 0),
])
def test_senior_citizen_conv(input_value, expected):
    assert senior_citizen_conv(input_value) == expected


# ------------------------
# Phone Service Conversion
# ------------------------
@pytest.mark.parametrize("input_value,expected", [
    ("Yes", 1),
    ("No", 0),
])
def test_phone_service_conv(input_value, expected):
    assert phone_service_conv(input_value) == expected


# ------------------------
# Partner Conversion
# ------------------------
@pytest.mark.parametrize("input_value,expected", [
    ("Yes", (0, 0, 1)),
    ("No", (1, 0, 0)),
    ("Unknown", (0, 1, 0)),
])
def test_partner_conv(input_value, expected):
    assert partner_conv(input_value) == expected


# ------------------------
# Internet Service Conversion
# ------------------------
@pytest.mark.parametrize("input_value,expected", [
    ("DSL", (1, 0, 0)),
    ("Fiber optic", (0, 1, 0)),
    ("No", (0, 0, 1)),
])
def test_internet_service_conv(input_value, expected):
    assert internet_service_conv(input_value) == expected


# ------------------------
# Contract Conversion
# ------------------------
@pytest.mark.parametrize("input_value,expected", [
    ("Month-to-Month", (1, 0, 0)),
    ("One year", (0, 1, 0)),
    ("Two year", (0, 0, 1)),
])
def test_contract_value_conv(input_value, expected):
    assert contract_value_conv(input_value) == expected


# ------------------------
# Dependents Conversion
# ------------------------
@pytest.mark.parametrize("input_value,expected", [
    ("Yes", (0, 0, 1)),
    ("No", (1, 0, 0)),
    ("Unknown", (0, 1, 0)),
])
def test_dependents_conv(input_value, expected):
    assert dependents_conv(input_value) == expected


# ------------------------
# Multiple Lines Conversion
# ------------------------
@pytest.mark.parametrize("input_value,expected", [
    ("Yes", (0, 0, 1)),
    ("No", (1, 0, 0)),
    ("Unknown", (0, 1, 0)),
])
def test_multiple_lines_conv(input_value, expected):
    assert multiple_lines_conv(input_value) == expected


# ------------------------
# Payment Method Conversion
# ------------------------
@pytest.mark.parametrize("input_value,expected", [
    ("Electronic check", (0, 0, 1, 0, 0)),
    ("Mailed check", (0, 0, 0, 1, 0)),
    ("Bank transfer (automatic)", (1, 0, 0, 0, 0)),
    ("Credit card (automatic)", (0, 1, 0, 0, 0)),
    ("Unknown", (0, 0, 0, 0, 1)),
])
def test_payment_method_conv(input_value, expected):
    assert payment_method_conv(input_value) == expected

