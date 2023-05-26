import telebot, random
from jokes import jokes
from telebot import types
from memes import memes
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    privet = f'Приветствую, мой дорогой друг <u>{message.from_user.first_name}</u>. Да начнётся <b>великое путешествие</b> ' \
                  f'по безкрайним просторам мемов и отборных анекдотов'
    bot.send_message(message.chat.id, privet, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    random_joke = types.KeyboardButton('Получить случайный анекдот')
    random_meme = types.KeyboardButton('Получить случайный мем')
    markup.add(random_joke, random_meme)
    bot.send_message(message.chat.id, 'Выберете категорию', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_memes(message):
    if message.text == 'Получить случайный анекдот':
        bot.send_message(message.chat.id, random.choice(jokes))
    elif message.text == 'Получить случайный мем':
        bot.send_photo(message.chat.id, random.choice(memes))
    else:
        bot.send_message(message.chat.id,'Нажмите любую кнопку!')




bot.polling(none_stop=True)