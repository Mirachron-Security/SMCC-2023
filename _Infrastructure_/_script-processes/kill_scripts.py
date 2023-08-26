#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

import os
import subprocess
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

def kill_process(process_name):
    try:
        subprocess.run(["pkill", "-f", process_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def get_full_script_paths(script_names):
    return [os.path.abspath(script) for script in script_names]

def check_and_kill_scripts(script_paths):
    running_scripts = []

    for script_path in script_paths:
        script_name = os.path.basename(script_path)
        if is_process_running(script_name):
            running_scripts.append(script_path)
            
    if running_scripts:
        print(f"{R}[-] Running scripts detected:{NO}")
        all_killed = True
        for script in running_scripts:
            if kill_process(os.path.basename(script)):
                print(f"{R}[*] {NO}{script!r}{R} has been killed.{NO}")
            else:
                print(f"{R}[*] {script} could not be killed.{NO}")
                all_killed = False
        
        if all_killed:
            print(f"\n{G}[+] All scripts are successfully killed.{NO}")
        else:
            print(f"\n{R}[-] Some scripts are still running after kill attempt.{NO}")
    else:
        print(f"{G}\n[+] No running scripts detected.{NO}")

    return running_scripts

def main():
    full_script_paths = get_full_script_paths(script_paths)
    check_and_kill_scripts(full_script_paths)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[-] Script terminated by user.{NO}")
    except Exception as e:
        print(f"\n{R}[-] An error occurred:{NO}", str(e))
