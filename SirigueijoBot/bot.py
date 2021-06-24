import telegram, logging, config, schedule, random
from telegram.ext import Updater
from datetime import time, date, datetime
from time import sleep
from threading import Thread

bot = telegram.Bot(token=config.bot_token)
chat_id = config.chat_id
updater = Updater(token=config.bot_token, use_context=True)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(60)

def sendKrabs():
    if random.randint(1,5000) == 1:
        bot.sendMessage(chat_id=chat_id, text="Uh oh, os amigos furries de Mr. Tichamon me hackearam!! ;)")
        bot.sendVideo(chat_id=chat_id, video="https://files.catbox.moe/8wol39.mp4")
    else:
        now = datetime.now().strftime("%A")

        if now == "Monday":
            vfile = "https://files.catbox.moe/wjqwun.mp4"
        elif now == "Tuesday":
            vfile = "https://files.catbox.moe/gkiexm.mp4"
        elif now == "Wednesday":
            if random.randint(1,2) == 1: vfile = "https://files.catbox.moe/bzj1sb.mp4"
            else: vfile = "https://files.catbox.moe/bz5rka.mp4"
        elif now == "Thursday":
            vfile = "https://files.catbox.moe/jfagkz.mp4"
        elif now == "Friday":
            vfile = "https://files.catbox.moe/wdiopc.mp4"
        elif now == "Saturday":
            vfile = "https://files.catbox.moe/tnbl3v.mp4"
        elif now == "Sunday":
            vfile = "https://files.catbox.moe/81axko.mp4"
        bot.sendVideo(chat_id=chat_id, video=vfile)

def sendKrabs2():
    # ze do picadinho
    bot.sendVideo(chat_id=chat_id, video="https://files.catbox.moe/husmbs.mp4")

def sextaFeira():
    bot.sendVideo(chat_id=chat_id, video="https://files.catbox.moe/dvu5j6.mp4")

def goodMonday():
    bot.sendVideo(chat_id=chat_id, video="https://files.catbox.moe/kwu2k6.mp4")
    

if __name__ == "__main__":
    schedule.every().day.at("07:00").do(sendKrabs)
    schedule.every().tuesday.at("19:00").do(sendKrabs2)
    schedule.every().friday.at("17:30").do(sextaFeira)
    schedule.every().monday.at("12:00").do(goodMonday)
    
    Thread(target=schedule_checker).start() 

updater.start_polling()
