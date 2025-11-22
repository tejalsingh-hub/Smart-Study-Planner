import matplotlib.pyplot as plt
from datetime import date
from typing import Dict, List

def plot_workload(schedule: Dict[date, List], output_path="report/workload.png"):
    # Prepare x-axis and y-axis data
    days = list(schedule.keys())
    hours = [sum(item["hours"] for item in schedule[d]) for d in days]

    # Create report folder if needed
    import os
    os.makedirs("report", exist_ok=True)

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(days, hours, marker="o")
    plt.xlabel("Date")
    plt.ylabel("Planned Study Hours")
    plt.title("Daily Workload Distribution")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
