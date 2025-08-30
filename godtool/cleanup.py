import sys
sys.path.append(".")
from utils.scheduler import scheduler_instance
scheduler_instance.clear_all_jobs()
print("All jobs cleared!")

