# src/scheduler.py
from datetime import datetime, timedelta, date
from typing import List, Dict
from .models import Task

def parse_date(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()

def generate_schedule(start_date: date, daily_hours: float, tasks: List[Task], days: int = 7) -> Dict[date, List]:
    """
    Simple greedy scheduler:
    - Sort tasks by (deadline, -priority)
    - For each day from start_date for `days`, assign available capacity to earliest deadline tasks
    - Return schedule: {date: [ {"task_id":..., "title":..., "hours":..., "subject":...}, ... ] }
    """
    pending = [t for t in tasks if t.remaining() > 1e-6]
    # sort pending list by deadline then by higher priority
    pending.sort(key=lambda t: (parse_date(t.deadline), -t.priority))
    schedule = {}
    day_list = [start_date + timedelta(days=i) for i in range(days)]

    for d in day_list:
        cap = daily_hours
        schedule[d] = []
        # re-sort daily to pick up any changed priorities
        pending.sort(key=lambda t: (parse_date(t.deadline), -t.priority))
        i = 0
        while cap > 1e-6 and i < len(pending):
            t = pending[i]
            rem = t.remaining()
            if rem <= 1e-6:
                i += 1
                continue
            days_left = (parse_date(t.deadline) - d).days
            # urgency factor: more urgent tasks are treated slightly preferentially
            urgency_factor = 2.0 if days_left <= 0 else (1.5 if days_left <= 2 else 1.0)
            # simple greedy assign: min(remaining, cap)
            assign = min(rem, cap)
            t.completed_hours += assign
            cap -= assign
            schedule[d].append({"task_id": t.id, "title": t.title, "hours": round(assign, 2), "subject": t.subject})
            if t.remaining() <= 1e-6:
                pending.pop(i)
            else:
                i += 1
    return schedule
