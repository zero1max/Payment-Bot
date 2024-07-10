from aiogram import  F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, LabeledPrice, ShippingQuery, PreCheckoutQuery
from loader import router, dp, bot ,PROVIDER_TOKEN_CLICK
from keyboards.defoult_keyboards.menu_keyboard import *
from keyboards.inline_keyboards.payment_keyboard import buy_item_btn
from product.product_data import iphone 
from product.delivery_option import FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING

ADMIN = 5471452269

@router.message(CommandStart())
async def start_handler(msg: Message):
    if msg.from_user.id == ADMIN:
        await msg.answer('Siz adminsiz', reply_markup=add)
    await msg.answer(f"Salom{msg.from_user.full_name}", reply_markup=menu_btn)


@router.message(F.text=="menu")
async def menu_handler(msg:Message):
    await msg.answer_photo(photo=iphone["photo"],
                           caption=f"<b>{iphone["title"]}</b>\n{iphone["description"]}",
                           reply_markup=buy_item_btn)



@router.callback_query(F.data.startswith("buy:"))
async def buy_handler(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,#foydalanuvchi id'si
                           title=iphone["title"],
                           description=iphone["description"],
                           payload="iphone:15:pro",
                           provider_token=PROVIDER_TOKEN_CLICK,
                           currency="UZS",
                           prices=[LabeledPrice(label=iphone["title"],
                                                amount=iphone["price"]*100)
                                   ],
                           photo_url=iphone["photo"],
                           photo_height=1280,
                           photo_width=1920,
                           need_name=True,
                           need_phone_number=True,
                           need_shipping_address=True,
                           is_flexible=True
                           )

@router.shipping_query()
async def shipping_query_handler(query:ShippingQuery ):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Biz faqat O'zbekiston uchun yetkazib bera olamiz!")
    elif  query.shipping_address.city.lower()=='tashkent' or 'toshkent' or 'toshken':
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True
                                        )
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True
                                        )
       
@router.pre_checkout_query()
async def pre_ch_q_handler(pre_checkout_query: PreCheckoutQuery ):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Xaridingiz uchun raxmat!")

