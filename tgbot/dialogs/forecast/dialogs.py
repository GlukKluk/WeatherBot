from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, Cancel

from tgbot.states.user import ForecastSG
from .getters import weather_data_getter
from .handlers import back_to_weather


forecast_dialog = Dialog(
    Window(
        Format(
            text="<b>🏠 {weather_data[location][name]}</b>\n\n"
            "🌤️ Стан: {weather_data[current][condition][text]}\n"
            "🌡️ Температура: {weather_data[current][temp_c]}°C\n"
            "🌬️ Швидкість вітру: {weather_data[current][wind_kph]} км/год\n"
            "🌧️ Опади: {weather_data[current][precip_mm]} мм\n"
            "💧 Вологість: {weather_data[current][humidity]}%"
        ),
        Cancel(text=Const("🔎 Вибрати інший населений пункт")),
        Button(text=Const("⬅️ Назад"), id="back_to_weather", on_click=back_to_weather),
        getter=weather_data_getter,
        state=ForecastSG.current_st
    )
)