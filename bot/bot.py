
from datetime import date
from requests.sessions import get_auth_from_url
import telebot
import config
import pytz
import api
import json

P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 
        'Hi There! Can I help You?\n'+
        'To gat help tipe /help'
    )
@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Developer Message', url='telegram.me/myexpy'))
    bot.send_message(
        message.chat.id, 
        '#1: To receive a list of available currencies press /exchange.\n'+
        '#2: Click on the currency You are interested in.\n' +
        '#3: Click Update to receive the current information regarding the request',
        reply_markup=keyboard
    )

@bot.message_handler(commands=['exchange'])
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('USD', callback_data='get-USD'))
    keyboard.add(telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'))
    keyboard.add(telebot.types.InlineKeyboardButton('RUR', callback_data='get-RUR'))
    keyboard.add(telebot.types.InlineKeyboardButton('BTC', callback_data='get-BTC'))
    bot.send_message(
        message.chat.id, 
        'Click on the currency of choice',
        reply_markup=keyboard
    )

def serialize(ex):
    result = '<b>' + ex['base_ccy'] + ' -> ' + ex['ccy'] + ':</b>\n\n' + 'Buy: ' + ex['buy']
    result += '\nSell: ' + ex['sale'] + '\n'
    return result

def get_aupdate_keyboard(ex):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton(
        'Update', callback_data=json.dumps(
         {
             't': 'u',
             'e': {
                 'b': ex['buy'],
                 's': ex['sale'],
                 'c': ex['ccy'],
             }
         }
         ).replace(' ', '')
        ),
        telebot.types.InlineKeyboardButton('Share', switch_inline_query=ex['ccy']))
    return keyboard

    
def send_exchange_result(message, code):
    bot.send_chat_action(message.chat.id, 'typing')
    ex = api.get_exchange(code)
    bot.send_message(message.chat.id, serialize(ex), reply_markup=get_aupdate_keyboard(ex), parse_mode='HTML')
    
def get_ex_callback(query):
    bot.answer_callback_query(query.id)
    send_exchange_result(query.message, query.data[4:])
    

@bot.callback_query_handler(func=lambda call: True)
def callback(query):
    data = query.data
    if data.startswith('get-'):
        get_ex_callback(query)

    
if __name__ == '__main__':
    bot.infinity_polling()