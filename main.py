import telebot
from telebot import types
import pyttsx3

en_w_voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
en_m_voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
ru_w_voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'

bot = telebot.TeleBot("5700611925:AAGdtwRm0E8crpFX7QW-g1k-rcjc6Wb1D5E")


@bot.message_handler(commands=['start'])
def start(message):
    # Buttons under the message
    markup_inline = types.InlineKeyboardMarkup()
    voice_en_w = types.InlineKeyboardButton(text='Woman, English', callback_data='w_en')
    voice_ru_w = types.InlineKeyboardButton(text='Woman, Russian', callback_data='w_ru')
    voice_en_m = types.InlineKeyboardButton(text='Man, English', callback_data='m_en')
    markup_inline.add(voice_en_w, voice_ru_w, voice_en_m)
    bot.send_message(message.chat.id, 'Choose language and type:', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data)
def user_answer(call):
    if call.data == 'w_en':
        msg = bot.send_message(call.message.chat.id, 'You chose: Woman, English. Now enter the text: ')
        bot.register_next_step_handler(msg, result_w_en)
    if call.data == 'w_ru':
        msg = bot.send_message(call.message.chat.id, 'You chose: Woman, Russian. Now enter the text: ')
        bot.register_next_step_handler(msg, result_w_ru)
    if call.data == 'm_en':
        msg = bot.send_message(call.message.chat.id, 'You chose: Man, English. Now enter the text: ')
        bot.register_next_step_handler(msg, result_m_en)


def result_w_en(message):
    engine = pyttsx3.init()
    engine.setProperty('voice', en_w_voice)
    engine.setProperty('rate', 125)
    engine.save_to_file(message.text, '1.mp3')
    engine.runAndWait()

    with open('1.mp3', 'rb') as main:
        bot.send_voice(message.chat.id, main)



def result_w_ru(message):
    engine = pyttsx3.init()
    engine.setProperty('voice', ru_w_voice)
    engine.save_to_file(message.text, '1.mp3')
    engine.runAndWait()

    with open('1.mp3', 'rb') as main:
        bot.send_voice(message.chat.id, main)



def result_m_en(message):
    engine = pyttsx3.init()
    engine.setProperty('voice', en_m_voice)
    engine.setProperty('rate', 125)
    engine.save_to_file(message.text, '1.mp3')
    engine.runAndWait()

    with open('1.mp3', 'rb') as main:
        bot.send_voice(message.chat.id, main)



bot.polling(non_stop=True)
