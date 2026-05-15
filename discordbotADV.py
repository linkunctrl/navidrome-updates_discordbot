#This version sends updates only when the state of the navidrome container changes
#Replace the 0 with * in your cronjob for this version to work well


import subprocess
import requests
import os

WEBHOOK_URL = "webhooks url goes here"
CONTAINER_NAME = "navidrome"
STATE_FILE = "/tmp/navidrome_last_state"

def get_status():
    result = subprocess.run(
        ["docker", "inspect", "--format", "{{.State.Status}}", CONTAINER_NAME],
        capture_output=True, text=True
    )
    return result.stdout.strip() == "running"

def notify(is_running):
    msg = ":3 the music server is **UP**" if is_running else ":p the music server is **DOWN**"
    requests.post(WEBHOOK_URL, json={"content": msg})

current = get_status()

if os.path.exists(STATE_FILE):
    with open(STATE_FILE) as f:
        last = f.read().strip() == "True"
    if current != last:
        notify(current)
else:
    notify(current)

with open(STATE_FILE, "w") as f:
    f.write(str(current))
