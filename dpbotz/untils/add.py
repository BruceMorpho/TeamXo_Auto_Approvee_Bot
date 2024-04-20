from pyrogram.types import BotCommand


# Commond Automatic Set 📐
#(©) @DPBOTZ Repo - https://github.com/DP-BOTZ/DP-DEVELOP-AUTO-ACCEPT-BOT 
# Please Don't Remove Credit 🙏
async def set_commands(app):
    DP = [
        BotCommand("start", "Check Bot Alive."),
        BotCommand("dpusers", "Total Users Check.(Aᴅᴍɪɴ Oɴʟʏ)"),
        BotCommand("broadcast", "Broadcast Massage Send All Users In Bot (Aᴅᴍɪɴ Oɴʟʏ)."),
        BotCommand("fd_broadcast", "Broadcast massage Forward Not Remove (Aᴅᴍɪɴ Oɴʟʏ)."),
        BotCommand("restart", "Restarts or re-deploys the server (Aᴅᴍɪɴ Oɴʟʏ).")
 
    ]
    await app.set_bot_commands(DP)
