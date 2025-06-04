from config import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

@bot.message_handler(commands=["buttons"])
def send_keyboard(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Нажми меня", callback_data="clicked"))
    bot.send_message(message.chat.id, "Вот кнопка:", reply_markup=markup)