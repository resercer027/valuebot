
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, JobQueue
import asyncio

BOT_TOKEN = "INSERISCI_IL_TUO_TOKEN_QUI"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Messaggio fisso da inviare ogni 10 minuti
VALUE_BET = "💰 Ecco una value bet automatica!

📍 Partita: Juventus - Milan
🏆 Mercato: 1X2
💡 Puntata: 1 (Quota 3.10)
📈 Valore stimato: +8%"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot attivo! Riceverai automaticamente le value bet ogni 10 minuti.")

async def valuebet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(VALUE_BET)

async def scheduled_send(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=context.job.chat_id, text=VALUE_BET)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("valuebet", valuebet))

    async def start_bot():
        # Esegui ogni 10 minuti (600 secondi)
        app.job_queue.run_repeating(scheduled_send, interval=600, first=10, chat_id="INSERISCI_IL_TUO_CHAT_ID")
        await app.run_polling()

    asyncio.run(start_bot())

if __name__ == '__main__':
    main()
