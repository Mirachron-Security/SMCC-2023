#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

import os
import subprocess
import time
from find_scripts import script_names 

scripts = ["discord-creds-bot.py", "verify_srv.py"]
script_paths = script_names(scripts)

# Colored output
R = "\033[0;31m"
G = "\033[0;32m"
NO = "\033[0m"

def is_process_running(process_name):
    try:
        subprocess.run(["pgrep", "-f", process_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def start_process(script_path):
    try:
        subprocess.Popen(["python3", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as e:
        print(f"{R}[*] {NO}{script_path!r}{R} could not be started. Error: {e}{NO}")
        return False

def get_full_script_paths(script_names):
    return [os.path.abspath(script) for script in script_names]

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
    
    if any_script_not_running:
        print(f"\n{R}[*] Non-running scripts detected:{NO}")
        for script_path in non_running_scripts:
            print(f"{R}[-] {NO}{script_path!r}{R} is not running. Starting...", end="")
            if start_process(script_path):
                print(f"{G} Done!{NO}")
            else:
                print(f"{R}[*] {NO}{script_path!r}{R} could not be started.{NO}")
        
        print(f"\n{G}[*] Waiting for a few seconds to let the scripts start...{NO}\n")
        time.sleep(5)  # Wait for 5 seconds
        
        print(f"{G}[*] Re-checking running status after start attempt...{NO}")
        for script_path in script_paths:
            script_name = os.path.basename(script_path)
            if not is_process_running(script_name):
                print(f"{R}[-] {NO}{script_path!r}{R} is still not running.{NO}")
    else:
        print(f"{G}\n[+] All scripts are already running.{NO}")

    return non_running_scripts

def main():
    full_script_paths = get_full_script_paths(script_paths)
    check_and_start_scripts(full_script_paths)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[-] Script terminated by user.{NO}")
    except Exception as e:
        print(f"\n{R}[-] An error occurred:{NO}", str(e))
