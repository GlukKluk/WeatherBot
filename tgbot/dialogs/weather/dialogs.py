from aiogram.enums import ContentType

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo, Back
from aiogram_dialog.widgets.input import MessageInput

from tgbot.states.user import WeatherSG
from .handlers import residence_check
from .getters import error_text_getter


weather_dialog = Dialog(
    Window(
        Const(
            text='Щоб вибрати ваш населений пункт натисніть кнопку "🔎 Пошук"\n\n'
            'Також ви можете переглянути список збережених населених пунктів за допомогою кнопки "📝 Збереження".'
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
    Window(
        Const(
          text="Помилка! Назва населеного пункту невірна!",
          when="is_error_text"
        ),
        Const(
            text="Введіть назву населеного пункту:",
        ),
        MessageInput(
            func=residence_check,
            content_types=[ContentType.TEXT]
        ),
        Back(text=Const("⬅️ Назад")),
        getter=error_text_getter,
        state=WeatherSG.select_residence_st,
    ),
)
