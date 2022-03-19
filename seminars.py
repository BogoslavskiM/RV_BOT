import random
import asyncio
from cafe_functions import *
from data import timetable as t
from data import child as ch
from data import s0, s1, s2, s3, time0, time1, time2, time3
from data import users as us
from game_qwestions import gq as gq
from threading import Thread


def seminar(query):
    keyboard = telebot.types.InlineKeyboardMarkup()
    if str(query.data) == 'friday1800': p = s2
    elif str(query.data) == 'friday1730': p = s1
    elif str(query.data) == 'satarday1800': p = s3
    for i in p.keys():
        t = p[i]['time']
        keyboard.row(
            telebot.types.InlineKeyboardButton(
                p[i]['name'],
                callback_data=f'{i}'
            )
        )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data='seminars'
        )
    )
    bot.send_message(
        query.message.chat.id,
        f'Блок семинаров, начинающихся в {t}, выберите тот, на который хотите пойти, вам придет уведомление за 15 мин до начала семинара',
        reply_markup=keyboard
    )


def seminar123(query):
    if query.data in s1.keys():
        message = s1[query.data]['name'] + ' \n' +  s1[query.data]['description'] + '\n' + s1[query.data]['time']
        a = 'friday1730'
    elif query.data in s2.keys():
        message = s2[query.data]['name'] + ' \n' +  s2[query.data]['description'] + '\n' + s2[query.data]['time']
        a = 'friday1800'
    elif query.data in s3.keys():
        message = s3[query.data]['name'] + ' \n' +  s3[query.data]['description'] + '\n' + s3[query.data]['time']
        a = 'satarday1800'
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Напомнить мне о семинаре',
            callback_data=f'RMM/{query.data}'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Назад',
            callback_data=f'{a}'
        )
    )
    bot.send_message(
        query.message.chat.id,
        message,
        reply_markup=keyboard
    )


def RMM(query):
    s = str(query.data)
    s = s[4:]
    print(s)
    if s in s1.keys(): s1[s]['notify'].append(str(query.message.chat.id))
    elif s in s2.keys(): s2[s]['notify'].append(str(query.message.chat.id))
    elif s in s3.keys(): s3[s]['notify'].apend(str(query.message.chat.id))
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Меню',
            callback_data='menu'
        )
    )
    bot.send_message(
        query.message.chat.id,
        'Ok, я запомнил',
        reply_markup=keyboard
    )


def remind():
    while True:
        while True:
            x = time.localtime()
            year, month, day, hour, min_t = x.tm_year, x.tm_mon, x.tm_mday, x.tm_hour, x.tm_min
            min_t += hour * 60 + day * 24 * 60 - 24 * 24 * 60
            if time0['s'] - 16 <= min_t <= time0['s'] - 15:
                p = s0
                break
            elif time1['s'] - 16 <= min_t <= time1['s'] - 15:
                p = s1
                break
            elif time2['s'] - 16 <= min_t <= time2['s'] - 15:
                p = s2
                break
            elif time3['s'] - 15 <= min_t <= time3['s'] - 15:
                p = s3
                break
            else:
                time.sleep(40)
        for i in p.keys():
            mes = f'вы просили напомнить о семинаре "{p[i]["name"]}",\n он начнется через 15 минут, успейте занять места'
            mes += f'\n\n{p[i]["description"]}\n/menu'
            for j in p[i]['notify']:
                try:
                    print(j, p[i]['notify'])
                    bot.send_message(
                        j,
                        mes
                    )
                except:
                    pass
        time.sleep(120)
        if p == s3:
            break


th = Thread(target=remind)
th.start()
