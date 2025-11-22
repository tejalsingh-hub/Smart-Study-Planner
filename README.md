# Smart Study Planner

A Python-based **Smart Study Planner** that generates personalized study schedules using **task priority, deadlines, and workload analysis**.  
It helps students plan their study sessions efficiently and avoid last-minute stress by distributing workload intelligently across days.

---

## 📌 Project Overview
The Smart Study Planner is a command-line application designed to assist students in creating and maintaining effective study plans.  
Users can add tasks, specify estimated effort, set priorities and deadlines, and generate a balanced multi-day study schedule.

The planner uses a **priority + earliest-deadline-first algorithm** combined with workload distribution to produce optimized study plans.

---

## ⭐ Features
- **Task Management (CRUD)**  
  Add, list, and manage study tasks with title, subject, hours, priority, and deadline.

- **Personalized Schedule Generation**  
  Generates a multi-day study plan customized according to:
  - Task priority  
  - Task deadlines  
  - Estimated workload  
  - User’s available daily study hours  

- **Workload Analytics**  
  Generates daily workload statistics and a workload plot.

- **Export Options**  
  Export the generated study schedule in CSV format.

- **Simple, Modular Codebase**  
  Clean folder structure with separate modules for scheduling, storage, analytics, and exporting.

- **Unit Tests Included**  
  Tests for core scheduler logic using `pytest`.

---

## 🛠 Technologies / Tools Used
- **Python 3.10+**
- **matplotlib** — workload graph
- **pytest** — unit testing
- **JSON storage** — for task persistence
- **CSV export** — for schedules

---

## 🚀 Installation & Running the Project

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd smart-study-planner
