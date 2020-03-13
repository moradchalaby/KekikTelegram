from telebot import TeleBot
from time import sleep
token = ""

bot = TeleBot(token)
kayit = {}  #kayit yeri

@bot.message_handler(content_types=['photo'])                                 #Fotoğraf gönderilirse...
def fotograf_geldi(m):    
    sohbet_turu = m.chat.type                                                 #Sohbetin türü
    if sohbet_turu == "private":                                              #Eğer özel sohbet ise
         kullanici_id = m.from_user.id                                        #Kullanıcı İD
         if str(kullanici_id) not in kayit.keys():                            #Eğer kullanıcının kaydı yoksa...
              kayit[str(kullanici_id)] = []                                   #Bir kayıt oluştur
         file_id = m.photo[-1].file_id                                        #Fotoğraf kimliği
         fotografin_yazisi = m.caption                                        #Fotoğraf yazısı
         kayit[str(kullanici_id)].append({"file_id" : file_id,                #Kaydet.
                                          "capt": fotografin_yazisi})        
         bot.reply_to(m, "Fotoğraf kaydedildi.")                              #Kaydedildiğini haber ver
            
@bot.message_handler(['fotograflarim'])                                       #Kullanıcı fotoğraflarını isterse
def fotograflari_gonder(m):
    sohbet_turu = m.chat.type                                                 #Sohbetin türü
    if sohbet_turu == "private":                                              #Eğer özel sohbet ise
         kullanici_id = m.from_user.id                                        #Kullanıcı İD
         if str(kullanici_id) not in kayit.keys():                            #Eğer kullanıcının kaydı yoksa...
              kayit[str(kullanici_id)] = []                                   #Bir kayıt oluştur
              bot.reply_to(m, "Kayıtlı bir fotoğraf bulunamadı.")             #Kaydı olmadığı için fotoğraf bulamadığını söyle
              return                                                          #Fonksiyonu bitir
         sayi = 0                                                             #Sayaç
         for i in kayit[str(kullanici_id)]:                                   #Listeyi döndür
              bot.send_photo(kullanici_id, i.get("file_id"), i.get("capt"))   #Fotoğrafları tek tek gönder
              sayi += 1                                                       #Sayaç ile her fotoğrafı say
              sleep(1)                                                        #Spam yapmayalım :)
         bot.send_message(kullanici_id, f"Toplam {sayi} tane fotoğraf gönderildi.") #Kaç fotoğraf olduğunu söyle
            
bot.polling() #Dinlemede...
