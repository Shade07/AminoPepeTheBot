#Bot Amino Pepe version 2.0.2 by Lil Zevi/Langa
# -*- coding: utf8 -*-
from BotAmino import *
from fancy_text import fancy
import sys
import emoji
import urllib.request
import time
from pathlib import Path
from google_trans_new import google_translator
import random
import os
from os import path
from random import uniform, choice, randint
client = BotAmino("email", "password") #Type email and password/Введите пароль и почту сюда
vers = "1.1.4"
print(f"Bot Version = {vers}")

@client.command("vkidsnusovski")
def vkidsnusovski(data):
    data.subClient.send_message(data.chatId, message="""
[C]Я бот vkidsnusovski! My Commands/Мои Команды
[C]!vkidsnusovski [Информация о боте!]
[C]!zabiv [игрок1, игрок2] - Игра забив без правил ауе🦁💪🏿
[C]!snus [Пользователь] - Сделать термоядерный вкид🥴
[C]!randemoji - Команда чтобы бот кинул 5 рандомных стикеров!
[C]!fancytext [Текст] - Команда чтобы бот украсил текст!
[C]!luv [Пользователь - 1, Пользователь - 2] - Команда чтобы проверить кто у кого сосет!
[C]!google [Текст] - Команда чтобы поискать что-то в гугле!
[C]!qs [Текст] - Команда чтобы задать вопрос боту!
[C]!joinallchats - Команда чтобы бот зашел во все активные чаты.
[C]!chatinfo - Команда чтобы получить chatId чата от бота.
[C]!text [Текст] - Написать что то от имени бота
[C]!vkidsnusovski2 [Вторая часть команд бота!]
""")

@client.command("vkidsnusovski2")
def vkidsnusovski2(data):
	data.subClient.send_message(data.chatId, message="""
[C]!follow - Команда чтобы бот подписался на вас.
[C]!unfollow - Команда чтобы бот отписался от вас.
[C]!joinchat [Ссылка на чат/Chat Link] - Команда чтобы бот зашел в выбранный чат по ссылке
[C]!backgr - Команда чтобы получить фон чата!)
[C]!staffask [Текст] - Команда чтобы анонимно писать через бота всем кураторам,лидерам. 
[C]!sperm - Секретная команда😱
[C]!translate [Текст] - Команда чтобы перевести что то на английский
[C]!stickmg - Команда чтобы получить стикер в виде изображения.
[C]!reboot - Команда чтобы перезапустить бота!
[C]!comment - Команда чтобы получить роспись от бота!
[C]!msgtypes - Команда чтобы получить типы сообщений.
[C]Бот сделан - !!github.com/LilZevi, YouTube - !!https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ
[C]Бот будет дополнятся!
""")

@client.on_member_join_chat()
def privet(data):
    data.subClient.send_message(data.chatId, f"Добро Пожаловать в чат {data.author} я бот мои команды !vkidsnusovski)")


@client.on_member_leave_chat(["chatId"]) # the chatId is not necessary, put one if you want a specified chat only
def poka(data):
    data.subClient.send_message(data.chatId, f"К сожалению {data.author} покинул чат! Пожелаем ему удачи!")


############################Commands info in english!############################
#vkidsnusovski [Information about the bot!]
#vkidsnusovski2 [information about the bot2!]
#!zabiv [player1, player2] - Scoring game without rules  🦁 💪 🏿 command  author github.com/BrenoMartinsDeOliveiraVasconcelo
#!snus - [User] - A fun command for snus🥴
#!luv [User-1, User-2] - A command to Check who sucks who!
#!google [Text] - A command to search for something in google!
#!qs [Text] - Command to ask a question to the bot!
#!joinallchats-A command for the bot to log in to all active chats.
#!joinchat [Link to the chat/Chat Link] - Command for the bot to enter the selected chat using the link
#!chatinfo - Command for get chatId of the chat
#!follow - command to let the bot follow to you
#!backgr - Command for get background image of the chat!
#!staffask [Text] - A command to write anonymously through the bot to all curators and leaders.
#!sperm - secret command
#!translate [Text] - A command to translate something into English
#!stickmg - Command for convert sticker to image.
#The bot is done - github.com/LilZevi, YouTube - https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ
#The bot will be updated!
################################################commands/команды################################################
@client.command("luv")
def luv(data):
		msg = data.message + " null null "
		msg = msg.split(" ")
		msg[2] = msg[1]
		msg[1] = msg[0]
		try:
			data.subClient.send_message(chatId=data.chatId, message=f"Вероятность того что  {msg[1]} сосет у {msg[2]} равна {random.randint(0,100)}%")
		except:
			pass

@client.command("google")
def google(data):
    msg = data.message.split(" ")
    msg = '+'.join(msg)
    data.subClient.send_message(chatId=data.chatId, message=f"https://www.google.com/search?q={msg}")

@client.command("snus")
def snus(data):
	msg = data.message + " null "
	msg = msg.split(" ")
	msg[1] = msg[0]
	try:
		data.subClient.send_message(chatId=data.chatId, message=f"{msg[1]} сделал термоядерный снюсовый супер вкид овсянкасер🥴...")
	except:
		pass
#command author github.com/BrenoMartinsDeOliveiraVasconcelos
@client.command("zabiv")
def zabiv(data):
	msg = data.message + " null null "
	msg = msg.split(" ")
	try:
		rounds = int(msg[0])
	except (TypeError, ValueError):
		rounds = 5
		msg[2] = msg[1]
		msg[1] = msg[0]
		msg[0] = 5
	data.subClient.send_message(chatId=data.chatId, message=f"Начинается забив между  {msg[1]} и {msg[2]}...")
	win1 = 0
	win2 = 0
	round = 0
	agress = ''
	defens = ''
	for zabiv in range(0, rounds):
		round = round + 1
		data.subClient.send_message(chatId=data.chatId, message=f"[bc]Round/Раунд {round}/{rounds}")
		punch = randint(0, 1)
		if punch == 0:
			win1 = win1 + 1
			agress = msg[1]
			defens = msg[2]
		else:
			     	win2 = win2 + 1
			     	agress = msg[2]
			     	defens = msg[1]
		time.sleep(4)
		data.subClient.send_message(chatId=data.chatId, message=f"[ic] {agress} ударил👊🏿 {defens}!")
		if win1 > win2:
		  data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[1]} Выиграл в забиве!")
		elif win1 < win2:
		  	data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[2]} Выиграл в забиве!")
		elif win1 == win2:
		  		data.subClient.send_message(chatId=data.chatId, message=f"[iC]Ничья никто не выиграл кроме бабки в кедах!.")
#Команда для вопросов для бота
@client.command("qs")
def qs(data):
	lis = ['Возможно', 'Да', 'Нет', 'Конечно', 'Наверное']
	msg = data.message + "null?"
	msg = data.message.split(" ")
	data.subClient.send_message(chatId=data.chatId, message=str(random.choice(lis)))

@client.command("sperm")
def sperm(data):
	msg = data.message + " null "
	msg = msg.split(" ")
	msg[2] = msg[1]
	msg[1] = msg[0]
	try:
		data.subClient.send_message(chatId=data.chatId, message=f"{msg[1]} получил сперму в рот и был забит членом досмерти...")
	except:
		pass
#Команда чтобы бот заходил во все активные чаты
@client.command("joinallchats")
def joinallchats(data):
	print(type(data))
	data.subClient.send_message(chatId=data.chatId, message="Заходим во все активные чаты в сообществе...")
	data.subClient.join_all_chat()
	data.subClient.send_message(chatId=data.chatId, message="Зашли во все активные чаты!")
@client.command("joinchat")
def joinchat(data):
	try:
		data.subClient.send_message(chatId=data.chatId, message="Заходим в выбранный чат")
		data.subClient.join_chatroom(data.message)
		data.subClient.send_message(chatId=data.chatId, message="Зашли в выбранный чат")
	except:
		data.subClient.send_message(chatId=data.chatId, message="Не удалось зайти в выбранный чат возможно бота кикнули!")
		pass

@client.command("follow")
def follow(data):
	try:
		data.subClient.send_message(data.chatId, f'Подписались на {data.author}')
		data.subClient.follow_user(data.authorId)
	except:
		data.subClient.send_message(data.chatId, f'Не удалось подписаться на {data.author}')
		pass

@client.command("chatinfo")
def chatinfo(data):
	data.subClient.send_message(data.chatId, f"chatId = {data.chatId}")

@client.command("backgr")
def backgr(data):
        image = data.subClient.get_chat_thread(chatId=data.chatId).backgroundImage
        if image:
            filename = path.basename(image)
            urllib.request.urlretrieve(image, filename)
            with open(filename, 'rb') as fp: data.subClient.send_message(data.chatId, file=fp, fileType="image")
            os.remove(filename)

@client.command("staffask")
def staffask(data):
	msg = data.message + " null "
	msg = msg.split(" ")
	msg[2] = msg[1]
	msg[1] = msg[0]
	data.subClient.ask_amino_staff(message=msg[1])
	data.subClient.ask_amino_staff(message=f"Это Сообщение было отправлено {data.author}/Я бот! Хорошего дня")

@client.command("translate")
def translate(data):
    translator = google_translator()
    translate_text = translator.translate(data.message)
    data.subClient.send_message(data.chatId, f"Перевод: {translate_text}")

@client.command("stickmg")
def stickmg(data):
	info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
	reply_message = info.json['extensions']
	if reply_message:
	   image = info.json['extensions']['replyMessage']['extensions']['sticker']['icon']
	   filename = image.split("/")[-1]
	   filetype = image.split(".")[-1]
	   if filetype!="gif":
	   	filetype = "image"
	   	urllib.request.urlretrieve(image, filename)
	   	with open(filename, 'rb') as fp: data.subClient.send_message(data.chatId, file=fp, fileType="image")
	os.remove(filename)

#########Команда для изменения ника бота/Command to change the bot's nickname############
@client.command("nckname")
def nckname(data):
	data.subClient.subclient.edit_profile(nickname=data.message)
	data.subClient.send_message(chatId=data.chatId,message=f"Ник бота изменен на {data.message}")

@client.command("unfollow")
def unfollow(data):
    data.subClient.send_message(data.chatId, f'Отписались от {data.author}')
    data.subClient.unfollow_user(data.authorId)

@client.command("welcome")
def welcome(data):
        data.subClient.set_welcome_message(data.message)
        data.subClient.send_message(data.chatId, "Приветственное сообщение изменено")

@client.command("randemoji")
def randemoji(data):
	lis = ['😰😨😱😓🤯', '😎🤡🥴🤕🌚', '🌝🥸👻🎃', '😺👹😈😇💩', '😛😉😊😘🥳', '🤣😀😆🥰🙂', '☺️😑🙃😶🤗', '🤩😋😔😌☺️', '🤫🤐🥺🙄🤔', '🧐😤😠😳🤯', '😓😥😩😖😵', '🌞🤮🤧🤒🎃', '😍😚🤭🥲😄', '😃😂🤣😭😰', '🤬😡😮😯😲', '🤓🤑🤠😇😷', '🥵🥶👺☠️👽', '😸😹😺😻😼', '😽🙀😿😾💀', '❤️🧡💛💚💙', '💜🤎🖤🤍♥️', '💘💝💖💗💓', '💞💕💌💟❣️', '💔💋👅👄👀', '🦾🦠🦷🏵️💐', '🧝🧙🧛🧟🥷', '😪😴🥱🤤🙄', '👿😈🔥⭐🌟', '🎊🎉🕳️💤💦', '🌜👻🤖💢⚡', '✨💫👁️🍂☀️', '🧠🫀🫁🩸🌡️', '👉👌🍺🍷👄', '🦁🐻🐼🐨🐹', '🐭🐷🐸🙉🐶', '🌌🌠🌉🌆🌃', '🕊️🦅🐦🦥🦏', '🐲🦖🐢🦮🐈', '🐐🦬🐖🐑🐆', '🦍🦧🐿️🦦🦈', '🐝🐠🐋🦋🐜', '🍔🍖🍗🌭🥪', '🥞🍳🫓🌮🍕', '🍉🍓🍒🫐🍎', '🧆🥙🥘🍜🦪', '🍧🍱🥟🍚🍢', '🍰🍙🍡🍣🍟', '🧇🥯🌯🥟🥡', '🍭🍩🍪🥮🍨', '🥗🍲🫕🍥🍿', '🥃🍾🍹🍸🍻', '🅿️🅾️🆘ℹ️🖕🏿', '🤏✋👊🙌👇', '👾🕹️🎮🎲🃏', '💵💴💶💷💰', '🇺🇸🇹🇨🇸🇻🇺🇦🇼🇸', '🏤🏣🏨🏥🏩']
	data.subClient.send_message(data.chatId, message=str(random.choice(lis)))

@client.command("fancytext")
def fancytext(data):
	msg = data.message + " null "
	msg = msg.split(" ")
	msg[1] = msg[0]
	data.subClient.send_message(data.chatId, message=fancy.light(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.bold(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.box(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.sorcerer(msg[1]))


@client.command("reboot")
def reboot(data):
    data.subClient.send_message(data.chatId, "Перезапускаем бота!")
    os.execv(sys.executable, ["None", os.path.basename(sys.argv[0])])

@client.command("comment")
def comment_profile(data):
	data.subClient.comment(message="Роспись от https://youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ 😎 Желаю всего Лучшего!", userId=data.authorId)
	data.subClient.send_message(data.chatId, message="Бот оставил вам роспись на стене!")

@client.command("msgtypes")
def msgtypes(data):
	data.subClient.send_message(data.chatId, message="""
[BC]--MESSAGETYPES--
[C]0 - BASE
[C]1 - STRIKE
[C]50 - UNSUPPORTED_MESSAGE
[C]57 - REJECTED_VOICE_CHAT
[C]58 - MISSED_VOICE_CHAT
[C]59 - CANCELED_VOICE_CHAT
[C]100 - DELETED_MESSAGE
[C]101 - JOINED_CHAT
[C]102 - LEFT_CHAT
[C]103 - STARTED_CHAT
[C]104 - CHANGED_BACKGROUND
[C]105 - EDITED_CHAT
[C]106 - EDITED_CHAT_ICON
[C]107 - STARTED_VOICE_CHAT
[C]109 - UNSUPPORTED_MESSAGE
[C]110 - ENDED_VOICE_CHAT
[C]113 - EDITED_CHAT_DESCRIPTION
[C]114 - ENABLED_LIVE_MODE
[C]115 - DISABLED_LIVE_MODE
[C]116 - NEW_CHAT_HOST
[C]124 - INVITE_ONLY_CHANGED
[C]125 - ENABLED_VIEW_ONLY
[C]126 - DISABLED_VIEW_ONLY
""")

@client.command("text")
def say_text(data):
	data.subClient.send_message(data.chatId, message=data.message)

@client.command("profile")
def profileinfo(data):
	repa = data.subClient.get_user_info(data.authorId).reputation
	lvl = data.subClient.get_user_info(data.authorId).level
	crttime = data.subClient.get_user_info(data.authorId).createdTime
	followers = data.subClient.get_user_achievements(data.authorId).numberOfFollowersCount
	profilchange = data.subClient.get_user_info(data.authorId).modifiedTime
	commentz = data.subClient.get_user_info(data.authorId).commentsCount
	posts = data.subClient.get_user_achievements(data.authorId).numberOfPostsCreated
	followed = data.subClient.get_user_info(data.authorId).followingCount
	sysrole = data.subClient.get_user_info(data.authorId).role
	data.subClient.send_message(data.chatId, message=f"""
[C]Никнейм/Nickname: {data.author}
[C]Айди-Аккаунта/UserId: {data.authorId}
[C]Дата Создания Аккаунта/Account created time: {crttime}
[C]Последний раз профиль изменялся/Last time the profile was changed: {profilchange}
[C]Количество Репутации/Reputation number: {repa}
[C]Уровень Аккаунта/Account level: {lvl}
[C]Количество постов созданных в профиле/Number of posts created in the profile: {posts}
[C]Количество комментариев на стене профиля/Number of comments on the profile wall: {commentz}
[C]Количество людей на которых вы подписаны/The number of people you follow: {followed}
[C]Подписчики аккаунта/Account followers: {followers}
[C]Номер аккаунта в системе/Account number in system: {sysrole}
	""")

client.launch()
################################################commands/команды################################################
time.sleep(10)
print("Bot started")

#socket
def restart():
    while True:
        time.sleep(120)
        count = 0
        for i in threading.enumerate():
            if i.name == "restart_thread":
                count += 1
        if count <= 1:
            print("Restart")
            client.socket.close()
            client.socket.start()
