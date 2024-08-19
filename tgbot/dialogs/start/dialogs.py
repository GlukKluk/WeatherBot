from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const

from tgbot.states.user import StartSG

start_dialog = Dialog(
    Window(
        Const(
            text="Вітаю! 👋\n"
            "Я допоможу вам дізнатися інформацію про погоду.\n\n"
            "/weather — погода\n"
            "/help — допомога"
        ),
        state=StartSG.start_st,
    )
)
