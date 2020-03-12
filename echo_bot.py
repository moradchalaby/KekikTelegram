from telebot import TeleBot

token = "TOKENİNİZ"

bot = TeleBot(token=token)

@bot.message_handler(content_types=['text']) #Yazı yazılırsa...
def tekrar_et(m):
     alinan_mesaj = m.text #kullanıcının girdiği mesaj.
     bot.reply_to(m, alinan_mesaj) #Tekrar edeceğimiz kısım.


bot.polling() #Gelecek mesajları dinlemeye hazırım.
