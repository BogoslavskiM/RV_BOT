import json
import requests
import telebot
import time

# APIS
TOKEN = '5097703894:AAFFcAITGDGbRBiS3R5PBCkmFF6gkoQhRRE'
TOKEN = '1758291980:AAFrT-pKFGyGkI_TurQ1ueURbKPcIapFzks'
bot = telebot.TeleBot(TOKEN)
# chats
odobralka_chat = '-1001596783480'
talk_chat = '-1001513463257'
cafe_chat_id = '-1001733726485'
slak_chat = '-1001781532365'
URL = 'http://127.0.0.1:8000'
# varibales
get_question_status = False
game_mode = False
mess_to_sub = [False, None]
get_order_status = False
child_menu_photo_id = 'AgACAgIAAxkBAAITXGHB9Zsgmlp8SZCHNoP8gGnqz54IAALctzEbaHkJSseFKHG4ZaAZAQADAgADeQADIwQ'
menu_photo_id = 'AgACAgIAAxkBAAITVGHB9UeOkANzPZ0Qg2ct8pOa87YzAALbtzEbaHkJSqJ3-iwee5bdAQADAgADeQADIwQ'

orders = dict()
