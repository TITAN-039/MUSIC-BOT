import telebot

bot = telebot.TeleBot("5641817385:AAGZ_LQR4lh-6Qio-vzCMpESseD7Vidaih4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Send me a music file and I'll play it for you.")

@bot.message_handler(content_types=['audio'])
def play_music(message):
    file_id = message.audio.file_id
    file_info = bot.get_file(file_id)
    file = bot.download_file(file_info.file_path)

    with open("music.mp3", 'wb') as f:
        f.write(file)

    # play the music using any library you like (e.g. pygame)

bot.polling()
