import argparse
from datetime import date
from .storage import load_tasks, save_tasks
from .scheduler import generate_schedule
from .analytics import plot_workload
from .exporter import export_schedule_csv

def main():
    parser = argparse.ArgumentParser(description="Smart Study Planner CLI")
    sub = parser.add_subparsers(dest="command")

    # Add task
    add = sub.add_parser("add")
    add.add_argument("--title", required=True)
    add.add_argument("--subject", required=True)
    add.add_argument("--est_hours", required=True, type=float)
    add.add_argument("--priority", required=True, type=int)
    add.add_argument("--deadline", required=True)

    # List tasks
    sub.add_parser("list")

    # Generate schedule
    gen = sub.add_parser("generate")
    gen.add_argument("--daily_hours", required=True, type=float)
    gen.add_argument("--days", required=True, type=int)

    args = parser.parse_args()

    if args.command == "add":
        tasks = load_tasks()
        new_id = max([t.id for t in tasks], default=0) + 1
        from .models import Task
        t = Task(
            id=new_id,
            title=args.title,
            subject=args.subject,
            est_hours=args.est_hours,
            priority=args.priority,
            deadline=args.deadline
        )
        tasks.append(t)
        save_tasks(tasks)
        print("Task added!")

    elif args.command == "list":
        tasks = load_tasks()
        if not tasks:
            print("No tasks found.")
        for t in tasks:
            print(f"{t.id}. {t.title} | {t.subject} | {t.est_hours}h | Priority {t.priority} | Deadline {t.deadline}")

    elif args.command == "generate":
        tasks = load_tasks()
        today = date.today()
        schedule = generate_schedule(
            start_date=today,
            daily_hours=args.daily_hours,
            tasks=tasks,
            days=args.days,
        )

        print("\nGenerated Study Schedule:")
        for d, items in schedule.items():
            print(f"\n{d}:")
            for it in items:
                print(f"  - {it['title']} ({it['subject']}) → {it['hours']} hrs")

        # Export files
        export_schedule_csv(schedule)
        plot_workload(schedule)
        print("\nFiles generated in 'report/' folder:")
        print("- schedule.csv")
        print("- workload.png")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
