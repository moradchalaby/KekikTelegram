from telebot import TeleBot

bot = TeleBot("834367279:AAG-h-6lJtj-LOixDp6UYgKIKQDg5wZOXXk")

@bot.message_handler(['start'])
def baslangic_mesaji(m):
    chat_type = m.chat.type
    if chat_type == "private":
        bot.send_message(m.chat.id, "Merhaba, kullanımı öğrenmek için /help komutunu gönderin.")


@bot.message_handler(['help'])
def yardim_mesaji(m):
    chat_type = m.chat.type
    if chat_type == "private":
        bot.send_message(m.chat.id, "Yardım mesajı")


ban_listesi = []
bizim_IDmiz = 1022602366

@bot.message_handler(['feedback'])
def geri_bildirim(m):
    chat_type = m.chat.type
    if chat_type == "private":
        user_id = m.from_user.id
        if str(user_id) not in ban_listesi:
            kullanici = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
            bot.send_message(bizim_IDmiz, f"{kullanici}\nID : `{m.from_user.id}` \nFeedBack : {' '.join(m.text.split()[1:])}", parse_mode="Markdown")
            bot.reply_to(m, "FeedBack gönderildi.")


@bot.message_handler(['answer'])
def cevapla(m):
    user_id = m.from_user.id
    if int(user_id) == bizim_IDmiz:
        gonderliecek_kisi = m.text.split()[1]
        gonderilecek_mesaj = " ".join(m.text.split()[2:])
        try:
            bot.send_message(gonderliecek_kisi, f"Cevap : {gonderilecek_mesaj}")
            bot.reply_to(m, "Mesaj gönderildi.")
        except:
            bot.reply_to(m, "Mesaj gönderilemedi.")


@bot.message_handler(['ban'])
def ban(m):
    user_id = m.from_user.id
    if int(user_id) == bizim_IDmiz:
        ban_listesi.append(m.text.split()[1])
        bot.reply_to(m, "Kullanıcı banlandı.")


@bot.message_handler(['unban'])
def unban(m):
    user_id = m.from_user.id
    if int(user_id) == bizim_IDmiz:
        ban_listesi.remove(m.text.split()[1])
        bot.reply_to(m, "Kullanıcı banı kaldırıldı.")
        

bot.polling()
