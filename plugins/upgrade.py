from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GBGB
	Price 0
	
	**🪙 Basic** 
	Daily  Upload  limit 20GB
	Price Rs 49  ind /🌎 0.59$  per Month
	
	**⚡ Standard**
	Daily Upload limit 50GB
	Price Rs 99  ind /🌎 1.19$  per Month
	
	**💎 Pro**
	Daily Upload limit 100GB
	Price Rs 179  ind /🌎 2.16$  per Month
	
	
	Pay Using Upi I'd `9675208706@fam`
	
	After Payment Send Screenshots Of 
        Payment To Admin @itz_tusarr"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Admin",url = "https://t.me/itz_tusarr")], 
        			[InlineKeyboardButton("Phone Pay",url = "https://t.me/about_tosuu"),
        			InlineKeyboardButton("Paytm Wallet/UPI",url = "https://t.me/about_tosuu")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**🪙 Basic** 
	Daily  Upload  limit 20GB
	Price Rs 49  ind /🌎 0.59$  per Month
	
	**⚡ Standard**
	Daily Upload limit 50GB
	Price Rs 99  ind /🌎 1.19$  per Month
	
	**💎 Pro**
	Daily Upload limit 100GB
	Price Rs 179  ind /🌎 2.16$  per Month
	
	
	Pay Using Upi I'd `9675208706@fam`
	
	After Payment Send Screenshots Of 
        Payment To Admin @itz_tusarr"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Admin",url = "https://t.me/itz_tusarr")], 
        			[InlineKeyboardButton("Phone Pay",url = "https://t.me/about_tosuu"),
        			InlineKeyboardButton("Paytm Wallet/UPI",url = "https://t.me/about_tosuu")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
