import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from aiogram_dialog import setup_dialogs
from environs import Env

from tgbot.handlers.user import router as user_router
from tgbot.dialogs import dialogs_list


env = Env()



async def main() -> None:
    bot: Bot = Bot(
        token=env.str("BOT_TOKEN"),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
    dp: Dispatcher = Dispatcher(storage=MemoryStorage())
    
    dp.include_routers(
        user_router,
        *dialogs_list
    )
    
    setup_dialogs(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())