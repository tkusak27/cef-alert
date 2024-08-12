from utils.schedule_monitor import has_run_today, update_last_run_date

def main():
    if not has_run_today():
        # Your task here
        print("Task running")

        # Update the log to mark that the task has run today
        update_last_run_date()
    else:
        print("Task has already run today.")

if __name__ == "__main__":
    main()