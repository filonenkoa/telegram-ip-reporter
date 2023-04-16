# Telegram Ip Reporter
A simple Python app to report the machine's name and IP addresses via a Telegram bot

## Requirements:
- aiogram
- python-dotenv

## Installation
### Linux
- Clone the repository: 
```console
git clone https://github.com/filonenkoa/telegram-ip-reporter.git
```
- Enter the repository
```console
cd telegram-ip-reporter
```
- Enter the Telegram bot API key into `.env` file:
```console
cp .env.template .env & nano .env
```
- Create Python's virtual environment:
```console
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

- Create a daemon file:
```console
sudo nano /etc/systemd/system/telegram-ip-reporter.service
```
- Enter the following text in the newly created file and replace `/home/alex/code` with the actual code directory:
```yaml
[Unit]
Description=A script for reporting this machine's name and IP adresses via Telegram
After=syslog.target network.target

[Service]
WorkingDirectory=/home/alex/code/telegram-ip-reporter
ExecStart=/home/alex/code/telegram-ip-reporter/venv/bin/python3 /home/alex/code/telegram-ip-reporter/main.py

Restart=always
RestartSec=120

[Install]
WantedBy=multi-user.target
```
- Reload the daemon manager
```console
sudo systemctl daemon-reload
 ```

- Start your daemon
```console
sudo systemctl start telegram-ip-reporter
```
- Check the status
```console
sudo systemctl status telegram-ip-reporter
```
If everything is fine, you should see the "active" status
- Add the newly created service to the autostart list:
```console
sudo systemctl enable telegram-ip-reporter
```