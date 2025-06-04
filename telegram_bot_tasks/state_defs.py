from telebot.handler_backends import StatesGroup, State

class MyStates(StatesGroup):
    name = State()
    age = State()