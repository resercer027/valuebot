import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# ==== ATTENZIONE: METODO SICURO PER IL TOKEN ====
# OPZIONE 1 (Consigliata per Render):
# TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  # Configuralo in Render > Environment

# OPZIONE 2 (Solo per test locali, NON commitare su GitHub):
TOKEN = "7896737431:AAE1uGhEdjqtuts3KoWeMRFPYJLoryYazz4"  # <-- Usa SOLO queste virgolette

# ================================================

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
    if not TOKEN or "7896737431" in TOKEN:  # Controllo generico per token di esempio
        logger.error("❌ ERRORE: Configura il token correttamente!")
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
