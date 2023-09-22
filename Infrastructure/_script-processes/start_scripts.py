#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

import os, sys
import subprocess
import time

# Custom functions
from find_path import find_path

# Colored output
R = "\033[0;31m"
G = "\033[0;32m"
NO = "\033[0m"

scripts = ["discord-creds-bot.py", "verify_srv.py"]

# Get the full paths of the scripts required
script_paths = []
for script in scripts:
    script_path = find_path('.', script)
    script_paths.append(script_path)


# Check if the script is running
def is_process_running(process_name):
    try:
        subprocess.run(["pgrep", "-f", process_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


# Execute the script
def start_process(script_path):
    try:
        subprocess.Popen(["python3", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as e:
        print(f"{R}[*] {NO}{script_path!r}{R} could not be started. Error: {e}{NO}")
        return False


# If the script is not running, execute it
def check_and_start_scripts(script_paths):
    non_running_scripts = []
    any_script_not_running = False

    print(f"{G}[*] Chosen scripts to start:{NO}")
    for script_path in script_paths:
        print(f"{script_path!r}")
    
    for script_path in script_paths:
        script_name = os.path.basename(script_path)
        if not is_process_running(script_name):
            non_running_scripts.append(script_path)
            any_script_not_running = True
    
    # If at least one script is not running
    if any_script_not_running:
        print(f"\n{R}[*] Non-running scripts detected:{NO}")
        for script_path in non_running_scripts:
            time.sleep(1)
            print(f"{R}[-] Starting {NO}{script_path!r}",end="",flush=True)
            if start_process(script_path):
                time.sleep(1)
                print(f"\t{G}Done!{NO}")
            else:
                print(f"{R}[*] {NO}{script_path!r}{R} could not be started.{NO}")
        
        time.sleep(1)
        print(f"\n{G}[*] Re-checking running status after start attempt...{NO}\n")
        time.sleep(4)  

        all_running = True
        for script_path in script_paths:
            script_name = os.path.basename(script_path)
            if not is_process_running(script_name):
                print(f"{R}[-] {NO}{script_path!r}{R} is not running.{NO}")
                all_running = False
        if all_running:
            print(f"{G}[+] All scripts are running now.{NO}")

    else:
        print(f"{G}\n[+] All scripts are already running.{NO}")

    return non_running_scripts

def main():
    check_and_start_scripts(script_paths)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[-] Script terminated by user.{NO}")
    except Exception as e:
        print(f"\n{R}[-] An error occurred:{NO}", str(e))
