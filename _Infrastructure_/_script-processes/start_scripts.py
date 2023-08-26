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

scripts = ["discord-creds-bot.py", ]#"verify_srv.py"]
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
    subprocess.Popen(["python3", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return is_process_running(os.path.basename(script_path))

def get_full_script_paths(script_names):
    return [os.path.abspath(script) for script in script_names]

def check_and_start_scripts(script_paths):
    non_running_scripts = []

    for script_path in script_paths:
        script_name = os.path.basename(script_path)
        if not is_process_running(script_name):
            non_running_scripts.append(script_path)
            print(f"{R}[*] Non-running scripts detected:{NO}")
            print(f"{R}[-] {NO}{script_path!r}{R} is not running. Starting...{NO}", end="")
            if start_process(script_path):
                print(f"\t{G}Done!{NO}")
            else:
                print(f"{R}[*] {NO}{script_path!r}{R} could not be started.{NO}")
        
    if non_running_scripts:
        print(f"\n{G}[*] Waiting for a few seconds to let the scripts start...{NO}")
        time.sleep(5)  # Wait for 5 seconds
        
        still_non_running_scripts = [script for script in non_running_scripts if not is_process_running(os.path.basename(script))]
        if still_non_running_scripts:
            print(f"\n{R}[-] The following scripts are still not running after start attempt:{NO}")
            for script in still_non_running_scripts:
                print(f"{script!r}")
        else:
            print(f"\n{G}[+] All non-running scripts are successfully started.{NO}")
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
