from threading import Thread
import time

def zaman():
    while 1:
        print(time.now())
        time.sleep(1)

def polling():
    bot.polling()


Thread(target=zaman).start()
Thread(target=polling).start()