from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7016432253:AAE8Klg4sPgu3IAVuTsK4Z2eFXB5c51c1p4'
BOT_USERNAME: Final = '@ramalakshmanan_bot'

async def start_command(upadte: Update, context: ContextTypes.DEFAULT_TYPE):
    await upadte.message.reply_text("Hello!, Thanks for Connecting")

async def help_command(upadte: Update, context: ContextTypes.DEFAULT_TYPE):
    await upadte.message.reply_text("Please type something")

async def custom_command(upadte: Update, context: ContextTypes.DEFAULT_TYPE):
    await upadte.message.reply_text("Custom MSG")


# Handle response

def handle_response(text: str):
    processed:str = text.lower()
    if 'hello' in processed:
        return 'Hey Here!'

    if 'how are you' in processed:
        return 'I am good'

    return 'I cannot Understand you'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}:"{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response:str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(upadte: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {upadte} caused error {context.error}')


if __name__ == '__main__':
    print("start")
    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))


    app.add_error_handler(error)

    print("polling")
    app.run_polling(poll_interval=2)