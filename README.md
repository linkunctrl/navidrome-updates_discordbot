# navidrome-updates_discordbot
A Python-based Discord bot that provides automated, hourly status updates for your Navidrome media server. It monitors service availability and broadcasts health metrics directly to a designated Discord channel.

### Webhooks URL
   After creating your server, go to the server settings -> Integrations and create a new webhook.
   Save this url as this will be pasted in your python script.

### Prerequisites 
  ```bash
  sudo pacman -S python-requests (if you're on arch)
  OR
  pip install requests
```
Use the following to confirm your docker container name
```bash
  docker ps | grep navidrome
```
  
### Script
  Copy the above python script and add your webhooks URL and container details in it.

### Hourly updates
  Create a cronjob for hourly updates
  ```bash
  0 * * * * /usr/bin/python3 /path/to/discordbot.py
```
  
