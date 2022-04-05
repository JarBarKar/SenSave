from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext import CallbackQueryHandler
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import telegram.bot
import pandas as pd
import datetime


updater = Updater("<TOKEN_ID>",
				use_context=True)
token = "<TOKEN_ID>"
chat_id = "<CHAT_ID>"

def returnDuration():
    data = pd.read_csv("elderlyHabits.csv")
    year =int(data["year"].tail(1))
    month =int(data["month"].tail(1))
    day =int(data["day"].tail(1))
    hour =int(data["hour"].tail(1))
    minute =int(data["minute"].tail(1))

    startTime = datetime.datetime(year, month, day, hour, minute, 0)
    durationDelta = datetime.datetime.now() - startTime
    durationDeltaSeconds = durationDelta.total_seconds()
    duration = round(durationDeltaSeconds/(60),2)
    #unit = minute
    return duration

def returnPerson():
    data = pd.read_csv("ownerVisitor.csv")
    personCount =int(data["personCount"].tail(1))
    elderly = data["elderly"].tail(1)
    return [elderly, personCount]

def returnLocation():
    data = pd.read_csv("elderlyHabits.csv")
    location =data["location"].tail(1).item()
    return location

def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)

def unique_visitors(update: Update, context: CallbackContext):
	number= returnPerson()[1]
	update.message.reply_text(f"This elderly has {int(number)} visitors this month.")

def where_is_elderly(update: Update, context: CallbackContext):
	location = returnLocation()
	duration = returnDuration()
	update.message.reply_text(
		f"Elderly is in {location} for {duration} min")


def profile(update: Update, context: CallbackContext):
	name = "Karen Thiam Siew Siew"
	age = 88
	illness = ["Arthritis", "Have history of falls", "Mild Dementia"]
	dietary = ["No seafood", "G6PD"]
	religion = "Buddist"
	update.message.reply_text(
		f"Name: {name}\nage: {age}\nillness: {','.join(illness)} \nDietary: {','.join(dietary)}\nreligion: {religion}")
	bot.send_document(chat_id="<CHAT_ID>", document=open("known_faces/elderly.jpg", 'rb'))

updater.dispatcher.add_handler(CommandHandler('profile',profile))
updater.dispatcher.add_handler(CommandHandler('where',where_is_elderly))
updater.dispatcher.add_handler(CommandHandler('unique', unique_visitors))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

bot = telegram.Bot(token=token)
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()

updater.idle()