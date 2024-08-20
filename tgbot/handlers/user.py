from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from aiogram_dialog import DialogManager, StartMode

from tgbot.states.user import StartSG, WeatherSG


router = Router()


@router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(StartSG.start_st, mode=StartMode.RESET_STACK)


@router.message(Command("weather"))
async def weather(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(WeatherSG.weather_st, mode=StartMode.RESET_STACK)
