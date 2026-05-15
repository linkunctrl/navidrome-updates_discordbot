
import subprocess
import requests
import os

WEBHOOK_URL = "https://discord.com/api/webhooks/1504796089184813198/_Qgx3EiDWKwPhpxysTK-TLbWa_7bP42dWRwjQWLcdHGGckGC2wNqQqs2iv4xKGQvkste"
CONTAINER_NAME = "navidrome"
STATE_FILE = "/tmp/navidrome_last_state"

def get_status():
    result = subprocess.run(
        ["docker", "inspect", "--format", "{{.State.Status}}", CONTAINER_NAME],
        capture_output=True, text=True
    )
    return result.stdout.strip() == "running"

def notify(is_running):
    msg = ":3 zee moosik server is **UP**" if is_running else ":p zee moosik server is **DOWN**"
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
