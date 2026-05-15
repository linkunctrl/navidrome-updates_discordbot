import subprocess
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1504796089184813198/_Qgx3EiDWKwPhpxysTK-TLbWa_7bP42dWRwjQWLcdHGGckGC2wNqQqs2iv4xKGQvkste"
CONTAINER_NAME = "navidrome"  # run: docker ps | grep navidrome  to confirm

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
