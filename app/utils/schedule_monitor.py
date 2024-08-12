# script.py
import datetime
import os
from utils.helpers import get_path

def get_log_file_path():
    cwd = os.path.dirname(get_path())
    return f"{cwd}/logs/runs.log"
    

def has_run_today():
    log_file = get_log_file_path()
    print(log_file)

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            last_run_date = f.read().strip()
            today_date = datetime.date.today().isoformat()
            return last_run_date == today_date
    return False

def update_last_run_date():
    log_file = get_log_file_path()
    print(log_file)

    with open(log_file, "w") as f:
        f.write(datetime.date.today().isoformat())