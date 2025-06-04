from telebot import TeleBot
from telebot.storage import StateMemoryStorage

API_TOKEN = "YOUR_TOKEN_HERE"
storage = StateMemoryStorage()
bot = TeleBot(API_TOKEN, state_storage=storage)