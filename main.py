from print_phonebook import print_all
from add_contact import add
from delete_contact import delete
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/print_all\nпоказать весь справочник\n\n/add имя_фамилия_номер_коментарий\nдобавить новый контакт\n\n/delete №\nудалить контакт с выбранным № (узнать № можно посмотрев весь справочник)')

app = ApplicationBuilder().token("YOUR TOKEN HERE").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("print_all", print_all))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("delete", delete))
app.run_polling()
