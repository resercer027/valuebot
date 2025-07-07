
from telegram.ext import Updater, CommandHandler
from auto_sender import run_combined_scrapers
import schedule
import time
import threading

TOKEN = "7896737431:AAE1uGhEdjqtuts3KoWeMRFPYJLoryYazz4"
CHAT_ID = None  # sarà salvato alla prima interazione

updater = Updater(TOKEN)
dp = updater.dispatcher

def start(update, context):
    global CHAT_ID
    CHAT_ID = update.effective_chat.id
    update.message.reply_text("✅ Bot attivo! Ti invierò scommesse value ogni 10 minuti.")

def valuebet(update, context):
    bets = run_combined_scrapers()
    if bets:
        for bet in bets:
            update.message.reply_text(bet)
    else:
        update.message.reply_text("⏳ Nessuna value bet valida trovata ora.")

def send_auto_value_bets():
    if CHAT_ID:
        bets = run_combined_scrapers()
        bot = updater.bot
        if bets:
            for bet in bets:
                bot.send_message(chat_id=CHAT_ID, text=bet)
        else:
            bot.send_message(chat_id=CHAT_ID, text="⏳ Nessuna value bet automatica trovata ora.")

def schedule_loop():
    schedule.every(10).minutes.do(send_auto_value_bets)
    while True:
        schedule.run_pending()
        time.sleep(1)

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("valuebet", valuebet))

threading.Thread(target=schedule_loop, daemon=True).start()
updater.start_polling()
updater.idle()
