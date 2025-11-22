from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    subject: str
    est_hours: float
    priority: int          # 1 (low) - 5 (high)
    deadline: str          # ISO date: YYYY-MM-DD
    completed_hours: float = 0.0
    notes: Optional[str] = None

    def remaining(self) -> float:
        return max(0.0, float(self.est_hours) - float(self.completed_hours))
