from telebot import TeleBot #Modülümüzü ekliyoruz

bot = TeleBot("")           #Botumuzu oluşturuyoruz

@bot.message_handler(['start']) #Start komutu girilirse...
def baslangic_mesaji(m):
    chat_type = m.chat.type                                                                         #Sohbet türü
    if chat_type == "private":                                                                      #Eğer özel sohbet ise
        bot.send_message(m.chat.id, "Merhaba, kullanımı öğrenmek için /help komutunu gönderin.")    #Start mesajını gönder.


@bot.message_handler(['help']) #Help komutu girilirse...
def yardim_mesaji(m):
    chat_type = m.chat.type                                                                     #Sohbet türü
    if chat_type == "private":                                                                  #Eğer özel sohbet is
        bot.send_message(m.chat.id, "Yardım mesajı")                                            #Help mesajını gönder.


ban_listesi = []                #Banlanacakların ID'si
bizim_IDmiz = 1234567890        #Bizim ID'miz

@bot.message_handler(['feedback']) #Feedback komutu girilirse...
def geri_bildirim(m):
    chat_type = m.chat.type                                                                     #Sohbet Türü
    if chat_type == "private":                                                                  #Eğer özel sohbet ise
        user_id = m.from_user.id                                                                #Kullanıcı ID'si
        if str(user_id) not in ban_listesi:                                                     #Kullanıcı banlı değilse
            kullanici = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"            #Kullanıcı mention
            bot.send_message(bizim_IDmiz, f"{kullanici}\nID : `{m.from_user.id}` \nFeedBack : {' '.join(m.text.split()[1:])}", parse_mode="Markdown")
            bot.reply_to(m, "FeedBack gönderildi.")                                             #Dönüt


@bot.message_handler(['answer']) #Answer komutu girilirse...
def cevapla(m):
    user_id = m.from_user.id                                                                    #Kullanıcı ID'si
    if int(user_id) == bizim_IDmiz:                                                             #Eğer komutu biz girdiysek
        gonderliecek_kisi = m.text.split()[1]                                                   #Komuttan sonraki kelimeyi  ID olarak al
        gonderilecek_mesaj = " ".join(m.text.split()[2:])                                       #Komuttan sonraki 2. kelimeden sonrası
        try:                                                                                    #ID'yi yanlış girmediysek
            bot.send_message(gonderliecek_kisi, f"Cevap : {gonderilecek_mesaj}")                #Cevap mesajını gönder
            bot.reply_to(m, "Mesaj gönderildi.")                                                #Dönüt
        except:                                                                                 #ID yanlış ise
            bot.reply_to(m, "Mesaj gönderilemedi.")                                             #Dönüt


@bot.message_handler(['ban']) #Ban komutu girilirse...
def ban(m):
    user_id = m.from_user.id                                                                    #Kullanıcı ID'si
    if int(user_id) == bizim_IDmiz:                                                             #Eğer komutu biz girdiysek
        ban_listesi.append(m.text.split()[1])                                                   #ID'yi ban listesine ekle
        bot.reply_to(m, "Kullanıcı banlandı.")                                                  #Dönüt


@bot.message_handler(['unban']) #Unban komutu girilirse
def unban(m):
    user_id = m.from_user.id                                                                    #Kullanıcı ID'si
    if int(user_id) == bizim_IDmiz:                                                             #Eğer komutu biz girdiysek
        ban_listesi.remove(m.text.split()[1])                                                   #ID'yi ban listesinden kaldır
        bot.reply_to(m, "Kullanıcı banı kaldırıldı.")                                           #Dönüt
        

bot.polling() #Çalıştır...
