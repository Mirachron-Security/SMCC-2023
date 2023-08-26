### Set crontabs for start_scripts.sh and start_dockers.sh at reboot

```bash
crontab -e
# 1 -- nano
# @reboot /home/chronos/processes/dockers/start_dockers.sh
# @reboot /home/chronos/processes/scripts/start_scripts.sh
