import subprocess

# Get the list of deleted files matching the pattern using grep
git_status_output = subprocess.check_output(["git", "status", "--porcelain"]).decode("utf-8")
deleted_files = [line.split(" ", 1)[2] for line in git_status_output.splitlines() if line.startswith("D ")]
print(deleted_files)

# Restore each deleted file
for file_path in deleted_files:
    if "intro.md" in file_path:
        subprocess.run(["git", "restore", "--", file_path])
