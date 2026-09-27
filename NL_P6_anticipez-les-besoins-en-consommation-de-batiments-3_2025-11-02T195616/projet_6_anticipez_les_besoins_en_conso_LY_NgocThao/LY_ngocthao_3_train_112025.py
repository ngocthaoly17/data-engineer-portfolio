import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import bentoml


df = pd.read_csv("2016_Building_Energy_Benchmarking.csv")


essential_columns = [
    "PropertyGFATotal", "NumberofFloors", "NumberofBuildings", 
    "YearBuilt", "YearsENERGYSTARCertified", "TotalGHGEmissions"
]


df = df[essential_columns].dropna()

df["PropertyGFATotal"] = pd.to_numeric(df["PropertyGFATotal"], errors='coerce')
df["NumberofFloors"] = pd.to_numeric(df["NumberofFloors"], errors='coerce')
df["NumberofBuildings"] = pd.to_numeric(df["NumberofBuildings"], errors='coerce')
df["YearBuilt"] = pd.to_numeric(df["YearBuilt"], errors='coerce')
df["YearsENERGYSTARCertified"] = pd.to_numeric(df["YearsENERGYSTARCertified"], errors='coerce')
df["TotalGHGEmissions"] = pd.to_numeric(df["TotalGHGEmissions"], errors='coerce')

df = df.dropna()

df["BuildingAge"] = 2025 - df["YearBuilt"]
df["AvgGFA_perFloor"] = df["PropertyGFATotal"] / np.where(df["NumberofFloors"] > 0, df["NumberofFloors"], 1)
df["AvgGFA_perBuilding"] = df["PropertyGFATotal"] / np.where(df["NumberofBuildings"] > 0, df["NumberofBuildings"], 1)
df["IsCertified"] = (df["YearsENERGYSTARCertified"] > 0).astype(int)
df["DecadeBuilt"] = (df["YearBuilt"] // 10) * 10
df["YearsENERGYSTARCertified"] = pd.to_numeric(df["YearsENERGYSTARCertified"], errors='coerce')
df["YearsENERGYSTARCertified"] = df["YearsENERGYSTARCertified"].clip(upper=2025)

features = [
    "PropertyGFATotal", "NumberofFloors", "NumberofBuildings", 
    "YearBuilt", "YearsENERGYSTARCertified", "BuildingAge",
    "AvgGFA_perFloor", "AvgGFA_perBuilding", "IsCertified", "DecadeBuilt"
]

X = df[features]
y = df["TotalGHGEmissions"]

X = X.replace([np.inf, -np.inf], np.nan)
X = X.fillna(0)  
X = X.astype(np.float32)
X["YearsENERGYSTARCertified"] = X["YearsENERGYSTARCertified"].clip(upper=2025)


valid_indices = X.dropna().index
X = X.loc[valid_indices]
y = y.loc[valid_indices]


print(f"Vérification des données:")
print(f"Valeurs infinies dans X: {np.isinf(X.values).sum()}")
print(f"Valeurs NaN dans X: {X.isna().sum().sum()}")

q_low, q_high = y.quantile([0.01, 0.99])
outlier_mask = (y >= q_low) & (y <= q_high)
X = X[outlier_mask]
y = y[outlier_mask]

print(f"Données finales: {X.shape[0]} échantillons, {X.shape[1]} features")
print("Features utilisées:", list(X.columns))
print(f"Plage de YearBuilt: {X['YearBuilt'].min()} - {X['YearBuilt'].max()}")
print(f"Plage de YearsENERGYSTARCertified: {X['YearsENERGYSTARCertified'].min()} - {X['YearsENERGYSTARCertified'].max()}")


print("\nPlages de valeurs des features:")
for feature in features:
    print(f"{feature}: {X[feature].min():.2f} - {X[feature].max():.2f}")


rf_final = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    max_depth=10
)
rf_final.fit(X, y)


train_score = rf_final.score(X, y)
print(f"Score R² sur l'ensemble d'entraînement: {train_score:.4f}")

bentoml.sklearn.save_model(
    "energy_predictor",
    rf_final,
    custom_objects={
        "features": list(X.columns),
        "feature_count": X.shape[1],
        "feature_ranges": {col: (X[col].min(), X[col].max()) for col in X.columns}
    }
)

print("✅ Modèle sauvegardé avec succès!")
print(f"📊 Features sauvegardées: {list(X.columns)}")