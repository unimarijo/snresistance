# -*- coding: utf-8 -*-


from app import logging
from app import config as config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, InlineQueryHandler
from telegram import Bot
from app.commands.start import start as start_command
from app.commands.debug import debug as debug_command
from app.commands.communities import addcommunity as addcommunity_command
from app.commands.communities import removecommunity as removecommunity_command
from app.commands.channel import addchannel as addchannel_command
from app.commands.channel import initializechannel as initchannel_command
from app.query_handlers.callback import callback as callback_query
from app.query_handlers.inline import inline as inline_query
import logging


def bot_initialize():
    try:
        # noinspection PyShadowingNames
        botUpdater = Updater(config.botToken, workers=16)
        dp = botUpdater.dispatcher

        dp.add_handler(CommandHandler("start", start_command))
        dp.add_handler(CommandHandler("debug", debug_command))
        dp.add_handler(CommandHandler("addcommunity", addcommunity_command))
        dp.add_handler(CommandHandler("removecommunity", removecommunity_command))
        dp.add_handler(CommandHandler("addchannel", addchannel_command))
        dp.add_handler(MessageHandler(Filters.text, initchannel_command))
        dp.add_handler(CallbackQueryHandler(callback_query))
        dp.add_handler(InlineQueryHandler(inline_query))
        dp.add_error_handler(error_handler)

        botUpdater.start_polling(clean=True)

        return botUpdater
    except Exception as e:
        logging.critical("Exception has been occurred while trying to set up bot settings.", exc_info=True)
        return e


def bot_configuration():
    try:
        bot = Bot(config.botToken)

        return bot
    except Exception as e:
        logging.critical("Exception has been occurred while trying to set up bot settings.", exc_info=True)
        return e


def error_handler(bot, update, error):
    logging.error("Exception has been occurred while trying to execute update {0}. Error: {1}.".format(
        str(update), str(error)
    ))
