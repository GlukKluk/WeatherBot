from aiogram_dialog import DialogManager


async def weather_data_getter(dialog_manager: DialogManager, **kwargs):
    weather_data = dialog_manager.start_data.get("weather_data")
    
    return {"weather_data": weather_data}