from aiogram_dialog import DialogManager

async def error_text_getter(dialog_manager: DialogManager, **kwargs):
    is_error_text = dialog_manager.dialog_data.get("is_error_text")
    
    return {"is_error_text": is_error_text}
