from config import bot
from telebot.custom_filters import StateFilter

# Импорт задач
import tasks.task1_start
import tasks.task2_get_name
import tasks.task3_get_age
import tasks.task4_keyboard
import tasks.task5_callback

bot.add_custom_filter(StateFilter(bot))

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()