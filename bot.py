import config
from datetime import datetime
import telebot
from telebot import types
import random
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

bot = telebot.TeleBot(config.TOKEN)

love = ["Если хочешь встретить любовь всей своей жизни — посмотри в зеркало.",
        "Такой вот парадокс: мы совершаем подвиги для тех, кому до нас уже нет никакого дела, а любят нас те, кому мы нужны и без всяких подвигов...",
        "Нет ничего хуже, чем любить кого-то, кто никогда не перестанет тебя разочаровывать.",
        "Любите друг друга, но не превращайте любовь в цепи. Пусть лучше она будет волнующим морем между берегами ваших душ.",
        "Я люблю тебя. Я тебя люблю. Я мысленно посылаю эти слова из своих пальцев в его, вверх по руке прямо в сердце. Услышь меня. Я тебя люблю.",
        "Без любви жить легче. Но без неё нет смысла."
        ]
motivation = ["Чем усерднее вы работаете, тем более удачливым вы становитесь",
              "Нет волшебства, чтобы мечта стала реальностью. Это требует решимости и упорного труда", 
              "Богатство лишило многих людей возможности постигать мудрость",
              "Успех – не ключ к счастью. Счастье – это ключ к успеху. Если вы любите то, что вы делаете, вы будете иметь успех.",
              "Если вы работаете над поставленными целями, то эти цели будут работать на вас",
              "Каждое утро начинай с чтения списка самых богатых людей. Если тебя там нет – берись за работу.",
              "Тот, кто ищет миллионы, весьма редко их находит, но тот, кто их не ищет, не находит никогда.",
              "У всякого человека в отдельности и у всех вместе есть, можно сказать, известная цель, стремясь к которой они одно избирают, другого избегают.",
              "Для большинства из нас опасность состоит не в том, что великая цель кажется недостижимой и мы ее упускаем, а в том, что достигаемой оказывается цель слишком мелкая.",
              "Будь безупречным. Я говорил тебе это уже двадцать раз. Быть безупречным — означает раз и навсегда выяснить для себя, чего ты хочешь в жизни, и тем самым поддержать свою решимость достигнуть этого. А потом делать все от тебя зависящее и даже больше для того, чтобы воплотить в жизнь свое стремление. Если ты не решился ни на что, ты просто-напросто в суматохе играешь с жизнью в рулетку.",
              "Между событием и реакцией есть промежуток, который называется <b>СВОБОДА ВЫБОРА.</b>\nЭтот промежуток и создает жизнь человека."
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
    markup2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2, one_time_keyboard=True)
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


@bot.message_handler(func = lambda message: message.text == 'Привет!')
@bot.message_handler(func = lambda message: message.text == 'Привет')
@bot.message_handler(func = lambda message: message.text == 'привет')
def privet(message):
    bot.reply_to(message, "Привет, <b>{0.first_name}!</b> Как твои дела?".format(message.from_user, bot.get_me()), parse_mode = 'HTML')

@bot.message_handler(func = lambda message: message.text == 'Хорошо')
@bot.message_handler(func = lambda message: message.text == 'хорошо')
@bot.message_handler(func = lambda message: message.text == 'Хорошо!')
@bot.message_handler(func = lambda message: message.text == 'хорошо!')
def privet(message):
    bot.reply_to(message, "Мои тоже! Ты уже подписался на все каналы?.".format(message.from_user, bot.get_me()), parse_mode = 'HTML', reply_markup = start_markup())

@bot.message_handler(func = lambda message: message.text == 'кто ты')
@bot.message_handler(func = lambda message: message.text == 'Кто ты')
@bot.message_handler(func = lambda message: message.text == 'Кто ты?')
@bot.message_handler(func = lambda message: message.text == 'кто ты?')
def privet(message):
    bot.reply_to(message, "{0.first_name}, я бот, который будет высылать тебе цитаты на интересующую тебя сферу.\nНадеюсь, мне удастся тебя подбодрить ими".format(message.from_user, bot.get_me()), parse_mode = 'HTML')

@bot.message_handler(commands=["time"])
def time(message):
    now = datetime.today()
    date = now.strftime("%d-%b-%Y")
    time = now.strftime("%H:%M:%S")
    bot.send_message(message.chat.id, "Сегодня, за окном " + date + " и время сейчас " + time)

@bot.message_handler(content_types = ['text'])
def callback_call(message):

    if message.text == "Любовь 💋":
        msg = random.choice(love)
        bot.send_message(message.chat.id, msg.format(message.from_user, bot.get_me()), parse_mode = 'HTML')
        bot.send_message(message.chat.id, "Хочешь прочитать что-то ещё? Выбери сферу и я пришлю тебе цитату на выбранную тобой тему!", reply_markup = options_markup())
    elif message.text == "Мотивация 💪🏼":
        msg1 = random.choice(motivation)
        bot.send_message(message.chat.id, msg1.format(message.from_user, bot.get_me()), parse_mode = 'HTML')
        bot.send_message(message.chat.id, "Хочешь услышать еще что-то? Выбери сферу и я пришлю тебе цитату на выбранную тобой тему!", reply_markup = options_markup())
    elif message.text == "Карьера 📈":
        msg2 = random.choice(career)
        bot.send_message(message.chat.id, msg2.format(message.from_user, bot.get_me()), parse_mode = 'HTML')
        bot.send_message(message.chat.id, "Хочешь услышать еще что-то? Выбери сферу и я пришлю тебе цитату на выбранную тобой тему!", reply_markup = options_markup())
    else:
        bot.send_message (message.chat.id,"Я не знаю что тебе ответить на это🥲\n Выбери интересующую тебя сферу и я вышлю тебе цитату на эту тему!", reply_markup = options_markup())

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.data == 'check':
        check(call)
    else:
        callback_call()

bot.polling(none_stop = True)
