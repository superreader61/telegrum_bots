from config import bot
from state_defs import MyStates

@bot.message_handler(state=MyStates.name)
def get_name(message):
    with bot.retrieve_data(message.from_user.id) as data:
        data["name"] = message.text
    bot.set_state(message.from_user.id, MyStates.age, message.chat.id)
    bot.send_message(message.chat.id, "Сколько тебе лет?")