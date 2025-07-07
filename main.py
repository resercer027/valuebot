import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = ""7896737431:AAE1uGhEdjqtuts3KoWeMRFPYJLoryYazz4""  # <-- Sostituisci con il tuo token e NON commitare su GitHub!

# =================================================================
# CODICE DEL BOT (NON MODIFICARE)
# =================================================================

# Configurazione logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f'👋 Ciao {user.first_name}! Bot attivo e funzionante.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'📩 Ricevuto: {update.message.text}')

def main() -> None:
    if not TOKEN or "IL_TUO_TOKEN" in TOKEN:
        logger.error("❌ ERRORE: Token non valido!")
        logger.info("Configura il token:")
        logger.info("1. Su Render: Imposta TELEGRAM_BOT_TOKEN in Environment")
        logger.info("2. Localmente: Sostituisci 'IL_TUO_TOKEN_REALE_QUI'")
        return

    try:
        updater = Updater(TOKEN)
        dispatcher = updater.dispatcher
        
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

        logger.info("✅ Bot avviato con successo")
        updater.start_polling()
        updater.idle()

    except Exception as e:
        logger.error(f"🔥 Errore critico: {e}")

if __name__ == '__main__':
    main()
