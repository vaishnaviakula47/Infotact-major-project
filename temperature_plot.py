import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/baltimore_temp.csv")

plt.figure(figsize=(12, 6))

plt.plot(df["Date - Time"], df["H16"])

plt.title("Baltimore Temperature Variation Over Time")
plt.xlabel("Date - Time")
plt.ylabel("Temperature")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("visualizations/baltimore_temperature.png")

plt.show()
