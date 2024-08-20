from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo

from tgbot.states.user import WeatherSG


weather_dialog = Dialog(
    Window(
        Const(
            text='Щоб вибрати ваше місце проживання натисніть кнопку "🔎 Пошук"\n\n'
            'Також ви можете переглянути список збережених міст та сіл за допомогою кнопки "📝 Збереження".'
        ),
        SwitchTo(
            text=Const("🔎 Пошук"),
            id="search",
            state=WeatherSG.select_residence_st
        ),
        SwitchTo(
            text=Const("📝 Збереження"),
            id="save",
            state=WeatherSG.saved_st
        ),
        state=WeatherSG.weather_st,
    ),
)
