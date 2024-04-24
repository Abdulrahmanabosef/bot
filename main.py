import telebot
from telebot import types

# استبدل "TOKEN" بمفتاح API الذي حصلت عليه من BotFather
bot = telebot.TeleBot("7120326643:AAG1Hrcthb1ot9fZjY5ub5GiTP40djBIIyk")

# استجابة للرسائل الواردة
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # إعداد لوحة المفاتيح
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('مرحبا')
    itembtn2 = types.KeyboardButton('مساعدة')
    itembtn3 = types.KeyboardButton('الترجمة')
    itembtn4 = types.KeyboardButton('الألعاب')
    keyboard.add(itembtn1, itembtn2, itembtn3, itembtn4)

    # استجابة للرسالة
    if message.text == 'مرحبا':
        bot.reply_to(message, 'مرحبًا بك!', reply_markup=keyboard)
    elif message.text == 'مساعدة':
        bot.reply_to(message, 'كيف يمكنني مساعدتك؟', reply_markup=keyboard)
    elif message.text == 'الترجمة':
        bot.reply_to(message, 'أدخل النص الذي تريد ترجمته:', reply_markup=keyboard)
        bot.register_next_step_handler(message, translate)
    elif message.text == 'الألعاب':
        # إظهار قائمة الألعاب
        games_markup = types.InlineKeyboardMarkup()
        game1_button = types.InlineKeyboardButton(text="لعبة 1", callback_data="game1")
        game2_button = types.InlineKeyboardButton(text="لعبة 2", callback_data="game2")
        games_markup.add(game1_button, game2_button)
        bot.reply_to(message, "اختر لعبة:", reply_markup=games_markup)

# دالة للترجمة
def translate(message):
    # هنا يمكنك استخدام مكتبة الترجمة الخاصة بك لتنفيذ العملية
    translated_text = "النص المترجم"
    bot.reply_to(message, translated_text)

# استجابة للاستعلامات المتقدمة مثل الضغط على زر اللعبة
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "game1":
        bot.send_message(call.message.chat.id, "لعبة 1: ابدأ اللعبة هنا...")
    elif call.data == "game2":
        bot.send_message(call.message.chat.id, "لعبة 2: ابدأ اللعبة هنا...")

# بدء البوت
bot.polling()
