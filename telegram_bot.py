"""
@brief  Telegram bot used to upload media to NAS server.
"""
### Libraries
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

### Global variables
# API key provided by FatherBot
updater = Updater(null,
                  use_context=True)
  
### Functions

## Repliers
def start_reply(update: Update, context: CallbackContext):
    """_summary_
        Welcoming interaction between user-bot
    Args:
        update (Update): Calling event
        context (CallbackContext): Context where event occurs
    """
    update.message.reply_text(
        "¡Hola! Bienvenido al sistema de almacenamiento Jimeno, ¿que deseas hacer?\n")

def help_reply(update: Update, context: CallbackContext):
    """_summary_
        Auxiliary function displaying use cases
    Args:
        update (Update): Calling event
        context (CallbackContext): Context where event occurs
    """
    update.message.reply_text("Los comandos disponibles son los siguientes:\n" + 
        "1. /ayuda - Muestra los posibles comandos que soy capaz de entender\n" +
        "2. /guardar - Indicame que quieres guardar y yo me encargaré\n" + 
        "3. /mostrar - Si necesitas que te mande algun video o imagen que" + 
        " tengas guardado indícamelo\n")
#TODO

def store_reply(update: Update, context: CallbackContext):
    """_summary_

    Args:
        update (Update): Calling event
        context (CallbackContext): Context where event occurs
    """
    update.message.reply_text("¿Que necesitas que guarde? Puedes mandármelo\n")
    #TODO
    pass

def load_reply(update: Update, context: CallbackContext):
    """_summary_

    Args:
        update (Update): Calling event
        context (CallbackContext): Context where event occurs
    """
    #TODO
    pass

def display_reply(update: Update, context: CallbackContext):
    """_summary_

    Args:
        update (Update): Calling event
        context (CallbackContext): Context where event occurs
    """
    #TODO
    pass

def unknown_reply(update: Update, context: CallbackContext):
    """_summary_

    Args:
        update (Update): _description_
        context (CallbackContext): _description_
    """
    update.message.reply_text(
        "Si necesitas ayuda introduce '/ayuda'.\n" + 
        "No soy capaz de entender '%s', lo siento \U0001F605" 
        % update.message.text)
    #TODO
  
  
def unknown_text(update: Update, context: CallbackContext):
    """_summary_

    Args:
        update (Update): _description_
        context (CallbackContext): _description_
    """
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
    #TODO

## Handlers
updater.dispatcher.add_handler(CommandHandler('empezar', start_reply))
updater.dispatcher.add_handler(CommandHandler('ayuda', help_reply))
updater.dispatcher.add_handler(CommandHandler('guardar', store_reply))
updater.dispatcher.add_handler(CommandHandler('cargar', load_reply))
updater.dispatcher.add_handler(CommandHandler('mostrar', display_reply))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_reply))

# Filters out unknown commands
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown_reply))
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()
