from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format

from tgbot.states.user import ForecastSG
from .getters import weather_data_getter


forecast_dialog = Dialog(
    Window(
        Format(text="{weather_data[location][name]}"),
        getter=weather_data_getter,
        state=ForecastSG.current_st
    )
)