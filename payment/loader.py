from aiogram import Bot, Dispatcher, types, Router
from aiogram.enums import ParseMode
from database.db_handlers import Database
from aiogram.client.default import DefaultBotProperties


dp = Dispatcher()
db = Database()
TOKEN = 'BOT_TOKEN' #getenv("BOT_TOKEN") # .env faylidan tokenni o'qish
PROVIDER_TOKEN_CLICK = "CLICK_TOKEN"
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
router = Router()
dp.include_router(router)
