#(©) @dp_botz
# Please Don't remove Credit 😢 @dp_botz
import time, os
import logging
import logging.config
from aiohttp import web
from datetime import datetime
from pytz import timezone
from pyrogram.raw.all import layer
from configs import dp1
from dpbotz.untils.add import set_commands
from pyrogram import Client, __version__
from dpbotz.web_support import web_server

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
 

class Bot(Client):

    def __init__(self):
        super().__init__(
            "approver",
            api_id=dp1.API_ID,
            api_hash=dp1.API_HASH,
            bot_token=dp1.BOT_TOKEN,
            plugins=dict(root='dpbotz')
             )
    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username 
        if dp1.WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()
            bind_address = "0.0.0.0"
            await web.TCPSite(app, bind_address, dp1.PORT).start()
        logging.info(f"{me.first_name} ✅✅ BOT started successfully ✅✅")
        logging.info(dp1.LOGO)
        await set_commands(self)
        for id in dp1.ADMIN:
            try:
                await self.send_message(id, f"**__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")
            except: pass
        if dp1.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(dp1.LOG_CHANNEL, f"**__{me.mention} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!**\n\n📅 Dᴀᴛᴇ : `{date}`\n⏰ Tɪᴍᴇ : `{time}`\n🌐 Tɪᴍᴇᴢᴏɴᴇ : `Asia/Kolkata`\n\n🉐 Vᴇʀsɪᴏɴ : `v{__version__} (Layer {layer})`</b>")                                
            except:
                print("Pʟᴇᴀꜱᴇ Mᴀᴋᴇ Tʜɪꜱ Iꜱ Aᴅᴍɪɴ Iɴ Yᴏᴜʀ Lᴏɢ Cʜᴀɴɴᴇʟ")
    async def stop(self, *args):
      await super().stop()      
      logging.info("Bot Stopped 🙄")
        
bot = Bot()
bot.run()
