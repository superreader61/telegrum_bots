from config import bot

@bot.callback_query_handler(func=lambda call: call.data == "clicked")
def handle_callback(call):
    bot.answer_callback_query(call.id, "Ты нажал кнопку!", show_alert=True)