import numpy as np
import matplotlib.pyplot as plt

print("Reservoir Drive Mechanism Analyzer")

# --- Drive Mechanism Selection ---
drive_map = {
    "1": "Solution Gas Drive",
    "2": "Gas Cap Drive",
    "3": "Water Drive"
}

print("Select Drive Mechanism:")
for k, v in drive_map.items():
    print(f"{k}. {v}")

while True:
    drive_choice = input("Enter choice (1/2/3): ")
    if drive_choice in drive_map:
        drive_mechanism = drive_map[drive_choice]
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# --- User Inputs ---
p_initial = float(input("Enter Initial Reservoir Pressure (psi): "))
recovery_factor = float(input("Enter Recovery Factor (%): ")) / 100
q_i = float(input("Enter Initial Production Rate qᵢ (STB/day): "))

# --- Decline Model Selection ---
decline_map = {
    "1": "Exponential",
    "2": "Harmonic",
    "3": "Hyperbolic"
}

print("\nSelect Decline Model:")
for k, v in decline_map.items():
    print(f"{k}. {v}")

while True:
    decline_choice = input("Enter choice (1/2/3): ")
    if decline_choice in decline_map:
        decline_model = decline_map[decline_choice].lower()
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# --- Decline Parameters Input ---
D = float(input("Enter Decline Constant D (e.g., 0.2): "))
t_max = float(input("Enter Production Time Period (years): "))
num_points = int(input("Enter Number of Time Points for Plot (e.g., 100): "))

# --- Time Setup ---
t = np.linspace(0, t_max, num_points)

# --- Production Rate Calculation ---
if decline_model == "exponential":
    q = q_i * np.exp(-D * t)
elif decline_model == "harmonic":
    q = q_i / (1 + D * t)
elif decline_model == "hyperbolic":
    b = 0.5
    q = q_i / ((1 + b * D * t) ** (1 / b))

# --- Pressure Decline (Linear Approximation) ---
pressure = p_initial * (1 - recovery_factor * t / max(t))

# --- Plotting ---
plt.figure(figsize=(10, 4))

# Pressure vs Time
plt.subplot(1, 2, 1)
plt.plot(t, pressure, label="Reservoir Pressure", color='blue')
plt.title(f"{drive_mechanism} - Pressure vs Time")
plt.xlabel("Time (years)")
plt.ylabel("Pressure (psi)")
plt.grid(True)

# Production Rate vs Time
plt.subplot(1, 2, 2)
plt.plot(t, q, label="Production Rate", color='green')
plt.title(f"{decline_map[decline_choice]} Decline Curve")
plt.xlabel("Time (years)")
plt.ylabel("Production Rate (STB/day)")
plt.grid(True)

plt.tight_layout()
plt.show()