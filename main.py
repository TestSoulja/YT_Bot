import random
import telebot
import pytube
from pytube import YouTube
import keyboa
import requests
from telebot import types
from random import randint
import os
import os.path
import datetime
import time
from tqdm import tqdm
from random import randint
import os.path
import datetime

# Создаем экземпляр бота
token = "5568655929:AAE0teKqI_xKja6RDLuK64HbpppSziMuaHQ"
bot = telebot.TeleBot("5568655929:AAE0teKqI_xKja6RDLuK64HbpppSziMuaHQ")

a = [0]


@bot.message_handler(commands=["start"])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True, one_time_keyboard=False)
	btn1 = types.KeyboardButton("_Что я могу?_")
	btn2 = types.KeyboardButton("_Выключить_")
	markup.add(btn1, btn2)
	bot.send_message(message.chat.id, text="Привет!!".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=["text"])
def func(message):
	z = message.text
	if message.text == "_Что я могу?_":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True, one_time_keyboard=False)
		btn1 = types.KeyboardButton("_Скачать видео_")
		btn2 = types.KeyboardButton("_Хочу мем_")
		btn3 = types.KeyboardButton("_В начало_")
		markup.add(btn1, btn2, btn3)
		bot.send_message(message.chat.id, text="Воть..".format(message.from_user), reply_markup=markup)
		z = message.text
	
	elif message.text == "_Хочу мем_" or message.text == "_Ещё!!!_":
		s = random.randint(0, 100)
		s = str(s)
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True, one_time_keyboard=False)
		btn1 = types.KeyboardButton("_Ещё!!!_")
		btn2 = types.KeyboardButton("_В начало_")
		markup.add(btn1, btn2)
		bot.send_photo(message.chat.id, open("/Users/s.ekker/PycharmProjects/Bot/AUF/Wolf/"+ s+"_.jpg", "rb"), reply_markup=markup)
		z = message.text
	
	elif message.text == "_Скачать видео_":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True, one_time_keyboard=False)
		btn1 = types.KeyboardButton("_В начало_")
		markup.add(btn1)
		bot.send_message(message.chat.id, text="Пришли ссылку на видео ютуба".format(message.from_user),
		                 reply_markup=markup)
		z = message.text
	
	elif "https" in message.text and z == "_bot_Скачать видео_":
		x = a[-1] + 1
		a.append(x)
		x = str(x)
		c = str(message)
		yt = YouTube(c)  # ссылка на видео.
		# yt.stream показывает какое видео ты можешь скачать
		# (mp4(720) + audio или только mp4(1080) без звука).
		# Сейчас стоит фильтр по mp4.
		# print(yt.streams.filter(file_extension='mp4'))
		print(yt.title)
		stream = yt.streams.get_by_itag(22)  # выбираем по тегу, в каком формате будем скачивать.
		stream.download("/Users/s.ekker/Desktop/YT", x + ".mp4")  # загружаем видео.
		str(yt.title)
		bot.send_message(message.chat.id, text=yt.title)
		bot.delete_message(message.chat.id, message.message_id)
		
		vid = open('/Users/s.ekker/Desktop/YT/' + x + ".mp4", 'rb')
		bot.send_video(message.chat.id, vid, message.message_id)
		vid.close()
		z = message.text
		
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True, one_time_keyboard=False)
		btn1 = types.KeyboardButton("_В начало_")
		btn2 = types.KeyboardButton("_Скачать видео_")
		markup.add(btn1, btn2)
		bot.send_message(message.chat.id, text="Here you are".format(message.from_user),
		                 reply_markup=markup)
		
	elif message.text == "_В начало_":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True, one_time_keyboard=False)
		btn1 = types.KeyboardButton("_Что я могу?_")
		btn2 = types.KeyboardButton("_Выключить_")
		markup.add(btn1, btn2)
		bot.send_message(message.chat.id, text="Привет!! Вы снова со мной :3".format(message.from_user), reply_markup=markup)
		z = message.text
	
	elif message.text == "_Выключить_" or message.text == "bot_Выключить_admin":
		markup = types.ReplyKeyboardRemove(selective=True)
		bot.send_message(message.chat.id, text="Пока(", reply_markup=markup)
		z = message.text
		
	elif message.text == "bot_admin_console":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True, one_time_keyboard=False)
		btn1 = types.KeyboardButton("bot_Очистка видео папки_admin")
		btn2 = types.KeyboardButton("bot_Выключить_admin")
		markup.add(btn1, btn2)
		bot.send_message(message.chat.id, text="/", reply_markup=markup)
		z = message.text
		
	
	# elif message.text == "bot_Очистка видео папки_admin":
	# 	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True, one_time_keyboard=False)
	# 	btn1 = types.KeyboardButton("bot_Очистка видео папки_admin")
	# 	btn2 = types.KeyboardButton("bot_Выключить_admin")
	# 	markup.add(btn1, btn2)
	# 	bot.send_message(message.chat.id, text="Папка почищена, удалено n", reply_markup=markup)
	# 	z = message.text
	# elif message.text == "bot_Выключить_admin":
	# 	markup = types.ReplyKeyboardRemove(selective=False)
	# 	bot.send_message(message.chat.id, text="Пока всем(", reply_markup=markup)
	# 	z = message.text


bot.polling(none_stop=True, interval=0)