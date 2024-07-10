from aiogram import Bot, Dispatcher, types, Router
from aiogram.enums import ParseMode
from database.db_handlers import Database
from aiogram.client.default import DefaultBotProperties


dp = Dispatcher()
db = Database()
TOKEN = '6450010593:AAF2x15EoyvML4mLFnikZkBQ6uB4BgSW9Dw' #getenv("BOT_TOKEN") # .env faylidan tokenni o'qish
PROVIDER_TOKEN_CLICK = "398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065"
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
router = Router()
dp.include_router(router)
