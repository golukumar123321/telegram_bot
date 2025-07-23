import telebot
from telebot import types

TOKEN = "7506442043:AAFNvZEZ7s4Znp_KMnisRY0QZOmBIxhVXqI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("🎥 Send Media")
    markup.add(btn)
    bot.send_message(message.chat.id, "Hello bhai! Neeche button dabao media ke liye:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def send_media(message):
    if message.text == "🎥 Send Media":
        try:
            # Photos bhejna
            photos = ["photo1.jpg", "photo2.jpg"]
            for photo in photos:
                with open(photo, "rb") as p:
                    bot.send_photo(message.chat.id, p, caption=f"Photo: {photo}")

            # Video bhejna
            videos = ["video1.mp4"]
            for video in videos:
                with open(video, "rb") as v:
                    bot.send_video(message.chat.id, v, caption=f"Video: {video}")

        except Exception as e:
            bot.send_message(message.chat.id, f"⚠️ File error: {e}")

        # Payment link
        payment_link = "https://rzp.io/rzp/XIhWggJ"
        bot.send_message(message.chat.id, f"Payment ke liye link: {payment_link}")

print("Bot chal raha hai...")
bot.polling()
