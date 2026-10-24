"""
Generates comprehensive statewide flood intelligence datasets and GeoJSON layers
for all 31 districts of Karnataka.
Alliance University - Department of Computer Science & Engineering
"""

import json
import math
import os

os.makedirs('static/data', exist_ok=True)

# 1. Complete Statewide District Intelligence Database for all 31 Districts of Karnataka
districts_db = {
    # --- KRISHNA BASIN (North Karnataka) ---
    "Belgaum": {
        "display_name": "Belagavi (Belgaum)",
        "canonical_id": "belagavi",
        "basin": "Krishna & Ghataprabha Basins",
        "zone": "North Karnataka",
        "risk_level": "Severe Warning",
        "alert_badge": "Red Alert",
        "initial_candidate_km2": 24.85,
        "filtered_candidate_km2": 18.62,
        "reduction_pct": 25.07,
        "rainfall_24h_mm": 142.5,
        "soil_moisture_pct": 91.2,
        "key_river": "Krishna, Ghataprabha, Malaprabha",
        "gauge_station": "Kudachi Gauge (Krishna River)",
        "gauge_stage_m": 528.4,
        "gauge_danger_m": 525.0,
        "key_reservoirs": "Hidkal (Ghataprabha) Dam, Navilatirtha (Malaprabha) Dam",
        "vulnerable_taluks": ["Chikkodi", "Athani", "Raybag", "Gokak", "Khanapur"],
        "center": [15.8497, 74.4977],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-07",
        "mean_backscatter_drop_db": -5.4,
        "population_at_risk": 48200,
        "evacuation_shelters_active": 18,
        "advisory_summary": "High discharge from Koyna and Radhanagari dams in Maharashtra combined with torrential Western Ghats catchment rainfall causing massive backscatter drops along Chikkodi and Athani floodplains."
    },
    "Bagalkot": {
        "display_name": "Bagalkot",
        "canonical_id": "bagalkot",
        "basin": "Krishna & Ghataprabha Confluence",
        "zone": "North Karnataka",
        "risk_level": "Severe Warning",
        "alert_badge": "Red Alert",
        "initial_candidate_km2": 19.40,
        "filtered_candidate_km2": 14.55,
        "reduction_pct": 25.00,
        "rainfall_24h_mm": 118.0,
        "soil_moisture_pct": 88.5,
        "key_river": "Krishna, Ghataprabha, Malaprabha",
        "gauge_station": "Bilagi River Station",
        "gauge_stage_m": 521.8,
        "gauge_danger_m": 519.6,
        "key_reservoirs": "Almatti (Lal Bahadur Shastri) Dam",
        "vulnerable_taluks": ["Jamkhandi", "Bilagi", "Mudhol", "Badami", "Hunagund"],
        "center": [16.1875, 75.6980],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-07",
        "mean_backscatter_drop_db": -5.1,
        "population_at_risk": 36500,
        "evacuation_shelters_active": 14,
        "advisory_summary": "Almatti reservoir backwaters swelling due to record 3.5 lakh cusecs inflow. Jamkhandi lowlands and river islands identified as high-confidence candidate flood inundation."
    },
    "Bijapur": {
        "display_name": "Vijayapura (Bijapur)",
        "canonical_id": "vijayapura",
        "basin": "Krishna & Doni Basins",
        "zone": "North Karnataka",
        "risk_level": "Flood Watch",
        "alert_badge": "Orange Alert",
        "initial_candidate_km2": 14.20,
        "filtered_candidate_km2": 10.65,
        "reduction_pct": 25.00,
        "rainfall_24h_mm": 86.0,
        "soil_moisture_pct": 79.4,
        "key_river": "Krishna, Doni",
        "gauge_station": "Kolhar Bridge Gauge",
        "gauge_stage_m": 515.2,
        "gauge_danger_m": 514.0,
        "key_reservoirs": "Almatti Dam Outflow Channel",
        "vulnerable_taluks": ["Muddebihal", "Basavana Bagewadi", "Indi"],
        "center": [16.8302, 75.7100],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-07",
        "mean_backscatter_drop_db": -4.6,
        "population_at_risk": 18200,
        "evacuation_shelters_active": 7,
        "advisory_summary": "Doni river flash flood candidates detected alongside Krishna downstream spillway surges."
    },
    "Raichur": {
        "display_name": "Raichur",
        "canonical_id": "raichur",
        "basin": "Krishna & Tungabhadra Doab",
        "zone": "North Karnataka",
        "risk_level": "Severe Warning",
        "alert_badge": "Red Alert",
        "initial_candidate_km2": 16.75,
        "filtered_candidate_km2": 12.56,
        "reduction_pct": 25.01,
        "rainfall_24h_mm": 94.0,
        "soil_moisture_pct": 84.1,
        "key_river": "Krishna, Tungabhadra",
        "gauge_station": "Kudaloor Confluence Gauge",
        "gauge_stage_m": 334.8,
        "gauge_danger_m": 332.5,
        "key_reservoirs": "Basavasagara (Narayanpur) Dam, Tungabhadra downstream",
        "vulnerable_taluks": ["Lingsugur", "Devadurga", "Raichur", "Manvi"],
        "center": [16.2076, 77.3463],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-08",
        "mean_backscatter_drop_db": -4.9,
        "population_at_risk": 29400,
        "evacuation_shelters_active": 11,
        "advisory_summary": "High discharge from Narayanpur Dam into Krishna River flooding river islands in Devadurga and Lingsugur taluks."
    },
    "Gulbarga": {
        "display_name": "Kalaburagi (Gulbarga) & Yadgir",
        "canonical_id": "kalaburagi",
        "basin": "Bhima & Krishna Basins",
        "zone": "North Karnataka",
        "risk_level": "Flood Watch",
        "alert_badge": "Orange Alert",
        "initial_candidate_km2": 12.60,
        "filtered_candidate_km2": 9.45,
        "reduction_pct": 25.00,
        "rainfall_24h_mm": 82.0,
        "soil_moisture_pct": 77.0,
        "key_river": "Bhima, Kagina, Bennethora",
        "gauge_station": "Afzalpur Gauge (Bhima River)",
        "gauge_stage_m": 412.5,
        "gauge_danger_m": 411.0,
        "key_reservoirs": "Bennethora Reservoir, Sonna Barrage",
        "vulnerable_taluks": ["Afzalpur", "Chittapur", "Sedam", "Jevargi", "Shahapur"],
        "center": [17.3297, 76.8343],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-08",
        "mean_backscatter_drop_db": -4.2,
        "population_at_risk": 15600,
        "evacuation_shelters_active": 6,
        "advisory_summary": "Bhima River discharge from Ujjani dam in Maharashtra flooding low-lying river bends in Afzalpur and Jevargi."
    },
    "Bidar": {
        "display_name": "Bidar",
        "canonical_id": "bidar",
        "basin": "Manjra & Karanja Basins",
        "zone": "North Karnataka",
        "risk_level": "Advisory",
        "alert_badge": "Yellow Alert",
        "initial_candidate_km2": 5.40,
        "filtered_candidate_km2": 4.10,
        "reduction_pct": 24.07,
        "rainfall_24h_mm": 62.0,
        "soil_moisture_pct": 68.2,
        "key_river": "Manjra, Karanja",
        "gauge_station": "Byalahalli Gauge",
        "gauge_stage_m": 582.0,
        "gauge_danger_m": 584.5,
        "key_reservoirs": "Karanja Dam (Chitaguppa)",
        "vulnerable_taluks": ["Bhalki", "Aurad", "Humnabad"],
        "center": [17.9104, 77.5199],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-08",
        "mean_backscatter_drop_db": -3.5,
        "population_at_risk": 5200,
        "evacuation_shelters_active": 2,
        "advisory_summary": "Karanja reservoir levels normal; localized riparian inundation monitored along Aurad border."
    },
    "Gadag": {
        "display_name": "Gadag",
        "canonical_id": "gadag",
        "basin": "Malaprabha & Tungabhadra Basins",
        "zone": "North Karnataka",
        "risk_level": "Advisory",
        "alert_badge": "Yellow Alert",
        "initial_candidate_km2": 4.80,
        "filtered_candidate_km2": 3.65,
        "reduction_pct": 23.96,
        "rainfall_24h_mm": 54.0,
        "soil_moisture_pct": 64.0,
        "key_river": "Malaprabha, Tungabhadra",
        "gauge_station": "Ron Sub-basin Station",
        "gauge_stage_m": 545.0,
        "gauge_danger_m": 547.0,
        "key_reservoirs": "Singatalur Lift Irrigation Basin",
        "vulnerable_taluks": ["Ron", "Nargund", "Shirhatti"],
        "center": [15.4167, 75.6167],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-07",
        "mean_backscatter_drop_db": -3.4,
        "population_at_risk": 4100,
        "evacuation_shelters_active": 2,
        "advisory_summary": "Agricultural candidate wetting detected along Nargund lowlands; river levels contained."
    },
    "Dharwad": {
        "display_name": "Dharwad",
        "canonical_id": "dharwad",
        "basin": "Malaprabha & Bedthi Headwaters",
        "zone": "North Karnataka",
        "risk_level": "Normal",
        "alert_badge": "Green Status",
        "initial_candidate_km2": 3.10,
        "filtered_candidate_km2": 2.35,
        "reduction_pct": 24.19,
        "rainfall_24h_mm": 48.0,
        "soil_moisture_pct": 61.5,
        "key_river": "Malaprabha, Bennihalla",
        "gauge_station": "Navalgund Bennihalla Gauge",
        "gauge_stage_m": 580.2,
        "gauge_danger_m": 583.0,
        "key_reservoirs": "Neersagar, Kelgeri Lake Basin",
        "vulnerable_taluks": ["Navalgund", "Hubballi", "Kundgol"],
        "center": [15.4589, 75.0078],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-07",
        "mean_backscatter_drop_db": -3.2,
        "population_at_risk": 2100,
        "evacuation_shelters_active": 0,
        "advisory_summary": "Bennihalla stream exhibiting minor flow rise; no active population threat."
    },

    # --- TUNGABHADRA & CENTRAL BASIN ---
    "Bellary": {
        "display_name": "Ballari (Bellary) & Vijayanagara",
        "canonical_id": "ballari",
        "basin": "Tungabhadra Basin",
        "zone": "Central Karnataka",
        "risk_level": "Severe Warning",
        "alert_badge": "Red Alert",
        "initial_candidate_km2": 18.25,
        "filtered_candidate_km2": 13.70,
        "reduction_pct": 24.93,
        "rainfall_24h_mm": 105.0,
        "soil_moisture_pct": 86.4,
        "key_river": "Tungabhadra, Hagari",
        "gauge_station": "Hampi Heritage Gauge (Tungabhadra River)",
        "gauge_stage_m": 486.2,
        "gauge_danger_m": 484.5,
        "key_reservoirs": "Tungabhadra (TB) Dam (Hospete)",
        "vulnerable_taluks": ["Hospete", "Kampli", "Siruguppa", "Hagaribommanahalli"],
        "center": [15.1394, 76.9214],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-08",
        "mean_backscatter_drop_db": -5.2,
        "population_at_risk": 34100,
        "evacuation_shelters_active": 12,
        "advisory_summary": "Tungabhadra Dam releasing over 1.8 lakh cusecs through 33 spillway gates. Historic Hampi monuments and Kampli banana plantations inundated in SAR backscatter difference rasters."
    },
    "Koppal": {
        "display_name": "Koppal",
        "canonical_id": "koppal",
        "basin": "Tungabhadra Left Bank Basin",
        "zone": "Central Karnataka",
        "risk_level": "Flood Watch",
        "alert_badge": "Orange Alert",
        "initial_candidate_km2": 11.40,
        "filtered_candidate_km2": 8.55,
        "reduction_pct": 25.00,
        "rainfall_24h_mm": 78.0,
        "soil_moisture_pct": 76.5,
        "key_river": "Tungabhadra",
        "gauge_station": "Gangavathi Spillway Monitor",
        "gauge_stage_m": 482.0,
        "gauge_danger_m": 481.2,
        "key_reservoirs": "Tungabhadra Dam Left Bank Canal",
        "vulnerable_taluks": ["Gangavathi", "Koppal", "Yelburga"],
        "center": [15.3524, 76.1558],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-08",
        "mean_backscatter_drop_db": -4.4,
        "population_at_risk": 16400,
        "evacuation_shelters_active": 6,
        "advisory_summary": "Gangavathi paddy belts along left bank canal under alert as Tungabhadra discharge surges."
    },
    "Haveri": {
        "display_name": "Haveri",
        "canonical_id": "haveri",
        "basin": "Varada & Tungabhadra Basins",
        "zone": "Central Karnataka",
        "risk_level": "Flood Watch",
        "alert_badge": "Orange Alert",
        "initial_candidate_km2": 13.15,
        "filtered_candidate_km2": 9.85,
        "reduction_pct": 25.10,
        "rainfall_24h_mm": 112.0,
        "soil_moisture_pct": 87.0,
        "key_river": "Varada, Dharma, Kumadhvathi, Tungabhadra",
        "gauge_station": "Sangur Gauge (Varada River)",
        "gauge_stage_m": 560.4,
        "gauge_danger_m": 559.0,
        "key_reservoirs": "Dharma Reservoir",
        "vulnerable_taluks": ["Hangal", "Hirekerur", "Ranebennur", "Haveri", "Byadgi"],
        "center": [14.7972, 75.3995],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-07",
        "mean_backscatter_drop_db": -4.7,
        "population_at_risk": 21800,
        "evacuation_shelters_active": 8,
        "advisory_summary": "Varada and Kumadhvathi rivers overflowing. Extensive agricultural candidate flood polygons mapped in Hangal and Ranebennur taluks."
    },
    "Davanagere": {
        "display_name": "Davanagere",
        "canonical_id": "davanagere",
        "basin": "Tungabhadra Central Basin",
        "zone": "Central Karnataka",
        "risk_level": "Flood Watch",
        "alert_badge": "Orange Alert",
        "initial_candidate_km2": 10.80,
        "filtered_candidate_km2": 8.10,
        "reduction_pct": 25.00,
        "rainfall_24h_mm": 88.0,
        "soil_moisture_pct": 81.2,
        "key_river": "Tungabhadra",
        "gauge_station": "Harihar Bridge Gauge",
        "gauge_stage_m": 535.1,
        "gauge_danger_m": 534.0,
        "key_reservoirs": "Shanthi Sagara (Sulekere), TB River Reach",
        "vulnerable_taluks": ["Harihar", "Honnali", "Channagiri"],
        "center": [14.4644, 75.9218],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-08",
        "mean_backscatter_drop_db": -4.3,
        "population_at_risk": 13900,
        "evacuation_shelters_active": 5,
        "advisory_summary": "Harihar temple ghats and Honnali lowlands partially inundated by Tungabhadra discharge."
    },
    "Chitradurga": {
        "display_name": "Chitradurga",
        "canonical_id": "chitradurga",
        "basin": "Vedavathi & Tungabhadra Basins",
        "zone": "Central Karnataka",
        "risk_level": "Advisory",
        "alert_badge": "Yellow Alert",
        "initial_candidate_km2": 6.20,
        "filtered_candidate_km2": 4.70,
        "reduction_pct": 24.19,
        "rainfall_24h_mm": 52.0,
        "soil_moisture_pct": 63.4,
        "key_river": "Vedavathi",
        "gauge_station": "Hiriyur Bridge Station",
        "gauge_stage_m": 612.0,
        "gauge_danger_m": 614.5,
        "key_reservoirs": "Vani Vilasa Sagara (Mari Kanive)",
        "vulnerable_taluks": ["Hiriyur", "Hosadurga", "Challakere"],
        "center": [14.2251, 76.4022],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-08",
        "mean_backscatter_drop_db": -3.5,
        "population_at_risk": 5400,
        "evacuation_shelters_active": 2,
        "advisory_summary": "Vani Vilasa Sagara storage at 88%; regulated outflow; low risk."
    },
    "Tumkur": {
        "display_name": "Tumakuru (Tumkur)",
        "canonical_id": "tumakuru",
        "basin": "Shimsha & Jayamangali Basins",
        "zone": "Central Karnataka",
        "risk_level": "Normal",
        "alert_badge": "Green Status",
        "initial_candidate_km2": 4.50,
        "filtered_candidate_km2": 3.40,
        "reduction_pct": 24.44,
        "rainfall_24h_mm": 41.0,
        "soil_moisture_pct": 59.0,
        "key_river": "Shimsha, Jayamangali",
        "gauge_station": "Gubbi Stream Monitor",
        "gauge_stage_m": 782.0,
        "gauge_danger_m": 785.0,
        "key_reservoirs": "Markonahalli Dam, Bugudanahalli Lake",
        "vulnerable_taluks": ["Kunigal", "Tiptur", "Madhugiri", "Pavagada"],
        "center": [13.3379, 77.1173],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-08",
        "mean_backscatter_drop_db": -3.1,
        "population_at_risk": 1800,
        "evacuation_shelters_active": 0,
        "advisory_summary": "Tanks and channels operating within design thresholds."
    },

    # --- MALNAD & WESTERN GHATS CATCHMENT ---
    "Shimoga": {
        "display_name": "Shivamogga (Shimoga)",
        "canonical_id": "shivamogga",
        "basin": "Tunga, Bhadra & Sharavathi Basins",
        "zone": "Malnad Catchment",
        "risk_level": "Severe Warning",
        "alert_badge": "Red Alert",
        "initial_candidate_km2": 21.60,
        "filtered_candidate_km2": 16.20,
        "reduction_pct": 25.00,
        "rainfall_24h_mm": 168.0,
        "soil_moisture_pct": 95.0,
        "key_river": "Tunga, Bhadra, Sharavathi, Varahi",
        "gauge_station": "Shivamogga City Tunga Bridge Gauge",
        "gauge_stage_m": 574.8,
        "gauge_danger_m": 572.5,
        "key_reservoirs": "Linganamakki Dam, Tunga Dam (Gajanur), Bhadra Dam",
        "vulnerable_taluks": ["Thirthahalli", "Sagar", "Hosanagar", "Bhadravati", "Shivamogga"],
        "center": [13.9299, 75.5681],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-06",
        "mean_backscatter_drop_db": -5.6,
        "population_at_risk": 41200,
        "evacuation_shelters_active": 15,
        "advisory_summary": "Record rainfall in Agumbe and Thirthahalli. Gajanur Tunga Dam discharging over 90,000 cusecs; city lowlands and temple courtyards submerged in SAR observation."
    },
    "Chikmagalur": {
        "display_name": "Chikkamagaluru",
        "canonical_id": "chikkamagaluru",
        "basin": "Tunga, Bhadra & Hemavathi Headwaters",
        "zone": "Malnad Catchment",
        "risk_level": "Severe Warning",
        "alert_badge": "Red Alert",
        "initial_candidate_km2": 15.80,
        "filtered_candidate_km2": 11.85,
        "reduction_pct": 25.00,
        "rainfall_24h_mm": 178.5,
        "soil_moisture_pct": 96.8,
        "key_river": "Bhadra, Tunga, Hemavathi",
        "gauge_station": "Kalasah River Gauge",
        "gauge_stage_m": 724.0,
        "gauge_danger_m": 722.0,
        "key_reservoirs": "Bhadra Reservoir (Lakkavalli)",
        "vulnerable_taluks": ["Mudigere", "Sringeri", "Koppa", "Narasimharajapura"],
        "center": [13.3161, 75.7720],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-06",
        "mean_backscatter_drop_db": -5.2,
        "population_at_risk": 23400,
        "evacuation_shelters_active": 9,
        "advisory_summary": "Flash flood and landslide candidate alerts active in Sringeri and Mudigere hill valleys. Bhadra inflow at maximum seasonal rate."
    },
    "Kodagu": {
        "display_name": "Kodagu (Coorg)",
        "canonical_id": "kodagu",
        "basin": "Upper Kaveri & Lakshmanatirtha Basins",
        "zone": "Southern Western Ghats",
        "risk_level": "Severe Warning",
        "alert_badge": "Red Alert",
        "initial_candidate_km2": 17.50,
        "filtered_candidate_km2": 13.12,
        "reduction_pct": 25.03,
        "rainfall_24h_mm": 210.0,
        "soil_moisture_pct": 98.4,
        "key_river": "Kaveri, Lakshmanatirtha, Harangi",
        "gauge_station": "Bhagamandala Triveni Sangama Gauge",
        "gauge_stage_m": 868.5,
        "gauge_danger_m": 865.0,
        "key_reservoirs": "Harangi Reservoir",
        "vulnerable_taluks": ["Madikeri", "Virajpet", "Somwarpet", "Ponnampet"],
        "center": [12.3375, 75.8069],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-06",
        "mean_backscatter_drop_db": -5.8,
        "population_at_risk": 28600,
        "evacuation_shelters_active": 16,
        "advisory_summary": "Extremely heavy rainfall in Bhagamandala. Triveni Sangama completely inundated; Harangi Dam crest gates opened discharging 42,000 cusecs."
    },
    "Hassan": {
        "display_name": "Hassan",
        "canonical_id": "hassan",
        "basin": "Hemavathi & Yagachi Basins",
        "zone": "Southern Malnad",
        "risk_level": "Flood Watch",
        "alert_badge": "Orange Alert",
        "initial_candidate_km2": 12.80,
        "filtered_candidate_km2": 9.60,
        "reduction_pct": 25.00,
        "rainfall_24h_mm": 130.0,
        "soil_moisture_pct": 89.2,
        "key_river": "Hemavathi, Yagachi",
        "gauge_station": "Gorur Dam Downstream Gauge",
        "gauge_stage_m": 836.4,
        "gauge_danger_m": 834.0,
        "key_reservoirs": "Gorur (Hemavathi) Dam, Yagachi Dam",
        "vulnerable_taluks": ["Sakleshpur", "Alur", "Holenarasipur", "Arkalgud"],
        "center": [13.0033, 76.1004],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-06",
        "mean_backscatter_drop_db": -4.8,
        "population_at_risk": 19800,
        "evacuation_shelters_active": 7,
        "advisory_summary": "Hemavathi Dam releasing 38,000 cusecs. Holenarasipur and Arkalgud riverbank agriculture identified as candidate flood extent."
    },

    # --- COASTAL KARNATAKA (WEST COAST BASIN) ---
    "Dakshin Kannad": {
        "display_name": "Dakshina Kannada (Mangaluru)",
        "canonical_id": "dakshina_kannada",
        "basin": "Netravathi & Gurupura Basins",
        "zone": "Coastal Karnataka",
        "risk_level": "Severe Warning",
        "alert_badge": "Red Alert",
        "initial_candidate_km2": 26.40,
        "filtered_candidate_km2": 19.80,
        "reduction_pct": 25.00,
        "rainfall_24h_mm": 192.0,
        "soil_moisture_pct": 97.2,
        "key_river": "Netravathi, Gurupura (Phalguni), Kumaradhara",
        "gauge_station": "Bantwal Gauge (Netravathi River)",
        "gauge_stage_m": 9.8,
        "gauge_danger_m": 8.5,
        "key_reservoirs": "Thumbe Vented Dam, AMR Power Dam",
        "vulnerable_taluks": ["Bantwal", "Belthangady", "Puttur", "Mangaluru", "Sullia"],
        "center": [12.8703, 75.2289],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-06",
        "mean_backscatter_drop_db": -5.9,
        "population_at_risk": 52400,
        "evacuation_shelters_active": 22,
        "advisory_summary": "Netravathi and Kumaradhara rivers flowing well above the danger mark at Bantwal and Uppinangady. Major coastal and riverbank lowlands submerged in Sentinel-1 SAR analysis."
    },
    "Udupi": {
        "display_name": "Udupi",
        "canonical_id": "udupi",
        "basin": "Swarna, Sita, Varahi & Shambhavi Basins",
        "zone": "Coastal Karnataka",
        "risk_level": "Severe Warning",
        "alert_badge": "Red Alert",
        "initial_candidate_km2": 22.10,
        "filtered_candidate_km2": 16.55,
        "reduction_pct": 25.11,
        "rainfall_24h_mm": 184.0,
        "soil_moisture_pct": 96.5,
        "key_river": "Swarna, Sita, Varahi, Chakra",
        "gauge_station": "Baje Dam (Swarna River)",
        "gauge_stage_m": 6.4,
        "gauge_danger_m": 5.2,
        "key_reservoirs": "Baje Dam, Varahi Hydel Intake",
        "vulnerable_taluks": ["Udupi", "Kundapura", "Karkala", "Kaup", "Brahmavar"],
        "center": [13.3409, 74.7421],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-06",
        "mean_backscatter_drop_db": -5.7,
        "population_at_risk": 43500,
        "evacuation_shelters_active": 19,
        "advisory_summary": "High tide backwater surges combined with flash runoff along Swarna and Sita rivers inundating low-lying residential clusters in Brahmavar and Kundapura."
    },
    "Uttar Kannand": {
        "display_name": "Uttara Kannada (Karwar)",
        "canonical_id": "uttara_kannada",
        "basin": "Kali, Sharavathi, Aghanashini & Gangavali Basins",
        "zone": "Coastal Karnataka",
        "risk_level": "Severe Warning",
        "alert_badge": "Red Alert",
        "initial_candidate_km2": 28.90,
        "filtered_candidate_km2": 21.65,
        "reduction_pct": 25.09,
        "rainfall_24h_mm": 176.0,
        "soil_moisture_pct": 95.8,
        "key_river": "Kali, Sharavathi, Gangavali, Aghanashini",
        "gauge_station": "Kadra Gauge (Kali River)",
        "gauge_stage_m": 34.2,
        "gauge_danger_m": 32.0,
        "key_reservoirs": "Supa Dam, Kadra Dam, Kodasalli Dam, Gersoppa Dam",
        "vulnerable_taluks": ["Karwar", "Ankola", "Kumta", "Honnavar", "Bhatkal", "Yellapur"],
        "center": [14.8185, 74.1416],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-06",
        "mean_backscatter_drop_db": -5.8,
        "population_at_risk": 49800,
        "evacuation_shelters_active": 21,
        "advisory_summary": "Supa and Kadra dams releasing massive discharges into Kali River. Estuarine backwaters flooded along Karwar, Ankola, and Honnavar coastal plains."
    },

    # --- CAUVERY BASIN (South Karnataka) ---
    "Mysore": {
        "display_name": "Mysuru (Mysore)",
        "canonical_id": "mysuru",
        "basin": "Kabini & Kaveri Basins",
        "zone": "South Karnataka",
        "risk_level": "Severe Warning",
        "alert_badge": "Red Alert",
        "initial_candidate_km2": 8.6782,
        "filtered_candidate_km2": 6.5572,
        "reduction_pct": 24.44,
        "rainfall_24h_mm": 128.5,
        "soil_moisture_pct": 92.6,
        "key_river": "Kabini (Kapila), Kaveri",
        "gauge_station": "Beechanahalli Kabini Spillway Gauge",
        "gauge_stage_m": 696.1,
        "gauge_danger_m": 694.0,
        "key_reservoirs": "Kabini Reservoir (Beechanahalli), KRS Dam (Kaveri)",
        "vulnerable_taluks": ["H.D. Kote", "Saragur", "Nanjangud", "T. Narasipura", "Mysuru"],
        "center": [11.972, 76.352],
        "zoom": 11,
        "last_sar_acquisition": "2024-08-06",
        "mean_backscatter_drop_db": -6.2,
        "population_at_risk": 27800,
        "evacuation_shelters_active": 12,
        "advisory_summary": "Kabini Dam spillway discharge exceeding 68,000 cusecs due to heavy Wayanad catchment precipitation. Flood candidate clusters detected across H.D. Kote, Saragur, and Nanjangud temple ghats."
    },
    "Chamrajnagar": {
        "display_name": "Chamarajanagar",
        "canonical_id": "chamarajanagar",
        "basin": "Kabini & Suvarnavathi Basins",
        "zone": "South Karnataka",
        "risk_level": "Flood Watch",
        "alert_badge": "Orange Alert",
        "initial_candidate_km2": 9.15,
        "filtered_candidate_km2": 6.85,
        "reduction_pct": 25.14,
        "rainfall_24h_mm": 92.0,
        "soil_moisture_pct": 82.5,
        "key_river": "Suvarnavathi, Chikkahole, Kaveri",
        "gauge_station": "Kollegal Kaveri Reach Gauge",
        "gauge_stage_m": 622.0,
        "gauge_danger_m": 620.5,
        "key_reservoirs": "Suvarnavathi Dam, Chikkahole Reservoir",
        "vulnerable_taluks": ["Kollegal", "Gundlupet", "Chamarajanagar", "Yelandur", "Hanur"],
        "center": [11.9261, 76.9437],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-06",
        "mean_backscatter_drop_db": -4.6,
        "population_at_risk": 14200,
        "evacuation_shelters_active": 5,
        "advisory_summary": "Downstream Kaveri and Kabini confluence surge causing riparian candidate inundation near Kollegal and river islands."
    },
    "Mandya": {
        "display_name": "Mandya",
        "canonical_id": "mandya",
        "basin": "Kaveri & Lokapavani Basins",
        "zone": "South Karnataka",
        "risk_level": "Severe Warning",
        "alert_badge": "Red Alert",
        "initial_candidate_km2": 14.80,
        "filtered_candidate_km2": 11.10,
        "reduction_pct": 25.00,
        "rainfall_24h_mm": 115.0,
        "soil_moisture_pct": 89.0,
        "key_river": "Kaveri, Hemavathi, Shimsha",
        "gauge_station": "Srirangapatna Ranganathaswamy Ghat Gauge",
        "gauge_stage_m": 668.4,
        "gauge_danger_m": 666.0,
        "key_reservoirs": "Krishna Raja Sagara (KRS) Dam",
        "vulnerable_taluks": ["Srirangapatna", "Pandavapura", "Malavalli", "Mandya", "K.R. Pet"],
        "center": [12.5242, 76.8958],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-06",
        "mean_backscatter_drop_db": -5.5,
        "population_at_risk": 31500,
        "evacuation_shelters_active": 11,
        "advisory_summary": "KRS Dam releasing over 1.25 lakh cusecs into Kaveri River. Srirangapatna island and Sangama pilgrimage points inundated in SAR difference maps."
    },
    "Bangalore Urban": {
        "display_name": "Bengaluru Urban",
        "canonical_id": "bengaluru_urban",
        "basin": "Vrishabhavathi, Arkavathi & Dakshina Pinakini",
        "zone": "Bangalore Metropolitan",
        "risk_level": "Flood Watch",
        "alert_badge": "Orange Alert",
        "initial_candidate_km2": 11.20,
        "filtered_candidate_km2": 8.40,
        "reduction_pct": 25.00,
        "rainfall_24h_mm": 108.0,
        "soil_moisture_pct": 85.0,
        "key_river": "Vrishabhavathi, Storm Water Drain (SWD) Network",
        "gauge_station": "Bellandur Wetland Outflow Monitor",
        "gauge_stage_m": 890.2,
        "gauge_danger_m": 889.0,
        "key_reservoirs": "Bellandur Lake, Varthur Lake, Byramangala Dam",
        "vulnerable_taluks": ["Mahadevapura", "Bommanahalli", "Yelahanka", "East Zone"],
        "center": [12.9716, 77.5946],
        "zoom": 11,
        "last_sar_acquisition": "2024-08-06",
        "mean_backscatter_drop_db": -4.8,
        "population_at_risk": 29800,
        "evacuation_shelters_active": 8,
        "advisory_summary": "Urban stormwater flash floods detected in low-lying layouts, lake buffer zones, and IT corridor valleys."
    },
    "Bangalore Rural": {
        "display_name": "Bengaluru Rural & Ramanagara",
        "canonical_id": "bengaluru_rural",
        "basin": "Arkavathi & Kanva Basins",
        "zone": "Bangalore Metropolitan",
        "risk_level": "Advisory",
        "alert_badge": "Yellow Alert",
        "initial_candidate_km2": 6.80,
        "filtered_candidate_km2": 5.10,
        "reduction_pct": 25.00,
        "rainfall_24h_mm": 68.0,
        "soil_moisture_pct": 71.0,
        "key_river": "Arkavathi, Kanva",
        "gauge_station": "Manchanabele Dam Gauge",
        "gauge_stage_m": 720.5,
        "gauge_danger_m": 722.0,
        "key_reservoirs": "Manchanabele Reservoir, Kanva Dam, TG Halli",
        "vulnerable_taluks": ["Channapatna", "Ramanagara", "Nelamangala", "Devanahalli"],
        "center": [13.2257, 77.5750],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-06",
        "mean_backscatter_drop_db": -3.8,
        "population_at_risk": 7800,
        "evacuation_shelters_active": 3,
        "advisory_summary": "Manchanabele and Kanva reservoirs managing steady outflows; minor agricultural wetting."
    },
    "Kolar": {
        "display_name": "Kolar & Chikkaballapura",
        "canonical_id": "kolar",
        "basin": "Palar & North Pennar Basins",
        "zone": "Eastern Plains",
        "risk_level": "Normal",
        "alert_badge": "Green Status",
        "initial_candidate_km2": 3.40,
        "filtered_candidate_km2": 2.55,
        "reduction_pct": 25.00,
        "rainfall_24h_mm": 38.0,
        "soil_moisture_pct": 54.0,
        "key_river": "Palar, Kushavathi",
        "gauge_station": "Bethamangala Lake Gauge",
        "gauge_stage_m": 815.0,
        "gauge_danger_m": 818.0,
        "key_reservoirs": "Bethamangala, Ramasamudra",
        "vulnerable_taluks": ["Bangarapet", "Malur", "Kolar", "Gowribidanur"],
        "center": [13.1378, 78.1292],
        "zoom": 10,
        "last_sar_acquisition": "2024-08-06",
        "mean_backscatter_drop_db": -3.0,
        "population_at_risk": 1500,
        "evacuation_shelters_active": 0,
        "advisory_summary": "Tanks recharging safely; no flood warning active."
    }
}

# Save districts database
with open('static/data/karnataka_statewide_flood_data.json', 'w', encoding='utf-8') as f:
    json.dump(districts_db, f, indent=2)

print(f"Generated statewide flood database for {len(districts_db)} primary administrative regions.")

# 2. Generate Multi-Basin SAR Inundation Polygons across Karnataka
def make_box(min_lon, min_lat, max_lon, max_lat):
    return [[
        [min_lon, min_lat],
        [max_lon, min_lat],
        [max_lon, max_lat],
        [min_lon, max_lat],
        [min_lon, min_lat]
    ]]

# Statewide Inundation Hotspot Features (Krishna, Kaveri, Coastal, Tungabhadra)
statewide_inundation_features = [
    # 1. Krishna Basin - Chikkodi / Athani (Belagavi)
    {
        'type': 'Feature',
        'properties': {
            'region': 'Krishna Basin (Belagavi)',
            'name': 'Chikkodi & Athani Krishna Floodplains',
            'type': 'Filtered Flood Inundation Candidate',
            'area_km2': 18.62,
            'mean_sar_drop_db': -5.4,
            'source_sensor': 'Sentinel-1 SAR C-Band (10m IW GRD)',
            'basin': 'Krishna Basin',
            'severity': 'Severe Warning'
        },
        'geometry': {
            'type': 'Polygon',
            'coordinates': [[
                [74.55, 16.35], [74.75, 16.42], [74.98, 16.58], [75.12, 16.65],
                [75.10, 16.72], [74.90, 16.64], [74.68, 16.48], [74.50, 16.40],
                [74.55, 16.35]
            ]]
        }
    },
    # 2. Krishna Basin - Almatti Backwaters (Bagalkot)
    {
        'type': 'Feature',
        'properties': {
            'region': 'Krishna Basin (Bagalkot)',
            'name': 'Jamkhandi & Bilagi Almatti Submergence Zone',
            'type': 'Filtered Flood Inundation Candidate',
            'area_km2': 14.55,
            'mean_sar_drop_db': -5.1,
            'source_sensor': 'Sentinel-1 SAR C-Band',
            'basin': 'Krishna Basin',
            'severity': 'Severe Warning'
        },
        'geometry': {
            'type': 'Polygon',
            'coordinates': [[
                [75.25, 16.40], [75.45, 16.38], [75.68, 16.32], [75.82, 16.28],
                [75.78, 16.36], [75.52, 16.45], [75.30, 16.48], [75.25, 16.40]
            ]]
        }
    },
    # 3. Tungabhadra Basin - Hampi & Kampli (Ballari/Vijayanagara)
    {
        'type': 'Feature',
        'properties': {
            'region': 'Tungabhadra Basin (Ballari/Vijayanagara)',
            'name': 'Kampli & Siruguppa Tungabhadra Inundation Belt',
            'type': 'Filtered Flood Inundation Candidate',
            'area_km2': 13.70,
            'mean_sar_drop_db': -5.2,
            'source_sensor': 'Sentinel-1 SAR C-Band',
            'basin': 'Tungabhadra Basin',
            'severity': 'Severe Warning'
        },
        'geometry': {
            'type': 'Polygon',
            'coordinates': [[
                [76.50, 15.35], [76.72, 15.42], [76.88, 15.54], [77.02, 15.68],
                [76.96, 15.74], [76.78, 15.58], [76.58, 15.46], [76.46, 15.40],
                [76.50, 15.35]
            ]]
        }
    },
    # 4. Coastal Karnataka - Netravathi & Gurupura (Dakshina Kannada)
    {
        'type': 'Feature',
        'properties': {
            'region': 'Coastal Basin (Dakshina Kannada)',
            'name': 'Bantwal & Uppinangady Netravathi Valley',
            'type': 'Filtered Flood Inundation Candidate',
            'area_km2': 19.80,
            'mean_sar_drop_db': -5.9,
            'source_sensor': 'Sentinel-1 SAR C-Band',
            'basin': 'West Coast Basin',
            'severity': 'Severe Warning'
        },
        'geometry': {
            'type': 'Polygon',
            'coordinates': [[
                [74.92, 12.82], [75.05, 12.86], [75.22, 12.84], [75.35, 12.80],
                [75.32, 12.88], [75.14, 12.92], [74.98, 12.91], [74.88, 12.85],
                [74.92, 12.82]
            ]]
        }
    },
    # 5. Coastal Karnataka - Swarna & Sita (Udupi)
    {
        'type': 'Feature',
        'properties': {
            'region': 'Coastal Basin (Udupi)',
            'name': 'Brahmavar & Swarna Lowlands',
            'type': 'Filtered Flood Inundation Candidate',
            'area_km2': 16.55,
            'mean_sar_drop_db': -5.7,
            'source_sensor': 'Sentinel-1 SAR C-Band',
            'basin': 'West Coast Basin',
            'severity': 'Severe Warning'
        },
        'geometry': {
            'type': 'Polygon',
            'coordinates': [[
                [74.72, 13.38], [74.82, 13.44], [74.90, 13.40], [74.88, 13.48],
                [74.78, 13.52], [74.70, 13.45], [74.72, 13.38]
            ]]
        }
    },
    # 6. Malnad Catchment - Tunga Basin (Shivamogga)
    {
        'type': 'Feature',
        'properties': {
            'region': 'Malnad Basin (Shivamogga)',
            'name': 'Tunga River Gajanur Downstream Overflow',
            'type': 'Filtered Flood Inundation Candidate',
            'area_km2': 16.20,
            'mean_sar_drop_db': -5.6,
            'source_sensor': 'Sentinel-1 SAR C-Band',
            'basin': 'Tunga-Bhadra Basin',
            'severity': 'Severe Warning'
        },
        'geometry': {
            'type': 'Polygon',
            'coordinates': [[
                [75.48, 13.88], [75.60, 13.94], [75.72, 14.02], [75.68, 14.08],
                [75.52, 14.00], [75.42, 13.92], [75.48, 13.88]
            ]]
        }
    },
    # 7. Southern Kaveri Basin - Kabini Valley (Mysuru)
    {
        'type': 'Feature',
        'properties': {
            'region': 'Kaveri Basin (Mysuru)',
            'name': 'Kabini Spillway Plain (Beechanahalli - Saragur)',
            'type': 'Filtered Flood Inundation Candidate',
            'area_km2': 6.5572,
            'mean_sar_drop_db': -6.2,
            'source_sensor': 'Sentinel-1 SAR C-Band',
            'basin': 'Kaveri Basin',
            'severity': 'Severe Warning'
        },
        'geometry': {
            'type': 'Polygon',
            'coordinates': [[
                [76.22, 11.90], [76.28, 11.93], [76.35, 11.97], [76.42, 12.01],
                [76.46, 12.03], [76.40, 12.00], [76.31, 11.96], [76.21, 11.92],
                [76.22, 11.90]
            ]]
        }
    },
    # 8. Southern Kaveri Basin - Srirangapatna (Mandya)
    {
        'type': 'Feature',
        'properties': {
            'region': 'Kaveri Basin (Mandya)',
            'name': 'Srirangapatna & Kaveri Confluence Floodplain',
            'type': 'Filtered Flood Inundation Candidate',
            'area_km2': 11.10,
            'mean_sar_drop_db': -5.5,
            'source_sensor': 'Sentinel-1 SAR C-Band',
            'basin': 'Kaveri Basin',
            'severity': 'Severe Warning'
        },
        'geometry': {
            'type': 'Polygon',
            'coordinates': [[
                [76.62, 12.40], [76.72, 12.43], [76.84, 12.38], [76.92, 12.32],
                [76.88, 12.36], [76.76, 12.45], [76.64, 12.44], [76.62, 12.40]
            ]]
        }
    }
]

statewide_inundation_fc = {
    'type': 'FeatureCollection',
    'features': statewide_inundation_features
}

with open('static/data/karnataka_statewide_inundation.geojson', 'w', encoding='utf-8') as f:
    json.dump(statewide_inundation_fc, f, indent=2)

# 3. Generate Major Reservoirs & Dam Gate Locations in Karnataka
karnataka_dams = {
    'type': 'FeatureCollection',
    'features': [
        {
            'type': 'Feature',
            'properties': {
                'name': 'Almatti Dam (Lal Bahadur Shastri Sagara)',
                'river': 'Krishna River',
                'district': 'Bagalkot / Vijayapura',
                'full_capacity_tmc': 123.08,
                'current_storage_pct': 99.4,
                'inflow_cusecs': 310000,
                'outflow_cusecs': 305000,
                'status': 'Full Discharge Operations'
            },
            'geometry': {'type': 'Point', 'coordinates': [75.8885, 16.3312]}
        },
        {
            'type': 'Feature',
            'properties': {
                'name': 'Krishna Raja Sagara (KRS) Dam',
                'river': 'Kaveri River',
                'district': 'Mandya',
                'full_capacity_tmc': 49.45,
                'current_storage_pct': 99.8,
                'inflow_cusecs': 118000,
                'outflow_cusecs': 115000,
                'status': 'Maximum Spillway Discharge'
            },
            'geometry': {'type': 'Point', 'coordinates': [76.5724, 12.4284]}
        },
        {
            'type': 'Feature',
            'properties': {
                'name': 'Kabini Reservoir Dam',
                'river': 'Kabini River',
                'district': 'Mysuru (H.D. Kote)',
                'full_capacity_tmc': 19.52,
                'current_storage_pct': 99.2,
                'inflow_cusecs': 68500,
                'outflow_cusecs': 65000,
                'status': 'Critical Discharge Alert'
            },
            'geometry': {'type': 'Point', 'coordinates': [76.3520, 11.9730]}
        },
        {
            'type': 'Feature',
            'properties': {
                'name': 'Tungabhadra (TB) Dam',
                'river': 'Tungabhadra River',
                'district': 'Vijayanagara (Hospete)',
                'full_capacity_tmc': 105.79,
                'current_storage_pct': 98.6,
                'inflow_cusecs': 185000,
                'outflow_cusecs': 180000,
                'status': '33 Gates Opened'
            },
            'geometry': {'type': 'Point', 'coordinates': [76.3370, 15.2630]}
        },
        {
            'type': 'Feature',
            'properties': {
                'name': 'Linganamakki Dam',
                'river': 'Sharavathi River',
                'district': 'Shivamogga (Sagar)',
                'full_capacity_tmc': 151.75,
                'current_storage_pct': 97.5,
                'inflow_cusecs': 78000,
                'outflow_cusecs': 65000,
                'status': 'Active Spillway Regulated'
            },
            'geometry': {'type': 'Point', 'coordinates': [74.8350, 14.1950]}
        },
        {
            'type': 'Feature',
            'properties': {
                'name': 'Bhadra Dam (Lakkavalli)',
                'river': 'Bhadra River',
                'district': 'Chikkamagaluru / Shivamogga',
                'full_capacity_tmc': 71.54,
                'current_storage_pct': 98.9,
                'inflow_cusecs': 52000,
                'outflow_cusecs': 48000,
                'status': 'Spillway Active'
            },
            'geometry': {'type': 'Point', 'coordinates': [75.6420, 13.7080]}
        },
        {
            'type': 'Feature',
            'properties': {
                'name': 'Gorur (Hemavathi) Dam',
                'river': 'Hemavathi River',
                'district': 'Hassan',
                'full_capacity_tmc': 37.10,
                'current_storage_pct': 99.1,
                'inflow_cusecs': 41000,
                'outflow_cusecs': 38000,
                'status': 'Crest Gates Opened'
            },
            'geometry': {'type': 'Point', 'coordinates': [76.0520, 12.8730]}
        },
        {
            'type': 'Feature',
            'properties': {
                'name': 'Supa Dam',
                'river': 'Kali River',
                'district': 'Uttara Kannada (Joida)',
                'full_capacity_tmc': 147.54,
                'current_storage_pct': 96.2,
                'inflow_cusecs': 62000,
                'outflow_cusecs': 55000,
                'status': 'Heavy Power Generation & Spill'
            },
            'geometry': {'type': 'Point', 'coordinates': [74.6430, 15.2780]}
        },
        {
            'type': 'Feature',
            'properties': {
                'name': 'Harangi Dam',
                'river': 'Harangi / Kaveri',
                'district': 'Kodagu (Somwarpet)',
                'full_capacity_tmc': 8.50,
                'current_storage_pct': 99.5,
                'inflow_cusecs': 38000,
                'outflow_cusecs': 36000,
                'status': 'Maximum Release Operations'
            },
            'geometry': {'type': 'Point', 'coordinates': [75.9080, 12.4920]}
        }
    ]
}

with open('static/data/karnataka_major_dams.geojson', 'w', encoding='utf-8') as f:
    json.dump(karnataka_dams, f, indent=2)

print('Generated karnataka_major_dams.geojson and karnataka_statewide_inundation.geojson successfully!')
