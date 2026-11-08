import os
import json
import random
import string
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("BOT_TOKEN")
BOT_USERNAME = "Miuisafebot"
FILES_FILE = "files.json"

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

def load_files():
    try:
        with open(FILES_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_files(data):
    with open(FILES_FILE, "w") as f:
        json.dump(data, f)

def make_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if args:
        code = args[0]
        files = load_files()
        if code in files:
            file_id = files[code]
            await update.message.reply_document(document=file_id, caption="Ye lo tumhari file! ✅")
            return
    await update.message.reply_text("Hi! Mujhe koi file bhejo, mai uska link bana dunga.")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    file_id = None
    if msg.document:
        file_id = msg.document.file_id
    elif msg.photo:
        file_id = msg.photo[-1].file_id
    elif msg.video:
        file_id = msg.video.file_id
    elif msg.audio:
        file_id = msg.audio.file_id

    if not file_id:
        await msg.reply_text("Ye file nahi hai.")
        return

    files = load_files()
    code = make_code()
    files[code] = file_id
    save_files(files)
    link = f"https://t.me/{BOT_USERNAME}?start={code}"
    await msg.reply_text(f"Ho gaya! ✅\nTumhari file ka link:\n{link}")
async def main():
    threading.Thread(target=run_flask...
    ...
    asyncio.run(main())
