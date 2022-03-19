from settings import *
from data import cafe_menu_data, cafe_working_time


def kofee(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Капучино',
            callback_data='capusino'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Американо',
            callback_data='amerikano'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Латтэ',
            callback_data='latte'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Раф',
            callback_data='raf'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Эспрессо',
            callback_data='espresso'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data='cafe'
        )
    )
    bot.send_message(
        message.chat.id,
        'Всякие разные виды кофе:',
        reply_markup=keyboard
    )


def tea(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Малина - имбирь',
            callback_data='raspberry-ginger'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Облепиха - имбирь',
            callback_data='sea_buckthorn-ginger'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Апельсин - имбирь',
            callback_data='orange-ginger'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data='cafe'
        )
    )
    bot.send_message(
        message.chat.id,
        'Горячий чай с имбирем поможет справиться с любой болезнью🤒 и просто скрасит ваш день🌝',
        reply_markup=keyboard
    )


def food(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Мясной тост',
            callback_data='meat_tost'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Сладкий тост',
            callback_data='sweet_tost'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Каша с яблоком и медом',
            callback_data='kakayato_kasha'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data='cafe'
        )
    )
    bot.send_message(
        message.chat.id,
        'Мы готовим тосты с хрустящей корочкой 🥪 и вкусным содержимым 😊',
        reply_markup=keyboard
    )


def chockolate(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            '250 мл - 50 р',
            callback_data='hc250'
        ),
        telebot.types.InlineKeyboardButton(
            '350 мл - 80 р',
            callback_data='hc350'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data='cafe'
        )
    )
    bot.send_message(
        message.chat.id,
        'Напиток на основе какао и молока🥛 Идеален для детей 👶🏻',
        reply_markup=keyboard
    )


def is_working_cafe():
    x = time.localtime()
    year, month, day, hour, min_t = x.tm_year, x.tm_mon, x.tm_mday, x.tm_hour, x.tm_min
    min_t += hour * 60 + day * 24 * 60 - 24 * 24 * 60
    for i in cafe_working_time.keys():
        if cafe_working_time[i]['s'] <= min_t <= cafe_working_time[i]['e']:
            return True
        elif cafe_working_time[i]['s'] <= min_t:
            return False


def nearest_cafe_time():
    x = time.localtime()
    year, month, day, hour, min_t = x.tm_year, x.tm_mon, x.tm_mday, x.tm_hour, x.tm_min
    min_t += hour * 60 + day * 24 * 60 - 24 * 24 * 60
    for i in cafe_working_time.keys():
        if cafe_working_time[i]['s'] > min_t:
            return cafe_working_time[i]['t']
    return 'никогда'

def cafe_menu(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    # keyboard.row(
    #     telebot.types.InlineKeyboardButton(
    #         'Кофе',
    #         callback_data='kofee'
    #     ),
    #     telebot.types.InlineKeyboardButton(
    #         'Чай',
    #         callback_data='tea'
    #     )
    # )
    # keyboard.row(
    #     telebot.types.InlineKeyboardButton(
    #         'Закуски',
    #         callback_data='food'
    #     ),
    #     telebot.types.InlineKeyboardButton(
    #         'Горячий шоколад',
    #         callback_data='chockolate'
    #     )
    # )
    # keyboard.row(
    #     telebot.types.InlineKeyboardButton(
    #         'Назад',
    #         callback_data='menu'
    #     )
    # )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Чай малина - имбирь',
            callback_data='raspberry-ginger'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Чай облепиха - имбирь',
            callback_data='sea_buckthorn-ginger'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Чай апельсин - имбирь',
            callback_data='orange-ginger'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Глинтвейн',
            callback_data='mulled_wine'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Чай клюква',
            callback_data='cranberry'
        )
    )
    keyboard.row(
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
    if is_working_cafe():
        bot.send_message(
            message.chat.id,
            'Да, да, вам не показалось, я могу заказать напиток ☕️ в кафе для вас, теперь незачем стоять в очереди 🤩\n\n(Пока что я могу заказать лишь часть ассортимента, остальное придется заказывать у кассы. ⚙️Ждем обновления)',
                reply_markup=keyboard
        )
    else:
        k = telebot.types.InlineKeyboardMarkup()
        k.row(telebot.types.InlineKeyboardButton('Меню', callback_data='menu'))
        m = 'Да, да, вам не показалось, я могу заказать напиток ☕️ в кафе для вас, но к сожалению кафе сейчас не работает'
        m += f'\nКафе будет работать с {nearest_cafe_time()}'
        bot.send_message(
            message.chat.id,
            m,
            reply_markup=k
        )


# cofee - functions
def latte(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Латте',
            callback_data='simple_latte'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Латте на овсянном молоке',
            callback_data='not_simple_latte'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data='cafe'
        )
    )
    bot.send_message(
        message.chat.id,
        'Латте - напиток родом из италии🇮🇹, состоящий из молока 🥛и эспрессо ☕️\nБолее молочный, по сравнению с капучино',
        reply_markup=keyboard
    )


def capusino(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Капучино - 120',
            callback_data='simple_capusino'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Капучино на овсянном молоке - 120',
            callback_data='not_simple_capusino'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Капучино с доп. шотом - 150',
            callback_data='simple_capusino+'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Капучино с доп. шотом на овсянном молоке - 150',
            callback_data='not_simple_capusino+'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data='cafe'
        )
    )
    bot.send_message(
        message.chat.id,
        'Капучино - кофейный напиток на основе эспрессо ☕️ с добавлением молока🥛\nБолее кофейный по сравнению с латте\n\nВы можете взять капучино на овсяном молоке, если желаете\n\nТакже мы можем добавить доп. шот эспрессо в ваш капучино',
        reply_markup=keyboard
    )


def raf(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Цитрус - 199р',
            callback_data='sitrus'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Халва - 199р',
            callback_data='halva'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Орех- 199р',
            callback_data='nut'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Классик - 199р',
            callback_data='classic'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data='cafe'
        )
    )
    bot.send_message(
        message.chat.id,
        'Кофе раф делается на сливках 🍶 и эспрессо ☕️, очень нежный на вкус с наполнителем на выбор:\n(Если хотите раф без сиропа, можете указать дальше в комментарии)',
        reply_markup=keyboard
    )


def amerikano(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Американо 250 мл - 60р',
            callback_data='americano250'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Американо 350мл - 80р',
            callback_data='americano350'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data='cafe'
        )
    )
    bot.send_message(
        message.chat.id,
        'Американо - черный не концентрированный кофе ☕️',
        reply_markup=keyboard
    )


def espresso(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Эспрессо - 50р',
            callback_data='espresso50'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Двойной эспрессо - 80р',
            callback_data='espresso80'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data='cafe'
        )
    )
    bot.send_message(
        message.chat.id,
        '30 мл концентрированного кофе из зерен арабики ☕️\n\nВы также можете заказать двойной эспрессо, который разбудит вас наверняка 💪🏻️',
        reply_markup=keyboard
    )


# tea - functions
def raspberry_ginger(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Малина - имбирь 250 мл - 60р',
            callback_data='raspberry_ginger250'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Малина - имбирь 350 мл - 80',
            callback_data='raspberry_ginger350'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data='cafe'
        )
    )
    bot.send_message(
        message.chat.id,
        'Отличный выбор, какой обьем этого чудесного напитка вам приготовить?',
        reply_markup=keyboard
    )


def sea_buckthorn_ginger(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Облепиха - имбирь 250 мл - 60р',
            callback_data='sea_buckthorn-ginger250'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Облепиха - имбирь 350 мл - 80',
            callback_data='sea_buckthorn-ginger350'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data='cafe'
        )
    )
    bot.send_message(
        message.chat.id,
        'Отличный выбор, какой обьем этого чудесного напитка вам приготовить?',
        reply_markup=keyboard
    )


def orange_ginger(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Апельсин -  имбирь 250 мл - 60р',
            callback_data='orange-ginger250'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Апельсин -  имбирь 350 мл - 80',
            callback_data='orange-ginger350'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data='cafe'
        )
    )
    bot.send_message(
        message.chat.id,
        'Отличный выбор, какой обьем этого чудесного напитка вам приготовить?',
        reply_markup=keyboard
    )


def get_order(query):
    orders[query.from_user.id] = cafe_menu_data[query.data]
    bot.send_message(
        query.message.chat.id,
        'Обычный вопрос\n\nНа чье имя подписать стаканчик🥤? Пожалуйста, укажите еще фамилию, чтобы никто не перепутал ваш напиток 😊\n\nТакже здесь вы можете указать любой комментарий к заказу ✏️'
    )
