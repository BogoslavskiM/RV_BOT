from library import *


# основное меню
def menu(message):
    global get_order_status
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Узнать ближайшее событие',
            callback_data='now-nearest'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Узнать общее расписание программы',
            callback_data='future'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Для детей',
            callback_data='for_child'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Выбрать семинар для посещения',
            callback_data='seminars'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Сыграть в игру на общение',
            callback_data='game_rules'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Заказать напиток в кафе',
            callback_data='cafe'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Задать вопрос',
            callback_data='question'
        )
    )

    bot.send_message(
        message.chat.id,
       'Что вы хотите?',
        reply_markup=keyboard,
    )


def for_child(message):
    bot.send_photo(
        message.chat.id,
        child_menu_photo_id
    )
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Да!',
            callback_data='menu'
        )
    )
    bot.send_message(
        message.chat.id,
        'Хотите вернуться в основное меню?',
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    print(query.data)
    x = str(query.data)
    if str(query.data) == 'now-nearest': nearest(query.message)
    elif str(query.data) == 'future': future(query.message)
    elif str(query.data) == 'resurses': resurses(query.message)
    elif str(query.data) == 'for_child': for_child(query.message)
    elif str(query.data) == 'question': question(query.message)
    elif str(query.data) == 'good': good(query.message)
    elif str(query.data) == 'bad': bad(query.message)
    elif str(query.data) == 'seminars': seminars(query.message)
    elif str(query.data) == 'menu': menu(query.message)
    elif str(query.data) == 'cafe': cafe_menu(query.message)
    elif str(query.data) == 'game': game(query.message)
    elif str(query.data) == 'game_rules': game_rules(query.message)
    elif str(query.data) == 'kofee': kofee(query.message)
    elif str(query.data) == 'tea': tea(query.message)
    elif str(query.data) == 'food': food(query.message)
    elif str(query.data) == 'chockolate': chockolate(query.message)
    elif str(query.data) == 'orange-ginger': orange_ginger(query.message)
    elif str(query.data) == 'capusino': capusino( query.message)
    elif str(query.data) == 'amerikano': amerikano(query.message)
    elif str(query.data) == 'latte': latte(query.message)
    elif str(query.data) == 'raf': raf(query.message)
    elif str(query.data) == 'espresso': espresso(query.message)
    elif str(query.data) == 'raspberry-ginger': raspberry_ginger(query.message)
    elif str(query.data) == 'sea_buckthorn-ginger': sea_buckthorn_ginger(query.message)
    elif str(query.data) in cafe_menu_data.keys(): get_order(query)
    elif str(query.data) in ['friday1730', 'friday1800', 'satarday1800']: seminar(query)
    elif x in s1.keys() or x in s2.keys() or x in s3.keys(): seminar123(query)
    elif x[:3] == 'RMM': RMM(query)
