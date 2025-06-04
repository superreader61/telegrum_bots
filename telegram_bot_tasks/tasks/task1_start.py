from config import bot
from state_defs import MyStates

@bot.message_handler(commands=["start"])
def start(message):
    bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
    bot.send_message(message.chat.id, "Привет! Как тебя зовут?")