import subprocess
import requests

WEBHOOK_URL = "add your url here"
CONTAINER_NAME = "navidrome"  

def get_status():
    result = subprocess.run(
        ["docker", "inspect", "--format", "{{.State.Status}}", CONTAINER_NAME],
        capture_output=True, text=True
    )
    return result.stdout.strip() == "running"

def notify(is_running):
    msg = ":) Navidrome is **UP**" if is_running else ":( Navidrome is **DOWN**"
    requests.post(WEBHOOK_URL, json={"content": msg})

notify(get_status())
