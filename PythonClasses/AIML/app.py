import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -------------------------------
# Load model
# -------------------------------
model = joblib.load("house_price_model.pkl")

st.set_page_config(page_title="House Price Prediction", layout="wide")
st.title("🏡 Ames House Price Prediction")
st.write("Provide house details below to estimate the selling price.")

# =========================================================
# SECTION 1 — GENERAL INFO
# =========================================================
st.header("📌 General Information")
col1, col2, col3 = st.columns(3)

with col1:
    LotArea = st.number_input("Lot Area (sq ft)", 2000, 100000, 10000)
    YearBuilt = st.number_input("Year Built", 1870, 2025, 2005)
    YearRemodAdd = st.number_input("Year Remodel", 1950, 2025, 2010)

with col2:
    OverallQual = st.slider("Overall Quality (1–10)", 1, 10, 5)
    OverallCond = st.slider("Overall Condition (1–10)", 1, 10, 5)
    LotFrontage = st.number_input("Lot Frontage (ft)", 0, 200, 60)

with col3:
    MSZoning = st.selectbox("Zoning", ["RL", "RM", "FV", "RH", "C (all)"])
    Neighborhood = st.selectbox("Neighborhood", [
        'NAmes','CollgCr','OldTown','Edwards','Somerst','Gilbert','NridgHt',
        'Sawyer','NWAmes','SawyerW','BrkSide','Mitchel','NoRidge','Crawfor',
        'Timber','IDOTRR','ClearCr','StoneBr'
    ])
    LotConfig = st.selectbox("Lot Configuration", [
        "Inside", "Corner", "CulDSac", "FR2", "FR3"
    ])

# =========================================================
# SECTION 2 — LIVING AREA
# =========================================================
st.header("🏠 Living Area")

col1, col2, col3 = st.columns(3)

with col1:
    FirstFlrSF = st.number_input("1st Floor SF", 0, 4000, 1000)
    SecondFlrSF = st.number_input("2nd Floor SF", 0, 4000, 500)

GrLivArea = FirstFlrSF + SecondFlrSF

with col2:
    TotalBsmtSF = st.number_input("Total Basement SF", 0, 4000, 800)
    BsmtFullBath = st.number_input("Basement Full Bath", 0, 3, 1)
    BsmtHalfBath = st.number_input("Basement Half Bath", 0, 2, 0)

with col3:
    FullBath = st.number_input("Full Bathrooms", 0, 5, 2)
    HalfBath = st.number_input("Half Bathrooms", 0, 5, 1)
    BedroomAbvGr = st.number_input("Bedrooms Above Ground", 0, 10, 3)

# =========================================================
# SECTION 3 — GARAGE
# =========================================================
st.header("🚗 Garage")

col1, col2, col3 = st.columns(3)

with col1:
    GarageCars = st.number_input("Garage Capacity (Cars)", 0, 5, 2)
    GarageArea = st.number_input("Garage Area (sq ft)", 0, 1500, 400)

with col2:
    GarageType = st.selectbox("Garage Type", [
        "Attchd", "Detchd", "BuiltIn", "CarPort", "Basment", "2Types", "None"
    ])

with col3:
    GarageFinish = st.selectbox("Garage Finish", ["Fin", "RFn", "Unf", "None"])
    GarageQual = st.selectbox("Garage Quality", ["Ex", "Gd", "TA", "Fa", "Po", "None"])

# =========================================================
# SECTION 4 — BASEMENT
# =========================================================
st.header("🏚 Basement")

col1, col2, col3 = st.columns(3)

with col1:
    BsmtQual = st.selectbox("Basement Quality", ["Ex","Gd","TA","Fa","Po","None"])
    BsmtCond = st.selectbox("Basement Condition", ["Ex","Gd","TA","Fa","Po","None"])

with col2:
    BsmtExposure = st.selectbox("Basement Exposure", ["Gd","Av","Mn","No","None"])
    BsmtFinType1 = st.selectbox("Basement Finish Type 1", [
        "GLQ","ALQ","BLQ","Rec","LwQ","Unf","None"
    ])

with col3:
    BsmtFinType2 = st.selectbox("Basement Finish Type 2", [
        "GLQ","ALQ","BLQ","Rec","LwQ","Unf","None"
    ])

# =========================================================
# SECTION 5 — EXTERIOR & STYLE
# =========================================================
st.header("🏘 Exterior & House Style")

col1, col2, col3 = st.columns(3)

with col1:
    HouseStyle = st.selectbox("House Style", [
        "1Story","2Story","1.5Fin","1.5Unf","SLvl","SFoyer"
    ])
    RoofStyle = st.selectbox("Roof Style", ["Gable","Hip","Flat","Shed","Gambrel","Mansard"])

with col2:
    Exterior1st = st.selectbox("Exterior 1st", [
        "VinylSd","MetalSd","Wd Sdng","HdBoard","BrkFace","Plywood","CemntBd","WdShing"
    ])
    Exterior2nd = st.selectbox("Exterior 2nd", [
        "VinylSd","MetalSd","Wd Sdng","HdBoard","BrkFace","Plywood","CemntBd","WdShing"
    ])

with col3:
    HeatingQC = st.selectbox("Heating Quality", ["Ex","Gd","TA","Fa","Po"])
    CentralAir = st.selectbox("Central Air", ["Y", "N"])

# =========================================================
# BUILD INPUT DATAFRAME
# =========================================================
input_data = {
    "LotArea": LotArea,
    "OverallQual": OverallQual,
    "OverallCond": OverallCond,
    "YearBuilt": YearBuilt,
    "YearRemodAdd": YearRemodAdd,
    "LotFrontage": LotFrontage,
    "Neighborhood": Neighborhood,
    "MSZoning": MSZoning,
    "LotConfig": LotConfig,
    "TotalBsmtSF": TotalBsmtSF,
    "BsmtFullBath": BsmtFullBath,
    "BsmtHalfBath": BsmtHalfBath,
    "FullBath": FullBath,
    "HalfBath": HalfBath,
    "BedroomAbvGr": BedroomAbvGr,
    "1stFlrSF": FirstFlrSF,
    "2ndFlrSF": SecondFlrSF,
    "GrLivArea": GrLivArea,
    "GarageCars": GarageCars,
    "GarageArea": GarageArea,
    "GarageType": GarageType,
    "GarageFinish": GarageFinish,
    "GarageQual": GarageQual,
    "BsmtQual": BsmtQual,
    "BsmtCond": BsmtCond,
    "BsmtExposure": BsmtExposure,
    "BsmtFinType1": BsmtFinType1,
    "BsmtFinType2": BsmtFinType2,
    "HouseStyle": HouseStyle,
    "RoofStyle": RoofStyle,
    "Exterior1st": Exterior1st,
    "Exterior2nd": Exterior2nd,
    "HeatingQC": HeatingQC,
    "CentralAir": CentralAir
}

input_df = pd.DataFrame([input_data])

# =========================================================
# PREDICT
# =========================================================
if st.button("📊 Predict Price"):
    log_price = model.predict(input_df)[0]
    price = np.expm1(log_price)
    st.subheader(f"🏠 Estimated House Price: **${price:,.0f}**")