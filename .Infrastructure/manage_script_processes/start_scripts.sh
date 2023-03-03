#!/bin/bash

# Define the path to the file containing script paths
SCRIPT_FILE="/home/chronos/processes/scripts.txt"

# Read the script paths from the file into an array
readarray -t SCRIPTS < "$SCRIPT_FILE"

# Initialize a variable to keep track of whether all scripts are running
all_running=true

# Loop over the script paths and check if each script is running
for script_path in "${SCRIPTS[@]}"
do
    #script=$(basename "$script_path")

    if ! pgrep -f "$script_path" > /dev/null
    then
        all_running=false
        echo "Script '$script_path' is not running. Starting..."
        "$script_path" &

        sleep 3

        # Check if the script started successfully
        if pgrep -f "$script_path" > /dev/null
        then
            echo "Script '$script_path' started successfully."
            all_running=true
        else
            echo "Failed to start script '$script_path'."
        fi
    fi
done

# Check if all scripts are running and print a message
if $all_running
then
    echo "All scripts are running."
else
    echo "Not all scripts are running."
fi
