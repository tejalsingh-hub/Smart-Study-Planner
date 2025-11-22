import json
from pathlib import Path
from typing import List
from .models import Task

DATA_FILE = Path("data/tasks.json")

def _ensure_datafile():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text(json.dumps({"next_id": 1, "tasks": []}, indent=2))

def load_tasks() -> List[Task]:
    _ensure_datafile()
    raw = json.loads(DATA_FILE.read_text())
    tasks_list = raw.get("tasks", [])
    tasks = []
    for t in tasks_list:
        tasks.append(Task(**t))
    return tasks

def save_tasks(tasks: List[Task]):
    _ensure_datafile()
    raw = {
        "next_id": max((t.id for t in tasks), default=0) + 1,
        "tasks": [t.__dict__ for t in tasks]
    }
    DATA_FILE.write_text(json.dumps(raw, indent=2))
