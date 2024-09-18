from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.kbd import Button

from tgbot.states.user import WeatherSG
   
    
async def back_to_weather(callback_query: CallbackQuery, widget: Button, diaolg_manager: DialogManager):
    await diaolg_manager.reset_stack()
    
    await diaolg_manager.start(state=WeatherSG.weather_st)
