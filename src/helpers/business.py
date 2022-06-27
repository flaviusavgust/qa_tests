# # -*- coding: utf-8 -*-
# import telebot
#
# bot = telebot.TeleBot('1921308623:AAE0khbbB4E9C4aIGCEDyMGJz5YUcxQDvlQ')
# build_status = 'true'
#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     test_message = f"Прогон завершился: {build_status} \n "
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, test_message)
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши Привет")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# bot.polling(none_stop=True, interval=0)

