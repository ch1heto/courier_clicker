import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
import db

TOKEN = 'kto posmotrit, tot loh'  # 🔒 замени на свой
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    db.create_user(user_id)

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = WebAppInfo(url="https://valba312.github.io/courier/")  # GitHub Pages
    markup.add(KeyboardButton("🎮 Открыть игру", web_app=web_app))

    bot.send_message(message.chat.id, "Добро пожаловать в Курьер-Кликер! Нажми кнопку ниже, чтобы начать:", reply_markup=markup)

@bot.message_handler(commands=['check'])
def check_user(message):
    user_id = message.from_user.id
    user = db.get_user(user_id)

    if user:
        money, speed, assistants, cost = user[1], user[2], user[3], user[4]
        bot.send_message(
            message.chat.id,
            f"🔍 Прогресс:\n💰 Деньги: {money}\n🚀 Скорость: {speed}\n🧍 Помощники: {assistants}\n💸 Следующий помощник: {cost}"
        )
    else:
        bot.send_message(message.chat.id, "⚠️ Вы не зарегистрированы. Введите /start.")

if __name__ == "__main__":
    db.init_db()
    bot.infinity_polling()
