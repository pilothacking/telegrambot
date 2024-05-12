from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler, ContextTypes

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.messageS.reaply_text(f'''
Hello! {update.effective_user.first_name}
''')

async def contact(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.messageS.reaply_text(f'''
Dear, {update.effective_user.first_name}
this is my contact info.
''')

async def help(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.messageS.reaply_text(f'''
Dear, {update.effective_user.first_name}
how can i help you.
''')


app=ApplicationBuilder().token('your bot token').build()


start_handler=CommandHandler('start', start)
contact_handler=CommandHandler('contact', contact)
help_handler=CommandHandler('help', help)

app.add_handler(start_handler)
app.add_handler(contact_handler)
app.add_handler(help_handler)


app.run_polling()
