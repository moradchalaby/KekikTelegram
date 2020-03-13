from telebot import TeleBot
token = ""

bot = TeleBot(token)

@bot.message_handler(content_types=['photo'])               #Fotoğraf gönderilirse...
def fotograf_tekrari(m):    
     chat_id = m.chat.id                                    #sohbetin ID numarası    
     file_id = m.photo[-1].file_id                          #fotoğrafa ait file_id değeri    
     caption = m.caption                                    #fotoğraf altındaki yazı    
     bot.send_photo(chat_id, file_id, caption)              #Fotoğraf gönder


bot.polling() #Gelecek mesajları dinlemeye hazır...
