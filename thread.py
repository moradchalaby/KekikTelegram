from threading import Thread
import time

def Zaman():
    while 1:
        print(time.now())
        time.sleep(1)

def Polling():
    bot.polling()


Thread(target=Zaman).start()
Thread(target=Polling).start()