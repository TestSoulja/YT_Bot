import random
import telebot
from pytube import YouTube
from telebot import types
import yadisk
import pytube
import keyboa
import requests
import posixpath
import time
import logging
from random import randint
import os
import os.path
import datetime
import time
from tqdm import tqdm
from random import randint
import os.path
import datetime
import json
import requests

# prod
import flask

app = flask.Flask(__name__)
API_TOKEN = "5568655929:AAE0teKqI_xKja6RDLuK64HbpppSziMuaHQ"
APP_HOST = "127.0.0.1"
APP_PORT = "8444"
WEB_HOOK_URL = "https://56c5-95-165-162-211.ngrok.io"

# stage
# API_TOKEN = "5624516487:AAEWFQYLHIkb3lN2sjVzpO3ignrhJVbvUWI"

# Создаем экземпляр бота
y = yadisk.YaDisk(token="y0_AgAAAAAHTEDxAAhXAgAAAADMuVu-C3oK6uX2Sji3L4Zxa4JxIUv5bC4")
bot = telebot.TeleBot(API_TOKEN)
logger = telebot.logger
a = [0]


@bot.message_handler(commands=["start"])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
	btn1 = types.KeyboardButton("_Что я могу?_")
	btn2 = types.KeyboardButton("_Выключить_")
	markup.add(btn1, btn2)
	bot.send_message(message.chat.id, text="Привет!!", reply_to_message_id=message.message_id, reply_markup=markup)
	z = message.text


@bot.message_handler(content_types=["text"])
def func(message):
	global z
	if message.text == "_Что я могу?_":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
		btn1 = types.KeyboardButton("_Скачать видео_")
		btn2 = types.KeyboardButton("_Хочу мем_")
		btn3 = types.KeyboardButton("_В начало_")
		markup.add(btn1, btn2, btn3)
		bot.send_message(message.chat.id, text="Воть..", reply_to_message_id=message.message_id, reply_markup=markup)
		z = 0
	
	elif message.text == "_Хочу мем_" or message.text == "_Ещё!!!_":
		s = random.randint(0, 100)
		s = str(s)
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
		btn1 = types.KeyboardButton("_Ещё!!!_")
		btn2 = types.KeyboardButton("_В начало_")
		markup.add(btn1, btn2)
		# Prod
		bot.send_photo(message.chat.id, open("/root/PycharmProjects/YT_Bot/AUF/Wolf/" + s + "_.jpg", "rb"), reply_to_message_id=message.message_id, reply_markup=markup)
		# Stage
		# bot.send_photo(message.chat.id, open("/Users/s.ekker/PycharmProjects/YT_Bot/AUF/Wolf/" + s + "_.jpg", "rb"),
		#                reply_to_message_id=message.message_id, reply_markup=markup)
		z = 0
	
	elif message.text == "_Скачать видео_":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
		btn1 = types.KeyboardButton("_Андрей_")
		btn2 = types.KeyboardButton("_Сережа_")
		btnext = types.KeyboardButton("_В начало_")
		markup.add(btn1, btn2, btnext)
		bot.send_message(message.chat.id, text="Хто я?".format(message.from_user),
		                 reply_to_message_id=message.message_id, reply_markup=markup)
		z = 0
	
	elif message.text == "_Андрей_":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
		btn1 = types.KeyboardButton("_В начало_")
		markup.add(btn1)
		bot.send_message(message.chat.id, text="Пришли ссылку на видос ютуб".format(message.from_user),
		                 reply_to_message_id=message.message_id, reply_markup=markup)
		z = 2
	
	elif message.text == "_Сережа_":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
		btn1 = types.KeyboardButton("_В начало_")
		markup.add(btn1)
		bot.send_message(message.chat.id, text="Пришли ссылку на видос ютуб".format(message.from_user),
		                 reply_to_message_id=message.message_id, reply_markup=markup)
		z = 1
	
	elif "https://you" in message.text and z == 1:
		x = a[-1] + 1
		a.append(x)
		x = str(x)
		c = str(message)
		yt = YouTube(c)  # ссылка на видео.
		print(yt.title)
		stream = yt.streams.get_by_itag(22)  # выбираем по тегу, в каком формате будем скачивать.
		str(yt.title)
		yt.title = yt.title.translate({ord(i): None for i in "/|#$'"})
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
		
		# Prod
		stream.download("/root/PycharmProjects/Bot/Sergey/", yt.title + ".mp4")  # загружаем видео.
		# Stage
		# stream.download("/Users/s.ekker/PycharmProjects/TestVid/", yt.title + ".mp4")  # загружаем видео.
		
		bot.send_message(message.chat.id, text=yt.title)
		bot.send_message(message.chat.id, text="To Pc OK".format(message.from_user),
		                 reply_to_message_id=message.message_id, reply_markup=markup)
		btn1 = types.KeyboardButton("_Скачать видео_")
		btn2 = types.KeyboardButton("_В начало_")
		markup.add(btn1, btn2)
		bot.send_message(message.chat.id, text="Here you are".format(message.from_user),
		                 reply_to_message_id=message.message_id, reply_markup=markup)
		z = 0
	
	elif "https://you" in message.text and z == 2:
		x = a[-1] + 1
		a.append(x)
		x = str(x)
		c = str(message)
		yt = YouTube(c)  # ссылка на видео.
		print(yt.title)
		stream = yt.streams.get_by_itag(22)  # выбираем по тегу, в каком формате будем скачивать.
		str(yt.title)
		yt.title = yt.title.translate({ord(i): None for i in "/|#$'"})
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
		
		# Prod
		stream.download("/root/PycharmProjects/Bot/Andrey/", yt.title + ".mp4")  # загружаем видео.
		# Stage
		# stream.download("/Users/s.ekker/PycharmProjects/TestVid/", yt.title + ".mp4")  # загружаем видео.
		
		bot.send_message(message.chat.id, text=yt.title)
		bot.send_message(message.chat.id, text="To Pc OK".format(message.from_user),
		                 reply_to_message_id=message.message_id, reply_markup=markup)
		btn1 = types.KeyboardButton("_В начало_")
		btn2 = types.KeyboardButton("_Скачать видео_")
		markup.add(btn1, btn2)
		bot.send_message(message.chat.id, text="Here you are".format(message.from_user),
		                 reply_to_message_id=message.message_id, reply_markup=markup)
		z = 0
	
	elif message.text == "_В начало_":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
		btn1 = types.KeyboardButton("_Что я могу?_")
		btn2 = types.KeyboardButton("_Выключить_")
		markup.add(btn1, btn2)
		bot.send_message(message.chat.id, text="Привет!! Вы снова со мной :3".format(message.from_user),
		                 reply_to_message_id=message.message_id, reply_markup=markup)
		z = 0
	
	elif message.text == "_Выключить_" or message.text == "bot_Выключить_admin":
		markup = types.ReplyKeyboardRemove(selective=True)
		bot.send_message(message.chat.id, text="Пока(", reply_to_message_id=message.message_id, reply_markup=markup)
		z = 0
	
	elif message.text == "bot_admin_console":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
		btn1 = types.KeyboardButton("bot_Очистка видео папки_admin")
		btn2 = types.KeyboardButton("bot_Выключить_admin")
		markup.add(btn1, btn2)
		bot.send_message(message.chat.id, text="/", reply_to_message_id=message.message_id, reply_markup=markup)
		z = 0
	
	else:
		z = 0


@app.route("/", methods=["POST"])
def webhook():
	if flask.request.headers.get("content-type") == "application/json":
		json_string = flask.request.get_data().decode("utf-8")
		update = telebot.types.Update.de_json(json_string)
		bot.process_new_updates([update])
		return ""
	else:
		flask.abort(403)


if __name__ == "__main__":
	bot.remove_webhook()
	time.sleep(1)
	bot.set_webhook(url=WEB_HOOK_URL)
	APP_PORT = int(APP_PORT)
	app.run(host=APP_HOST, port=APP_PORT, debug=True)

bot.polling(none_stop=True, interval=0)

# Archive

# vid = open("/root/PycharmProjects/YT_Bot/Videos/" + x + ".mp4", "rb")
# bot.send_video(message.chat.id, vid)
# vid.close()
# markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True, one_time_keyboard=False)
# btn1 = types.KeyboardButton("_В начало_")
# btn2 = types.KeyboardButton("_Скачать видео_")
# markup.add(btn1, btn2)
# bot.send_message(message.chat.id, text="Here you are".format(message.from_user),
#                  reply_markup=markup)
# z = message.text

# while not y.is_file("/Bot/Куда девать ПУСТЫЕ ФЛАКОНЫ от зелий - EPIC NPC MAN на Русском.mp4"):
# for i in range(1):
# 	try:
# 		y.upload("/Users/s.ekker/PycharmProjects/Bot/Videos/" + yt.title + ".mp4", "/Bot/" + yt.title + ".mp4")
# 	except yadisk.exceptions.PathExistsError:
# 		pass

# def recursive_upload(y, from_dir, to_dir):
# 	for root, dirs, files in os.walk(from_dir):
# 		p = root.split(from_dir)[1].strip(os.path.sep)
# 		dir_path = posixpath.join(to_dir, p)
# 		try:
# 			y.mkdir(dir_path)
# 		except yadisk.exceptions.PathExistsError:
# 			pass
# 		for file in files:
# 			file_path = posixpath.join(dir_path, file)
# 			p_sys = p.replace("/", os.path.sep)
# 			in_path = os.path.join(from_dir, p_sys, file)
# 			try:
# 				y.upload(in_path, file_path)
# 			except yadisk.exceptions.PathExistsError:
# 				pass

# to_dir = "/Bot/" + yt.title + ".mp4"
# from_dir = "/Users/s.ekker/PycharmProjects/Bot/Videos/" + yt.title + ".mp4"
# recursive_upload(y, "/Users/s.ekker/PycharmProjects/Bot/Videos/" + yt.title + ".mp4",
#                  "/Bot/" + yt.title + ".mp4")
# yadisk.functions.operations.get_operation_status
# print("OK")

# while True:
# 	if time.time() - timing > 10.0:
# 		timing = time.time()
# 		print("10 seconds")
# 	else:
# 		y.upload("/Users/s.ekker/PycharmProjects/Bot/Videos/" + yt.title + ".mp4", "/Bot/" + yt.title + ".mp4")

# Prod
# y.upload("/root/PycharmProjects/YT_Bot/Videos/" + x + ".mp4", "/Bot/")
# Stage
# y.upload("/Users/s.ekker/PycharmProjects/Bot/Videos/" + x + ".mp4", "/Bot/" + x + ".mp4")
# y.upload("/Users/s.ekker/PycharmProjects/Bot/Videos/" + yt.title + ".mp4", "/Bot/" + yt.title + ".mp4")
# bot.send_message(message.chat.id, text="To Disk OK".format(message.from_user),
#                  reply_to_message_id=message.message_id, reply_markup=markup)
