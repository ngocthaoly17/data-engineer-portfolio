from __future__ import annotations
import bentoml
import pandas as pd
import numpy as np
import traceback
from pydantic import BaseModel, Field, validator


class EnergyInput(BaseModel):
    PropertyGFATotal: float = Field(..., gt=0, description="Surface totale du bâtiment (doit être > 0)")
    NumberofFloors: int = Field(..., gt=0, description="Nombre d'étages (doit être > 0)")
    NumberofBuildings: int = Field(..., gt=0, description="Nombre de bâtiments (doit être > 0)")
    YearBuilt: int = Field(..., ge=1800, le=2025, description="Année de construction entre 1800 et 2025")
    YearsENERGYSTARCertified: int = Field(..., ge=0, description="Années de certification, doit être ≥ 0")

    @validator('YearsENERGYSTARCertified')
    def check_certified_years(cls, v, values):
        if 'YearBuilt' in values and v > (2025 - values['YearBuilt']):
            raise ValueError("Les années de certification ne peuvent pas dépasser l'âge du bâtiment")
        return v


@bentoml.service(
    resources={"cpu": "1"},
    traffic={"timeout": 10},
)
class EnergyPredictionService:
    
    def __init__(self):
        self.model = None
        self.features = [
            'PropertyGFATotal', 'NumberofFloors', 'NumberofBuildings', 
            'YearBuilt', 'YearsENERGYSTARCertified', 'BuildingAge', 
            'AvgGFA_perFloor', 'AvgGFA_perBuilding', 'IsCertified', 'DecadeBuilt'
        ]
        
        try:
            print("🔍 Recherche du modèle energy_predictor:latest...")
            available_models = bentoml.models.list()
            print(f"📦 Modèles disponibles: {[m.tag for m in available_models]}")
            
            self.model = bentoml.sklearn.load_model("energy_predictor:latest")
            print("Modèle chargé directement avec load_model()")
            
            try:
                model_info = bentoml.models.get("energy_predictor:latest")
                if hasattr(model_info, 'custom_objects') and model_info.custom_objects:
                    saved_features = model_info.custom_objects.get("features")
                    if saved_features:
                        self.features = saved_features
                        print("✅ Features récupérées depuis custom_objects")
            except Exception as e:
                print(f"⚠️ Impossible de récupérer les features: {e}")
            
        except Exception:
            traceback.print_exc()
    
    @bentoml.api
    def predict(self, parsed_json: dict) -> dict:
        try:
            print(f"📩 Données reçues: {parsed_json}")

            try:
                validated = EnergyInput(**parsed_json)
                print("✅ Données validées avec succès")
            except Exception as e:
                print(f"❌ Erreur de validation: {e}")
                return {"error": str(e), "status": "validation_error"}
            
            data = validated.dict()
            PropertyGFATotal = data["PropertyGFATotal"]
            NumberofFloors = data["NumberofFloors"]
            NumberofBuildings = data["NumberofBuildings"]
            YearBuilt = data["YearBuilt"]
            YearsENERGYSTARCertified = data["YearsENERGYSTARCertified"]

            current_year = 2025
            building_age = current_year - YearBuilt
            avg_gfa_per_floor = PropertyGFATotal / NumberofFloors
            avg_gfa_per_building = PropertyGFATotal / NumberofBuildings
            is_certified = 1.0 if YearsENERGYSTARCertified > 0 else 0.0
            decade_built = (YearBuilt // 10) * 10

            input_data_dict = {
                "PropertyGFATotal": PropertyGFATotal,
                "NumberofFloors": NumberofFloors,
                "NumberofBuildings": NumberofBuildings,
                "YearBuilt": YearBuilt,
                "YearsENERGYSTARCertified": YearsENERGYSTARCertified,
                "BuildingAge": building_age,
                "AvgGFA_perFloor": avg_gfa_per_floor,
                "AvgGFA_perBuilding": avg_gfa_per_building,
                "IsCertified": is_certified,
                "DecadeBuilt": decade_built
            }

            df_input = pd.DataFrame([input_data_dict], columns=self.features)

            if df_input.isna().any().any():
                return {"error": "Valeurs manquantes ou NaN dans les données"}

            prediction = self.model.predict(df_input)
            prediction_value = float(prediction[0])

            return {
                "predicted_energy_consumption": prediction_value,
                "features_used": len(self.features),
                "status": "success"
            }
        
        except Exception as e:
            error_msg = f"Erreur générale: {str(e)}"
            traceback.print_exc()
            return {"error": error_msg, "status": "error"}
