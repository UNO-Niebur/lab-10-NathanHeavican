#MapPlot.py
#Name: Nathan Heavican
#Date: 4/9/2026
#Assignment: Lab 10

# Step 1
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("reaction_time_data.csv")

# Step 4
df = df[df["ReactionTime_ms"] > 0]

# Step 2
trials = df["Trial"]
reaction_times = df["ReactionTime_ms"]

# Step 3
plt.plot(trials, reaction_times)
plt.xlabel("Trial")
plt.ylabel("Reaction Time (ms)")
plt.savefig("reaction_graph.png")
plt.show()