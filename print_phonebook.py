from telegram import Update
from telegram.ext import ContextTypes
from from_phonebook import read_pb

async def print_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pb = read_pb()
    count = 0
    await update.message.reply_text(f'№ имя фамилия телефон комментарий')
    for i in pb:
        firstname = i[0]
        secondname = i[1]
        tel_num = i[2]
        comment = i[3]
        await update.message.reply_text(f'{count} {firstname} {secondname} {tel_num} {comment}')
        count += 1