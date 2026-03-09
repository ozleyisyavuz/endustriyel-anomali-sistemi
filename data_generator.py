import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

n = 1000
start_time = datetime.now()

timestamps = [start_time + timedelta(minutes=i) for i in range(n)]

temperature = np.random.normal(loc=75, scale=3, size=n)
vibration = np.random.normal(loc=2.5, scale=0.4, size=n)
current = np.random.normal(loc=12, scale=1.0, size=n)
voltage = np.random.normal(loc=220, scale=5, size=n)
cycle_time = np.random.normal(loc=30, scale=2, size=n)

power = voltage * current

status = np.array(["normal"] * n)

anomaly_indices = np.random.choice(n, size=30, replace=False)
temperature[anomaly_indices] += np.random.uniform(8, 15, size=30)
vibration[anomaly_indices] += np.random.uniform(1.5, 3.0, size=30)
current[anomaly_indices] += np.random.uniform(3, 6, size=30)
status[anomaly_indices] = "anomaly"

df = pd.DataFrame({
    "timestamp": timestamps,
    "temperature_c": temperature,
    "vibration_mm_s": vibration,
    "current_a": current,
    "voltage_v": voltage,
    "power_w": power,
    "cycle_time_s": cycle_time,
    "status": status
})

df.to_csv("sample_production_data.csv", index=False)
print("Veri oluşturuldu: sample_production_data.csv")
