#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

import subprocess
import os

# Colored output
R = "\033[0;31m"
G = "\033[0;32m"
C = "\033[0;36m"
NO = "\033[0m"

python_packages = ["docker","inputimeout","logging","discord","textwrap"]
linux_binaries = ["wget","socat","docker.io"]

def check_requirements(requirements, check_func, install_func, message):
    try:
        missing_requirements = [req for req in requirements if not check_func(req)]
    except ValueError as e:
        print(f"{R}{e}{NO}")
        exit()

    if missing_requirements:
        print(f"{C}[*] Missing {message}:", ", ".join(missing_requirements),f"{NO}")
        install_missing_requirements(missing_requirements, install_func)
    else:
        print(f"{G}[+] All required {message.lower()} are installed.{NO}")

def check_python_package(package):
    try:
        __import__(package)
        return True
    except ImportError:
        return False

def check_linux_binary(binary):
    try:
        subprocess.run(["which", binary], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_missing_requirements(requirements, install_func):
    for requirement in requirements:
        print(f"{C}Installing {requirement}...{NO}")
        install_func(requirement)
    print(f"\n{G}[+]Installation complete.{NO}")

def install_python_package(package):
    subprocess.run(["pip", "install", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

def install_linux_binary(binary):
    try:
        os.system(f"sudo apt-get install -y {binary}")
    except:
        print(f"Error installing {binary}.")

if __name__ == "__main__":    
    check_requirements(python_packages, check_python_package, install_python_package, "Python Packages")
    check_requirements(linux_binaries, check_linux_binary, install_linux_binary, "Linux Binaries")
