# Write a python program that notifies you on a newly started process,
# the python port and the process id,  user account and the date of the currently 
# started operations Should be displayed.


import psutil
import datetime
import time

notified_processes = set()

while True:
    for process in psutil.process_iter(['pid', 'name', 'username', 'create_time']):
        try:
            if time.time() - process.info['create_time'] < 5 and process.info['pid'] not in notified_processes:
                notified_processes.add(process.info['pid'])
                print(f"New process started - PID: {process.info['pid']}, Name: {process.info['name']}, User: {process.info['username']}, Start Time: {datetime.datetime.fromtimestamp(process.info['create_time']).strftime('%Y-%m-%d %H:%M:%S')}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    time.sleep(1)
