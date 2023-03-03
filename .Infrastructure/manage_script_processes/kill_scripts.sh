#!/bin/bash

# Define an array of script names to check
SCRIPTS=(
    "/home/chronos/discord/discord-creds-bot.py"
    "/home/chronos/forensics/sniff_away/verify_srv.py"
)

# Loop over the script names and find the process IDs of each script
for script_path in "${SCRIPTS[@]}"
do
    script=$(basename "$script_path")
    # Use pgrep to find the process ID(s) of the script
    pids=$(pgrep -f "$script")

    if [ -z "$pids" ]; then
        echo "Script $script is not running."
    else
        echo "Script $script is running with PID(s): $pids"
        # Loop over the process IDs and kill each one
        for pid in $pids
        do
            if [[ $pid != $$ ]]; then # skip the current process running the script
                echo "Killing process with ID $pid (script: $script)..."
                kill $pid
            fi
        done
        echo ""
    fi
done
