import pandas as pd
import random
from datetime import datetime, timedelta

# Settings
num_rows = 100
start_time = datetime.now()

data = []

for i in range(num_rows):
    timestamp = start_time + timedelta(minutes=i * 5)
    machine_id = f"MCH-{random.randint(1, 5)}"
    temp = round(random.uniform(60, 100), 2)
    vibration = round(random.uniform(0.2, 1.2), 2)
    pressure = round(random.uniform(4.5, 6.5), 2)
    uptime = random.randint(100, 1000)
    status = random.choice(["Running", "Alert", "Failure"])

    data.append([timestamp, machine_id, temp, vibration, pressure, uptime, status])

# Create DataFrame
df = pd.DataFrame(data, columns=["Timestamp", "Machine_ID", "Temp", "Vibration", "Pressure", "Uptime", "Status"])

# Save as CSV
df.to_csv("../data/machine_data.csv", index=False)

print("✅ Machine data generated successfully!")
