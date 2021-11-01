from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""ℌ𝔦,👋 {message.from_user.first_name}!
\n★  🎀  𝒯𝒽𝒾𝓈 𝒾𝓈 𝒜𝓇𝓂𝓎 𝐵❁𝓉 𝒞𝑅𝐸𝒜𝒯𝐸𝒟 𝐵𝒴 @projectking.
𝐼 𝓅𝓁𝒶𝓎 𝓂𝓊𝓈𝒾𝒸 ❀𝓃 𝒯𝑒𝓁𝑒𝑔𝓇𝒶𝓂'𝓈 𝒱❀𝒾𝒸𝑒 𝒞𝒽𝒶𝓉𝓈.  🎀  ★
\nFo More Help Use Buttons Below:
 """,
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                 [
                    InlineKeyboardButton(
                        "𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐥𝐢𝐬𝐭📒", url="https://telegra.ph/Commands-for-army-music-11-01")
                  ],[
                    InlineKeyboardButton(
                        "𝐎𝐰𝐧𝐞𝐫🧑🏻‍💻", url="https://t.me/projectking")
                  ][
                    InlineKeyboardButton(
                        "𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐠𝐫𝐨𝐮𝐩", url="https://t.me/Worldwide_friends_chatting_zonee")
                ],[
                    InlineKeyboardButton(
                        "➕𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩➕", url="https://t.me/Armymusic127_bot?startgroup=true")
                  ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""★  🎀  𝒯𝒽𝒾𝓈 𝒾𝓈 𝒜𝓇𝓂𝓎 𝐵❁𝓉 𝒞𝑅𝐸𝒜𝒯𝐸𝒟 𝐵𝒴 @projectking.
𝐼 𝓅𝓁𝒶𝓎 𝓂𝓊𝓈𝒾𝒸 ❀𝓃 𝒯𝑒𝓁𝑒𝑔𝓇𝒶𝓂'𝓈 𝒱❀𝒾𝒸𝑒 𝒞𝒽𝒶𝓉𝓈.  🎀  ★""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐠𝐫𝐨𝐮𝐩", url="https://t.me/Worldwide_friends_chatting_zonee")
                ] [
                    InlineKeyboardButton(
                        "𝐎𝐰𝐧𝐞𝐫🧑🏻‍💻", url="https://t.me/projectking")
                ]
            ]
        )
   )
