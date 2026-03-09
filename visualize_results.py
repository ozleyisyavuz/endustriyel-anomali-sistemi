import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("analyzed_production_data.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])

plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["temperature_c"], label="Temperature (C)")
anomalies = df[df["anomaly_pred"] == "anomaly"]
plt.scatter(anomalies["timestamp"], anomalies["temperature_c"], label="Anomaly", marker="x")
plt.title("Temperature Over Time with Detected Anomalies")
plt.xlabel("Time")
plt.ylabel("Temperature (C)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temperature_anomalies.png")
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["power_w"], label="Power (W)")
plt.title("Power Consumption Over Time")
plt.xlabel("Time")
plt.ylabel("Power (W)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("power_consumption.png")
plt.show()

print("Grafikler oluşturuldu: temperature_anomalies.png, power_consumption.png")
