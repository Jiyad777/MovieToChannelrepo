from Script import script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.regex("FAST AND FURIOUS") | filters.regex("Fast And Furious") | filters.regex("fast and furious"))
async def fast(bot, msg):
    buttons = [[
        InlineKeyboardButton("Fast and furious", callback_data="tip2")
        ],[      
        InlineKeyboardButton("2001", callback_data="f2001"),
        InlineKeyboardButton("2003", callback_data="f2003"),
        InlineKeyboardButton("2006", callback_data="f2006"),
        InlineKeyboardButton("2009", callback_data="f2009")
        ],[
        InlineKeyboardButton("2011", callback_data="f2011"),
        InlineKeyboardButton("2013", callback_data="f2013"),
        InlineKeyboardButton("2015", callback_data="f2015"),
        InlineKeyboardButton("2017", callback_data="f2017")
        ],[
        InlineKeyboardButton("Fast And Furious Presents: Hobbs and Shaw", callback_data="f2019")
        ],[
        InlineKeyboardButton("F9 The Fast Saga", callback_data="f2021")
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await msg.reply_photo(
        photo="https://telegra.ph/file/8f74216a74c06f881a670.jpg",
        caption=script.FAST_FURI.format(msg.from_user.mention),
        reply_markup=reply_markup,
        parse_mode="html")

@Client.on_message(filters.regex("HOME ALONE") | filters.regex("Home alone") | filters.regex("Home Alone"))
async def home(bot, msg):
    buttons = [[
        InlineKeyboardButton("🏠 HOME ALONE 🏠", callback_data="tip2")
        ],[      
        InlineKeyboardButton("HA 1", callback_data="ha1"),
        InlineKeyboardButton("HA 2", callback_data="ha2"),
        InlineKeyboardButton("HA 3", callback_data="ha3")
        ],[
        InlineKeyboardButton("HA 4", callback_data="ha4"),
        InlineKeyboardButton("HA 5", callback_data="ha5"),
        InlineKeyboardButton("HA 6", callback_data="ha6")
        ],[
        InlineKeyboardButton('CLOSE 🗑', callback_data='close_data')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await msg.reply_chat_action("typing")
    await msg.reply_photo(
        photo="https://telegra.ph/file/8beaabbd30f4dbf084f4e.jpg",
        caption=script.HOME_ALONE.format(msg.from_user.mention),
        reply_markup=reply_markup,
        parse_mode="html")
@Client.on_message(filters.regex("VIKINGS") | filters.regex("vikings") | filters.regex("Vikings"))
async def vikings(bot, msg):
    buttons = [[
        InlineKeyboardButton("🌟 VIKINGS COLLECTION 🌟", callback_data="tip2")
        ],[      
        InlineKeyboardButton("❗️S 01❗️", callback_data="vk1"),
        InlineKeyboardButton("❕S 02❕", callback_data="vk2"),
        InlineKeyboardButton("❗️S 03❗️", callback_data="vk3")
        ],[
        InlineKeyboardButton("❕S 04❕", callback_data="vk4"),
        InlineKeyboardButton("❗️S 05❗️", callback_data="vk5"),
        InlineKeyboardButton("❕S 06❕", callback_data="vk6")
        ],[
        InlineKeyboardButton("❗️SEASON 06 [ PART B ]❗️", callback_data="vk7")
        ],[
        InlineKeyboardButton('CLOSE 🗑', callback_data='close_data')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await msg.reply_chat_action("typing")
    await msg.reply_photo(
        photo="https://telegra.ph/file/99ab7f0b438f320635db3.jpg",
        caption=script.VIKIN_GS.format(msg.from_user.mention),
        reply_markup=reply_markup,
        parse_mode="html")
  
@Client.on_message(filters.regex("MAHAAN") | filters.regex("mahaan") | filters.regex("Mahaan"))
async def mahaan(bot, msg):
    buttons = [[
        InlineKeyboardButton("🦋 MAHAAN MALAYALAM 🦋", url="https://t.me/lisamoviebot?start=DSTORE-NDFfNDRfLTEwMDE2NTc2MjkyODVfL2JhdGNo")
        ],[
        InlineKeyboardButton("TAMIL", url="https://t.me/lisamoviebot?start=DSTORE-NDVfNDhfLTEwMDE2NTc2MjkyODVfL2JhdGNo")
        ],[
        InlineKeyboardButton("‼️ ALERT ‼️", callback_data="alert")
        ],[
        InlineKeyboardButton("🌀 Jᴏɪɴ ᴄʜᴀɴɴᴇL 🌀", url="https://t.me/jkmoviestg")
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await msg.reply_sticker(
        sticker="CAACAgUAAxkBAAECGahiL6CDY53FYO4iRYXbu_ZXmtHvzAACLAUAAvv_KFQWafOBgNotdR4E",
        reply_markup=reply_markup
    )
@Client.on_message(filters.regex("JAN E MAN") | filters.regex("jan e man") | filters.regex("Jan e man") | filters.regex("Jan E Man"))
async def regex(bot, msg):
    buttons = [[
        InlineKeyboardButton("🔘 JAN E MAN 🔘", url="https://t.me/lisamoviebot?start=DSTORE-NDlfNTNfLTEwMDE2NTc2MjkyODVfL2JhdGNo")
        ],[
        InlineKeyboardButton("‼️ ALERT ‼️", callback_data="art")
        ],[
        InlineKeyboardButton("🌀 Jᴏɪɴ ᴄʜᴀɴɴᴇL 🌀", url="https://t.me/jkmoviestg")
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await msg.reply_sticker(
        sticker="CAACAgUAAxkBAAECGbViL-s5MJSgV4DmpZ0xG83RKZbdowAC2gQAAi5HqVR7BrHkcRQZ4B4E",
        reply_markup=reply_markup
    )
