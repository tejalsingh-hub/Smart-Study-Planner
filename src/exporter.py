# src/exporter.py
import csv
from datetime import date
from typing import Dict, List

def export_schedule_csv(schedule: Dict[date, List], filename="report/schedule.csv"):
    # Ensure report folder exists
    import os
    os.makedirs("report", exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "task_id", "title", "subject", "hours"])
        for d, items in schedule.items():
            for it in items:
                writer.writerow([d.isoformat(), it["task_id"], it["title"], it["subject"], it["hours"]])
    return filename
