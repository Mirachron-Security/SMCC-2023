import subprocess
import os

def check_requirements(requirements, check_func, install_func, message):
    missing_requirements = [req for req in requirements if not check_func(req)]
    
    if missing_requirements:
        print(f"Missing {message}:", ", ".join(missing_requirements))
        install_missing_requirements(missing_requirements, install_func)
    else:
        print(f"All required {message.lower()} are installed.")

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
        print(f"Installing {requirement}...")
        install_func(requirement)
    print("Installation complete.")

def install_python_package(package):
    subprocess.run(["pip", "install", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

def install_linux_binary(binary):
    try:
        os.system(f"sudo apt-get install -y {binary}")
    except:
        print(f"Error installing {binary}.")

if __name__ == "__main__":
    python_packages = ["requests", "numpy", "matplotlib"]
    linux_binaries = ["curl", "grep", "awk", "stegseek"]
    
    check_requirements(python_packages, check_python_package, install_python_package, "Python Packages")
    check_requirements(linux_binaries, check_linux_binary, install_linux_binary, "Linux Binaries")
