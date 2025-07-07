# Telegram Bot Deployment

## Prerequisiti
- Account Telegram con @BotFather per generare il token
- Account Render.com per l'hosting

## Configurazione
1. Impostare la variabile d'ambiente `TELEGRAM_BOT_TOKEN` su Render
2. Caricare questi file:
   - `main.py`
   - `requirements.txt`

## Comandi Render
- Build Command: `pip install -r requirements.txt`
- Start Command: `python bot.py`
