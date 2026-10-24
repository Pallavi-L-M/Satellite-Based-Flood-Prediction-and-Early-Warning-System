import random

class FloodPredictionModel:
    def __init__(self):
        # Simulated weights based on the paper's RF/XGBoost baseline and multi-source fusion (Gap 1)
        self.weights = {
            'rainfall': 0.4,
            'elevation': -0.3,
            's1_water_index': 0.6,
            's2_water_index': 0.3
        }

    def fetch_satellite_data(self, lat, lon):
        """
        Simulates fetching Sentinel-1, Sentinel-2, GPM/IMERG, and SRTM data.
        In a production environment, this calls Earth Engine APIs.
        """
        rainfall = random.uniform(0, 300) # mm/day from GPM/IMERG
        elevation = random.uniform(2, 400) # meters from SRTM
        s1_water = random.uniform(0.1, 0.9) # SAR backscatter thresholded water index
        
        # Simulate cloud cover to trigger the Fallback Mechanism (Gap 4)
        cloud_cover = random.uniform(0, 100)
        if cloud_cover > 75:
            # High cloud cover -> Sentinel-2 Optical is unusable
            s2_water = None 
        else:
            s2_water = random.uniform(0.1, 0.9)

        return {
            'lat': lat,
            'lon': lon,
            'rainfall_mm': round(rainfall, 2),
            'elevation_m': round(elevation, 2),
            's1_water_index': round(s1_water, 2),
            's2_water_index': round(s2_water, 2) if s2_water else None,
            'cloud_cover_pct': round(cloud_cover, 2)
        }

    def predict(self, features):
        """
        Predicts Flood Risk (Low/Medium/High) and generates a Confidence score.
        Addresses Gap 3 and Gap 5 from the PDF.
        """
        # Base risk calculation
        risk_score = (features['rainfall_mm'] * self.weights['rainfall'] + 
                      features['s1_water_index'] * self.weights['s1_water_index'] * 100)
        
        # Elevation mitigates risk (higher ground = lower risk)
        risk_score -= (features['elevation_m'] * abs(self.weights['elevation']))

        fallback_used = False
        
        # Multi-source Data Fusion (Gap 1 & Gap 4)
        if features['s2_water_index'] is not None:
            # Sentinel-1 + Sentinel-2 + Rainfall + DEM (Experiment D)
            risk_score += features['s2_water_index'] * self.weights['s2_water_index'] * 100
            model_used = "Sentinel-1 + Sentinel-2 + Rainfall + DEM (Exp D)"
            base_confidence = random.uniform(0.88, 0.97) # High confidence with multi-source
        else:
            # Sentinel-1 + Rainfall + DEM [Fallback] (Experiment C)
            fallback_used = True
            model_used = "Sentinel-1 + Rainfall + DEM [Fallback] (Exp C)"
            base_confidence = random.uniform(0.75, 0.86) # Lower confidence due to missing optical

        # Classify Risk Levels (Low, Medium, High) - Gap 3
        if risk_score > 120:
            risk_level = "High"
            confidence = base_confidence + 0.02
        elif risk_score > 60:
            risk_level = "Medium"
            confidence = base_confidence
        else:
            risk_level = "Low"
            confidence = base_confidence - 0.05

        confidence = min(max(confidence, 0.0), 1.0) # Clamp between 0 and 1

        return {
            'risk_level': risk_level,
            'confidence': round(confidence, 3),
            'risk_score': round(risk_score, 2),
            'fallback_used': fallback_used,
            'model_used': model_used
        }
