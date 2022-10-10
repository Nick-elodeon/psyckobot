import config
from datetime import datetime
import telebot
from telebot import types
import random
bot = telebot.TeleBot(config.TOKEN)

love = ["Если хочешь встретить любовь всей своей жизни — посмотри в зеркало.",
        "Такой вот парадокс: мы совершаем подвиги для тех, кому до нас уже нет никакого дела, а любят нас те, кому мы нужны и без всяких подвигов...",
        "Нет ничего хуже, чем любить кого-то, кто никогда не перестанет тебя разочаровывать."
        ]
motivation = ["Чем усерднее вы работаете, тем более удачливым вы становитесь",
              "Нет волшебства, чтобы мечта стала реальностью. Это требует решимости и упорного труда", 
              "Богатство лишило многих людей возможности постигать мудрость"
              ]
career = ["Ты не можешь дефилировать до конца своей жизни, поэтому очень важно то, как ты разнообразишь свою карьеру.",
          "Карьера — чудесная вещь, но она никого не может согреть в холодную ночь.",
          "Это, возможно, не то будущее, которое я хотела выбрать. Я думаю, что можно добиться успеха, как в браке, так и в карьере, даже если я этого не достигла. Но и это — не плохое будущее. И я не боюсь его."
          ]

def start_markup():
    markup = telebot.types.InlineKeyboardMarkup(row_width = True)
    link_keyboard1 = types.InlineKeyboardButton(text="1-й канал", url = "https://t.me/psyloging")
    link_keyboard2 = types.InlineKeyboardButton(text="2-й канал", url = "https://t.me/abobusmusic")
    check_keyboard = types.InlineKeyboardButton(text ="Проверить подписки✅", callback_data= "check")

    markup.add(link_keyboard1,link_keyboard2,check_keyboard)
    return markup

def options_markup():
    markup2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Любовь 💋")
    item2 = types.KeyboardButton("Мотивация 💪🏼")
    item3 = types.KeyboardButton("Карьера 📈")

    markup2.add(item1,item2,item3)
    return markup2

def back_markup():
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Назад 🔙")

    markup3.add(item1)
    return markup3

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Привет, <b> {0.first_name}!</b>\n\nЯ, {1.first_name}, бот, который был создан, чтобы делиться с тобой цитатами на разные сферы.\n<i>Чтобы пользоваться ботом, подпишись на следующие каналы:</i>".format(message.from_user, bot.get_me()), parse_mode='HTML', reply_markup=start_markup())

def check(call):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id="-1001549436852", user_id=call.message.chat.id).status:
            check2(call)
            break

    else:
        bot.send_message(call.message.chat.id,"Подпишитесь на каналы!", reply_markup=start_markup())

def check2(call):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id="-1001549345531", user_id=call.message.chat.id).status:
            bot.send_message(call.message.chat.id, "Спасибо за подписку!")
            hi(call)
            break

    else:
        bot.send_message(call.message.chat.id,"Подпишитесь на каналы!", reply_markup=start_markup())

def hi(call):
    bot.send_message (call.message.chat.id,"Пожалуйста, выбери сферу, которая тебя интересует", reply_markup = options_markup())

def sample_responses(message):
    user_message = str(message).lower()

    if user_message in ("Привет", "Привет!", "Прив"):
        return "Привет!"
    
    if user_message in ("Кто ты?", "Что ты за бот?"):
        return ("Привет, я Психология бот")
    
    if user_message in ("Время?", "Время"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

@bot.message_handler(content_types = ['text'])
def callback_call(message):
    if message.text == "Любовь 💋":
        msg = random.choice(love)
        bot.send_message(message.chat.id, msg)
        bot.send_message(message.chat.id, "Хочешь прочитать что-то ещё? Выбери сферу и я пришлю тебе цитату на выбранную тобой тему!")
    elif message.text == "Мотивация 💪🏼":
        msg1 = random.choice(motivation)
        bot.send_message(message.chat.id, msg1)
        bot.send_message(message.chat.id, "Хочешь услышать еще что-то? Выбери сферу и я пришлю тебе цитату на выбранную тобой тему!")
    elif message.text == "Карьера 📈":
        msg2 = random.choice(career)
        bot.send_message(message.chat.id, msg2)
        bot.send_message(message.chat.id, "Хочешь услышать еще что-то? Выбери сферу и я пришлю тебе цитату на выбранную тобой тему!")
    else:
        bot.send_message (message.chat.id,"Я не знаю что тебе ответить на это🥲\n Выбери интересующую тебя сферу и я вышлю тебе цитату на эту тему!", reply_markup = options_markup())

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.data == 'check':
        check(call)
    else:
        callback_call()


bot.polling(none_stop = True, interval= 0)
