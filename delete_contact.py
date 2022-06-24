from telegram import Update
from telegram.ext import ContextTypes
import csv
from from_phonebook import read_pb

async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pb = read_pb()
    contact_id = int(update.message.text[8:])
    with open("phonebook.csv", mode="w", encoding='utf-8') as file:
        file_writer = csv.writer(file)
    with open("phonebook.csv", mode="w", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter = "_", lineterminator="\r")
        pb.remove(pb[contact_id])
        for i in pb:
            file_writer.writerow(i)
    await update.message.reply_text(f'контакт удален')