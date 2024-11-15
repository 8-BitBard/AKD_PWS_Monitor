import psutil
import subprocess
import time
import logging
from logging.handlers import RotatingFileHandler

# Function to check if there is a process running that contains the given name
def is_process_running(process_name):
    process_name = process_name.lower()
    for proc in psutil.process_iter(["name"]):
        try:
            if process_name in proc.info["name"].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

# Specify the name of the process
process_name = "PWSvr"

# Set up logging
handler = RotatingFileHandler("akd_pws_monitor_log.txt", maxBytes=1024*1024, backupCount=5)
logging.basicConfig(handlers=[handler], level=logging.INFO,
                    format="%(asctime)s %(levelname)s:%(message)s")

# Check if the process is running
while True:
    if not is_process_running(process_name):
        executable_path = r"C:\SoftDent\PWSvr\PWSvr.exe"
        try:
            subprocess.Popen([executable_path])
            logging.info(f"{process_name} was not running and has been started.")
        except Exception as e:
            logging.info(f"Failed to start {process_name}: {e}")
    else:
        pass
    time.sleep(300) # time in seconds to wait until next check
