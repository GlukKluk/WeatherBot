from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from aiogram_dialog import DialogManager

from tgbot.states.user import StartSG

router = Router()


@router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(StartSG.start_st)
    