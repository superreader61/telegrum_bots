from config import bot
from state_defs import MyStates

@bot.message_handler(state=MyStates.age)
def get_age(message):
    with bot.retrieve_data(message.from_user.id) as data:
        data["age"] = message.text
        bot.send_message(
            message.chat.id,
            f"Тебя зовут {data['name']}, тебе {data['age']} лет."
        )
    bot.delete_state(message.from_user.id)