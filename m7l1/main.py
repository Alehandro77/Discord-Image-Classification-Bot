import telebot
from modol import get_class
# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7560127020:AAGXtHllWmykj1TsLaSEsaqiv77gP8phc44")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /emodji или /coin  ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(content_types=['photo'])
def photo(message):
    #Полсучаем файл и сохранеем
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    #Загружаем файл
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    # Анализ изображения
    resalt = get_class(model_path='keras_model.h5', lables_path='labels.txt', image_path=file_name)
    bot.send_message(message.chat.id, resalt)

# Запускаем бота
bot.polling()