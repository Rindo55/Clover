import asyncio
from main.modules.parser import auto_parser
from main import app
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
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
        source_text="https://da.gd/c7jivv"
        golink = "https://da.gd/t6Hh9"
        repl_markup=InlineKeyboardMarkup(

            [

                [

                     InlineKeyboardButton(

                        text="🚀GDrive",

                        url=source_text,

                    ),

                     InlineKeyboardButton(

                          text="🚀Worker",

                          url=golink,

                    ),

                ],

            ],

        )
        KAYO_ID = -1001159872623
        orgtext = f"**#Source_File**" + "\n" + f"**‣ File Name**: `Demon.Slayer.Kimetsu.no.Yaiba.Swordsmith.Village.Arc.S04E11.A.Connected.Bond.Daybreak.and.First.Light.1080p.CR.WEB-DL.AAC2.0.H.264.mkv`" + "\n" + "**‣ Video**: `1080p x264`" + "\n" + "**‣ Audio**: `Japanese`" + "\n" + f"**‣ Subtitle**: `Arabic, German, English, Spanish (Latin American), Spanish (European), French (France), Portuguese (Brazilian), Russian, Italian, Hindi`" + "\n" + f"**‣ File Size**: `2.9 GiB`" + "\n" + f"**‣ Duration**: 55 Minutes 29 Seconds" + "\n" + f"**‣ Downloads**: [🔗Google Drive]({source_text}) [🔗Worker]({golink})"
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
