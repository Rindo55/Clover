import asyncio
from main.modules.parser import auto_parser
from main import app
from pyrogram import filters, idle
from pyrogram.types import Message
from uvloop import install
from contextlib import closing, suppress
from main.modules.tg_handler import tg_handler

loop = asyncio.get_event_loop()

@app.on_message(filters.command(["help","ping"]))
async def start(bot, message: Message):
  return await message.reply_text("⚡ **Bot Is up...**")

@app.on_message(filters.command(["send"]))
async def start(bot, message: Message):
        source_text="https://da.gd/KUOqvg"
        golink = "https://da.gd/XHf7sT"
        repl_markup=InlineKeyboardMarkup(

            [

                [

                     InlineKeyboardButton(

                        text="🐌TG FILE",

                        url=source_text,

                    ),

                     InlineKeyboardButton(

                          text="🚀GoFile",

                          url=golink,

                    ),

                ],

            ],

        )
        KAYO_ID = -1001159872623
        orgtext = f"**#Encoded_File**" + "\n" + f"**‣ File Name**: `Demon Slayer S4 - 11 [720p.x265] @animxt.mkv`" + "\n" + "**‣ Video**: `720p HEVC x265 10Bit`" + "\n" + "**‣ Audio**: `Japanese`" + "\n" + f"**‣ Subtitle**: `English`" + "\n" + f"**‣ File Size**: `252.7 MiB`" + "\n" + f"**‣ Duration**: 55 Minutes 29 Seconds" + "\n" + f"**‣ Downloads**: [🔗Telegram File]({source_text})"
        rep_id = 31516
        return await app.send_message(
              chat_id=KAYO_ID,
              text=orgtext,
              reply_markup=repl_markup,
              reply_to_message_id=rep_id
          )
async def start_bot():
  print("==================================")
  print("[INFO]: AutoAnimeBot Started Bot Successfully")
  print("==========JOIN @Latest_ongoing_airing_animes=========")

  print("[INFO]: Adding Parsing Task")
  asyncio.create_task(auto_parser())
  asyncio.create_task(tg_handler())
  
  await idle()
  print("[INFO]: BOT STOPPED")
  await app.stop()  
  for task in asyncio.all_tasks():
    task.cancel()

if __name__ == "__main__":
  install()
  with closing(loop):
    with suppress(asyncio.exceptions.CancelledError):
      loop.run_until_complete(start_bot())
      loop.run_until_complete(asyncio.sleep(3.0))
