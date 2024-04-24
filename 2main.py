from googletrans import Translator
import telebot
from chatterbot import ChatBot

# إنشاء مترجم
translator = Translator()

# إنشاء بوت الدردشة
chatbot = ChatBot('7120326643:AAG1Hrcthb1ot9fZjY5ub5GiTP40djBIIyk')

# بقية الكود لبوت تليجرام
bot = telebot.TeleBot("YOUR_TOKEN")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # تحديد اللغة وترجمة النص
    translated_message = translator.translate(message.text, dest='en').text
    
    # الرد باستخدام الذكاء الاصطناعي
    response = chatbot.get_response(translated_message)
    
    # ترجمة الرد إلى لغة المستخدم
    translated_response = translator.translate(response, dest='ar').text
    
    # إرسال الرد
    bot.reply_to(message, translated_response)

bot.polling()
