
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------ Constants & Assumptions ------------------------

weeks_per_month = 4.33

# Define family scenarios
data = {
    "Family": ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"],
    "Head Count": ["1 Adult", "1 Adult, 1 Kid", "2 Adult, 2 Kid", "1 Adult", "1 Adult", "2 Adult, 2 Kid"],
    "Monthly Income ($)": [
        16 * 40 * weeks_per_month,  # Red
        16 * 40 * weeks_per_month + 380,  # Green
        16 * 80 * weeks_per_month,  # Blue
        16 * 40 * weeks_per_month * 0.64,  # Yellow
        16 * 20 * weeks_per_month + 1000,  # Orange
        17.25 * 80 * weeks_per_month  # Purple
    ],
    "Apartment Type": ["Studio", "Studio", "2-Bedroom", "Studio", "Studio", "2-Bedroom"],
    "Rent Expectation ($)": [1777, 1777, 2544, 1777, 1777, 2544]
}

df = pd.DataFrame(data)

# ------------------------ Financial Calculations ------------------------

df["30% Income Needed ($)"] = df["Rent Expectation ($)"] / 0.30
df["Can Afford?"] = df["Monthly Income ($)"] >= df["30% Income Needed ($)"]
df["Hours Needed/Week (at $16/hr)"] = df["30% Income Needed ($)"] / (16 * weeks_per_month)

# ------------------------ Visualization ------------------------

plt.figure(figsize=(10, 6))
plt.bar(df["Family"], df["Hours Needed/Week (at $16/hr)"], color="darkorange", label="Hours Needed per Week")
plt.axhline(y=40, color='green', linestyle='--', label="40 hrs/week Benchmark")
plt.title("Weekly Work Hours Needed to Afford Rent (30% Rule, $16/hr)")
plt.xlabel("Family")
plt.ylabel("Hours per Week")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("/mnt/data/screenshot.png")
plt.show()

# ------------------------ Summary ------------------------

print("Minimum Wage (CA): $16.00/hr")
monthly_income = 16 * 40 * weeks_per_month
print(f"Monthly Income (Full-Time): ${monthly_income:.2f}")
print(f"Families Unable to Afford Rent (per 30% Rule): {(~df['Can Afford?']).sum()} of {len(df)}")
print("\nDetailed Family Data:\n")
print(df[["Family", "Apartment Type", "Monthly Income ($)", "30% Income Needed ($)", "Hours Needed/Week (at $16/hr)", "Can Afford?"]])
