# AutoClaimBot
Этот бот позволяет собирать награды в различных ботах

# setup
## CLI
```bash
git clone https://github.com/jintaxi/AutoClaimBot.git
cd AutoClaimBot
python -m venv .env
.\.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
## Docker
`docker run -v ./.env:/app/.env:ro -v ./session.session:/app/session.session --name AutoClaimBot --restart unless-stopped jintaxi/autoclaimbot:latest`
## Docker compose
```docker compose
version: "3.9"

services:
  AutoClaimBot:
    image: jintaxi/autoclaimbot:latest
    container_name: AutoClaimBot
    restart: unless-stopped
    volumes:
      - ./.env:/app/.env:ro
      - ./session.session:/app/session.session
```

or 

```bash
git clone https://github.com/jintaxi/AutoClaimBot.git
cd AutoClaimBot
docker compose up -d
```