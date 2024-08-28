from aiogram.types import Message

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from tgbot.states.user import ForecastSG
from infrastructure.api.weatherapi import WeatherApiSession


async def residence_check(message: Message, widget: MessageInput ,dialog_manager: DialogManager):
    query = WeatherApiSession()
    
    weather_data = await query.make_request(residence=message.text)
    
    if weather_data:
        await dialog_manager.start(state=ForecastSG.current_st, data={"weather_data": weather_data})
    else:
        dialog_manager.dialog_data.update(is_error_text=True)
    