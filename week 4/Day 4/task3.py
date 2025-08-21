import os
from datetime import datetime
import getpass  # safer alternative to os.getlogin()

print("===== System Information Tool =====\n")

# Current date and time
print("Current Date and Time:")
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# OS name
print("\nOS Name:")
print(os.name)

# Current working directory
print("\nCurrent Working Directory:")
print(os.getcwd())

# Environment variables
print("\nEnvironment Variables:")
for key, value in os.environ.items():
    print(f"{key} = {value}")

# User login name
print("\nUser Login Name:")
print(getpass.getuser())  # safer than os.getlogin()

# Process ID
print("\nCurrent Process ID:")
print(os.getpid())

# List files and folders
print("\nFiles and Folders in Current Directory:")
for item in os.listdir():
    print(item)

# CPU Count
print("\nNumber of CPUs:")
print(os.cpu_count())

# System Boot Time - OPTIONAL (requires psutil)
try:
    import psutil
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.fromtimestamp(boot_time_timestamp)
    print("\nSystem Boot Time:")
    print(boot_time.strftime("%Y-%m-%d %H:%M:%S"))
except ImportError:
    print("\npsutil not installed. Skipping boot time info.")

print("\n===== End of System Information =====")
