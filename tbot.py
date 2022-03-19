from liba import *


@bot.message_handler(commands=['start'])
def start_message(message):
    print(message.chat.id, message.from_user.id,  ' - start')
    print(message)
    name = f'{message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(
        message.chat.id,
        f'Добро пожаловать, {name}! \n👋🏻 Я - рождественский бот 🎅🏻  Моя цель - послужить вам на этом выезде, так что обращайтесь ко мне, когда вам потребуется помощь 🎄✨'
    )
    typing(message, 2)
    menu(message)
    delete(message)


@bot.message_handler(commands=['premium_cafe'])
def premium_cafe(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Кофе',
            callback_data='kofee'
        ),
        telebot.types.InlineKeyboardButton(
            'Чай',
            callback_data='tea'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Закуски',
            callback_data='food'
        ),
        telebot.types.InlineKeyboardButton(
            'Горячий шоколад',
            callback_data='chockolate'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data='menu'
        )
    )
    bot.send_message(
        message.chat.id,
        'premium_cafe',
        reply_markup=keyboard
    )


@bot.message_handler(commands=['stop'])
def start_message(message):
    us.pop(message.from_user.username)


@bot.message_handler(commands=['mes'])
def rassil1(message):
    bot.send_message(
        message.chat.id,
        'админская команда, режим рассылки включен'
    )
    global mess_to_sub

    mess_to_sub[0] = True
    mess_to_sub[1] = message.from_user.id


@bot.message_handler(commands=['esc'])
def rassil2(message):
    bot.send_message(
        message.chat.id,
        'админская команда, режим рассылки выключен'
    )
    global mess_to_sub
    mess_to_sub = [False, None]


@bot.message_handler(commands=['help'])
def help_message(message):
    mes_text = '/start - перезапустит бота\n' + '/help - выведет список возможных команд\n/menu - выведет основное меню'
    mes_text += '/child - выведет меню для детей\n/cafe_menu - выведет меню кафе\n'
    bot.send_message(
        message.chat.id,
        mes_text
    )


@bot.message_handler(commands=['child'])
def menu_message1(message):
    for_child(message)


@bot.message_handler(commands=['menu'])
def menu_message2(message):
    menu(message)


@bot.message_handler(commands=['cafe_menu'])
def cafemenuchel(message):
    cafe_menu(message)


@bot.message_handler(content_types=['photo'])
def work_with_photo(message):
    print(message.photo[3].file_id)
    global mess_to_sub
    if mess_to_sub:
        c = str(message.caption)
        if c == str(None):
            c = ''
        for i in us.keys():
            bot.send_photo(
                us[i]['chat_id'],
                str(message.photo[2].file_id),
                caption=c
            )


@bot.message_handler(content_types=['document'])
def work_with_photo(message):
    print(message.document.file_id)
    print(message.document)
    bot.send_document(slak_chat, message.document.file_id, caption=str(message.from_user.username))


@bot.message_handler(commands=['swon'])
def worcking_cafe(message):
    global get_order_status
    get_order_status = True
    menu(message)


@bot.message_handler(commands=['swoff'])
def worcking_cafe(message):
    global get_order_status
    get_order_status = False
    menu(message)


@bot.message_handler(content_types=['text'])
def work_with_text(message):
    print(orders.keys(), message.from_user.id)
    global mess_to_sub
    print(mess_to_sub)
    if mess_to_sub[0] and message.from_user.id == mess_to_sub[1]:
        for i in us.keys():
            bot.send_message(
                us[i]['chat_id'],
                '# рассылка \n' + message.text
            )
            mess_to_sub = [False, None]
        bot.send_message(
            message.chat.id,
            'отправлено'
        )
    elif message.from_user.id in orders.keys():
        s = str(orders[message.from_user.id]) + '\n' + message.text
        bot.send_message(
            cafe_chat_id,
            s
        )
        bot.send_message(
            message.chat.id,
            'не забудте оплатить заказ при получении\n/menu'
        )
        orders.pop(message.from_user.id)
    else:
        message_with_odobralka(message)
        bot.send_message(
            message.chat.id,
            'ваш вопрос пройдет модерацию и будет опубликован, после чего на него смогут ответить.\n Канал с вопросами:\nhttps://t.me/joinchat/y0RT4gdaN4dhOTIy'
        )
        time.sleep(5)
        delete(message)
        typing(message, 1)
        menu(message)
        check(message)
