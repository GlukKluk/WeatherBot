from .start.dialogs import start_dialog
from .weather.dialogs import weather_dialog

dialogs_list = [start_dialog, weather_dialog]

__all__ = ["dialogs_list"]
