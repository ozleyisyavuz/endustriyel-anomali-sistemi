import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("sample_production_data.csv")

features = df[["temperature_c", "vibration_mm_s", "current_a", "voltage_v", "power_w", "cycle_time_s"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

model = IsolationForest(contamination=0.03, random_state=42)
df["anomaly_pred"] = model.fit_predict(X_scaled)

df["anomaly_pred"] = df["anomaly_pred"].map({1: "normal", -1: "anomaly"})

df.to_csv("analyzed_production_data.csv", index=False)

print("Analiz tamamlandı: analyzed_production_data.csv")
print(df["anomaly_pred"].value_counts())
