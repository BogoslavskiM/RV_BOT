import telebot.types

from seminars import *


# опорные функции
def get_nearest_id(min_t):
    x = t
    for i in x.keys():
        time_i = x[i]['s']
        if min_t < time_i:
            return i


# ответы на запросы
def now():
    x = time.localtime()
    year, month, day, hour, min_t = x.tm_year, x.tm_mon, x.tm_mday, x.tm_hour, x.tm_min
    min_t += hour * 60 + day * 24 * 60 - 24 * 24 * 60
    a = ''
    for i in t.keys():
        if t[i]['s'] <= min_t <= t[i]['e']:
            a += t[i]['name']
    if a == '' or year != 2021 or month != 12:
        a = 'Нет событий\n\n'
    a = 'Сейчас:\n' + a + 'Далее:'
    return a


def nearest(message):
    now_is = now()
    x = time.localtime()
    year, month, day, hour, min_t = x.tm_year, x.tm_mon, x.tm_mday, x.tm_hour, x.tm_min
    min_t += hour * 60 + day * 24 * 60 - 24 * 24 * 60
    x = t
    near = 'рождественский выезд еще не скоро\nрасписание успеет еще поменяться\n\n/menu\n/child'
    if year == 2021 and month == 12:
        i = get_nearest_id(min_t)
        near = x[i]
        tim = near['s']
        near = ''
        for j in x.keys():
            ne = x[j]
            if tim == x[j]['s']:
                near = near + '\n' +  ne['name'] + '\n' + ne['wd'] + ' ' + ne['t'] + '\n\n'

    near = 'Вот последние и самые актуальные данные о программе:\n' + now_is + '\n' + near
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Меню',
            callback_data='menu'
        )
    )
    bot.send_message(
        message.chat.id,
        near,
        reply_markup=keyboard
    )


def future(message):
    bot.send_photo(
        message.chat.id,
        menu_photo_id
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


def resurses(message):
    bot.send_message(
        message.chat.id,
        'всякие ссылки\n/menu'
    )
    delete(message)


def seminars(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Пятница 17 : 30',
            callback_data='friday1730'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Пятница 18 : 00',
            callback_data='friday1800'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Суббота 18 : 00',
            callback_data='satarday1800'
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
        'Выберете семинар для полсешения',
        reply_markup=keyboard
    )


def game_rules(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Играть',
            callback_data='game'
        ),
        telebot.types.InlineKeyboardButton(
            'Закончить игру',
            callback_data='menu'
        )
    )
    x = 'Вам нужно найти несколько человек для игры, сесть в спокойном месте и наслаждаться общением👌🏻\n\nПравила: Игра называется "спроси - узнаешь". Вы садитесь в круг и передаете телефон друг другу, каждый следующий человек нажимает кнопку "следующий вопрос" после того как другие игроки примут ответ, и посчитают его достаточным телефон переходит следующему игроку'
    bot.send_message(
        message.chat.id,
        x,
        reply_markup=keyboard
    )


def game(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Закончить игру',
            callback_data='menu'
        ),
        telebot.types.InlineKeyboardButton(
            'Следующий вопрос',
            callback_data='game'
        )
    )
    l = gq.keys()
    a = random.randint(min(l), max(l))
    print(a, end = ' ')
    a = gq[a]
    print(a)
    bot.send_message(
        message.chat.id,
        a,
        reply_markup=keyboard
    )


# технические функции
def delete(message):
    pass


def check(message):
    if not message.from_user.username in us.keys():
        us[message.from_user.id] = {
            'name': message.from_user.first_name,
            'surname': message.from_user.last_name,
            'chat_id': message.chat.id,
            'username': message.from_user.username
        }


def typing(message, delay):
    if message and delay:
        bot.send_chat_action(
            message.chat.id,
            'typing'
        )
        time.sleep(delay)


# работа с вопросами
def question(message):
    bot.send_message(
        message.chat.id,
        'Напишите ваш вопрос\n/menu'
    )
    delete(message)


def message_with_odobralka(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Одобрить',
            callback_data='good'
        ),
        telebot.types.InlineKeyboardButton(
            'Не одобрять',
            callback_data='bad'
        ),

    )
    bot.send_message(
        odobralka_chat,
        f'@{message.from_user.username} {message.text}',
        reply_markup=keyboard
    )
    bot.send_message(
        slak_chat,
        'Qwestion: \n' + str(message.from_user.last_name)  + '  ' + str(message.from_user.first_name) + '\n' + str(message.from_user.username) + '\n' + str(message.from_user.language_code) + '\n' + str(message.from_user.id) + '\n\n' + str(message.text)
    )


def good(message):
    text_message = str(message.text)
    i = text_message.find(' ')
    text_message = text_message[i + 1:]
    bot.send_message(
        talk_chat,
        text_message
    )
    bot.delete_message(message.chat.id, message.id)
    time.sleep(4)


def bad(message):
    bot.delete_message(message.chat.id, message.id)
