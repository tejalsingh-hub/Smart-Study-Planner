from datetime import date, timedelta
from src.scheduler import generate_schedule
from src.models import Task

def test_scheduler_basic():
    start = date.today()
    tasks = [
        Task(id=1, title="T1", subject="S", est_hours=4, priority=5, deadline=(start + timedelta(days=1)).isoformat()),
        Task(id=2, title="T2", subject="S", est_hours=2, priority=3, deadline=(start + timedelta(days=3)).isoformat()),
    ]
    sched = generate_schedule(start, daily_hours=4.0, tasks=tasks, days=3)
    total_assigned = sum(item["hours"] for day in sched.values() for item in day)
    assert round(total_assigned, 2) == 6.0
