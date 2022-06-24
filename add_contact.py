from telegram import Update
from telegram.ext import ContextTypes
import csv

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_contact = update.message.text
    i = new_contact.split('_')
    if len(new_contact) == 4:
        new_contact = [i[0][5:], i[1], i[2], i[3]]
        with open("phonebook.csv", mode = "a", newline = '', encoding='utf-8') as file:
            file_writer = csv.writer(file, delimiter = "_")
            file_writer.writerow(new_contact)
        await update.message.reply_text(f'новый контакт добавлен')
    else: await update.message.reply_text(f'неправельно введен новый контакт')