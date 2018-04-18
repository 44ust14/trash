# import sys
import time
# import threading
# import random
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
# from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
# from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
message_with_inline_keyboard = None

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
    if content_type != 'text':
        return
    command = msg['text'].lower()
# bot.sendMessage(chat_id, 'This is noooooot finnal noot wooorking keyboard', reply_markup=ReplyKeyboardMarkup(
# keyboard=[
# [KeyboardButton(text="🗓️ Current Weather 🗓️"), KeyboardButton(text="📅 Weekly Weather 📅"),
# KeyboardButton(text="🔧 Settings 🔧")]
# ]
# , resize_keyboard=True))
    if command == '/start':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🗓️ current weather 🗓️'), KeyboardButton(text='📅 weekly weather 📅',)],
        [KeyboardButton(text='🔧 settings 🔧')],
        ])
        bot.sendMessage(chat_id, '*Welcome!*', reply_markup=markup, parse_mode='Markdown')
    elif command == '🗓️ current weather 🗓️':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='📌 last location 📌')],[ KeyboardButton(text='➕ new Location ➕')],
        [KeyboardButton(text='🗺️ my location 🗺️', request_location=True)],[KeyboardButton(text='🔙 back 🔙')]
        ])
        bot.sendMessage(chat_id, '*Choose location*', reply_markup=markup, parse_mode='Markdown')
    elif command == '📅 weekly weather 📅':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='📌 last location 📌')],[ KeyboardButton(text='➕ new Location ➕')],
        [KeyboardButton(text='🗺️ my location 🗺️', request_location=True)],[KeyboardButton(text='🔙 back 🔙')]
        ])
        bot.sendMessage(chat_id, '*Choose location*', reply_markup=markup, parse_mode='Markdown')
    elif command == '🔧 settings 🔧':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🌐 languages 🌐'), KeyboardButton(text='units')],
        [KeyboardButton(text='alerts'), KeyboardButton(text='🔙 back 🔙')]
        ])
        bot.sendMessage(chat_id, '*Set up your bot*', reply_markup=markup, parse_mode='Markdown')
    elif command == '🔙 back 🔙':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🗓️ current weather 🗓️'), KeyboardButton(text='📅 weekly weather 📅',)],
        [KeyboardButton(text='🔧 settings 🔧')],
        ])
        bot.sendMessage(chat_id, '*you returned back*', reply_markup=markup, parse_mode='Markdown')
    elif command == 'units':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='celsium(°C)'), KeyboardButton(text='fahrenheit(°F)', )],
        [KeyboardButton(text='❌ cancel ❌')],
        ])
        bot.sendMessage(chat_id, '*Choose Celsium or Fahrenheit*', reply_markup=markup, parse_mode='Markdown')
    elif command == '❌ cancel ❌':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🌐 languages 🌐'), KeyboardButton(text='units')],
        [KeyboardButton(text='alerts'), KeyboardButton(text='🔙 back 🔙')]
        ])
        bot.sendMessage(chat_id, '*Set up your bot*', reply_markup=markup, parse_mode='Markdown')
    if command == 'celsium(°c)':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🗓️ current weather 🗓️'), KeyboardButton(text='📅 weekly weather 📅',)],
        [KeyboardButton(text='🔧 settings 🔧')],
        ])
        bot.sendMessage(chat_id, '*Units now are metric(celsium)*', reply_markup=markup, parse_mode='Markdown')
    if command == 'fahrenheit(°f)':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🗓️ current weather 🗓️'), KeyboardButton(text='📅 weekly weather 📅',)],
        [KeyboardButton(text='🔧 settings 🔧')],
        ])
        bot.sendMessage(chat_id, '*Units now are imperial(fahrenheit)*', reply_markup=markup, parse_mode='Markdown')
    if command == '🌐 languages 🌐':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿 english 🏴󠁧󠁢󠁥󠁮󠁧󠁿'), KeyboardButton(text='🇩🇪 deutsch 🇩🇪',)],
        [KeyboardButton(text='🇺🇦 українська 🇺🇦'), KeyboardButton(text='🇷🇺 русский 🇷🇺',)],
        ])
        bot.sendMessage(chat_id, '*Units now are imperial(fahrenheit)*', reply_markup=markup, parse_mode='Markdown')
    if command == '🏴󠁧󠁢󠁥󠁮󠁧󠁿 english 🏴':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🗓️ current weather 🗓️'), KeyboardButton(text='📅 weekly weather 📅', )],
        [KeyboardButton(text='🔧 settings 🔧')],
        ])
        bot.sendMessage(chat_id, '*Your language changed to English*', reply_markup=markup, parse_mode='Markdown')

        #ukrainian section

    if command == '🇺🇦 українська 🇺🇦':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🗓️ поточна погода 🗓️'), KeyboardButton(text='📅 тижнева погода 📅', )],
        [KeyboardButton(text='🔧 налаштування 🔧')],
        ])
        bot.sendMessage(chat_id, '*Ваша мова була змінена на Українську*', reply_markup=markup, parse_mode='Markdown')
    elif command == '🗓️ поточна погода 🗓️':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='📌 останнє місце 📌')],[ KeyboardButton(text='➕ нове місце ➕')],
        [KeyboardButton(text='🗺️ моє місце 🗺️', request_location=True)],[KeyboardButton(text='🔙 назад 🔙')]
        ])
        bot.sendMessage(chat_id, '*Виберіть місцезнаходження*', reply_markup=markup, parse_mode='Markdown')
    elif command == '📅 тижнева погода 📅':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='📌 останнє місце 📌')],[ KeyboardButton(text='➕ нове місце ➕')],
        [KeyboardButton(text='🗺️ моє місце 🗺️', request_location=True)],[KeyboardButton(text='🔙 назад 🔙')]
        ])
        bot.sendMessage(chat_id, '*Виберіть місцезнаходження*', reply_markup=markup, parse_mode='Markdown')
    elif command == '🔧 налаштування 🔧':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🌐 мови 🌐'), KeyboardButton(text='одиниці')],
        [KeyboardButton(text='сповіщення'), KeyboardButton(text='🔙 назад 🔙')]
        ])
        bot.sendMessage(chat_id, '*Налаштуйте свого бота*', reply_markup=markup, parse_mode='Markdown')
    elif command == '🔙 назад 🔙':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🗓️ поточна погода 🗓️'), KeyboardButton(text='📅 тижнева погода 📅',)],
        [KeyboardButton(text='🔧 налаштування 🔧')],
        ])
        bot.sendMessage(chat_id, '*Ви повернулися назад*', reply_markup=markup, parse_mode='Markdown')
    elif command == 'одиниці':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='цельсії(°C)'), KeyboardButton(text='фаренгейти(°F)', )],
        [KeyboardButton(text='❌ відмінити ❌')],
        ])
        bot.sendMessage(chat_id, '*Виберіть одиниці виміру*', reply_markup=markup, parse_mode='Markdown')
    elif command == '❌ відмінити ❌':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🌐 мови 🌐'), KeyboardButton(text='одиниці')],
        [KeyboardButton(text='сповіщення'), KeyboardButton(text='🔙 назад 🔙')]
        ])
        bot.sendMessage(chat_id, '*налаштуйте свого бота*', reply_markup=markup, parse_mode='Markdown')
    if command == 'цельсії(°c)':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🗓️ поточна погода 🗓️'), KeyboardButton(text='📅 тижнева погода 📅',)],
        [KeyboardButton(text='🔧 налаштування 🔧')],
        ])
        bot.sendMessage(chat_id, '*Одиниці виміру були змінені на цельсії*', reply_markup=markup, parse_mode='Markdown')
    if command == 'фаренгейти(°f)':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🗓️ поточна погода 🗓️'), KeyboardButton(text='📅 тижнева погода 📅',)],
        [KeyboardButton(text='🔧 налаштування 🔧')],
        ])
        bot.sendMessage(chat_id, '*Одиниці виміру були змінені на фаренгейти*', reply_markup=markup, parse_mode='Markdown')
    if command == '🌐 мови 🌐':
        markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿 english 🏴󠁧󠁢󠁥󠁮󠁧󠁿'), KeyboardButton(text='🇩🇪 deutsch 🇩🇪',)],
        [KeyboardButton(text='🇺🇦 українська 🇺🇦'), KeyboardButton(text='🇷🇺 русский 🇷🇺',)],
        ])
        bot.sendMessage(chat_id, '*Виберіть мову*', reply_markup=markup,
parse_mode='Markdown')
TOKEN = "597420522:AAHdU-Cy7B6U_wQ5UQBjLp1TsmlSeyr2aY8"
bot = telepot.Bot(TOKEN)

answerer = telepot.helper.Answerer(bot)
MessageLoop(bot, {'chat': on_chat_message}).run_as_thread()

print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)


