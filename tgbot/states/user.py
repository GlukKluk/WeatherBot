from aiogram.fsm.state import State, StatesGroup


class StartSG(StatesGroup):
    """
    First level: START MESSAGE
    """
    start_st = State()
    

class WeatherSG(StatesGroup):
    """
    Second level: WEATHER MENUE
    """
    weather_st = State()
    select_residence_st = State()
    saved_st = State()
    
    
class ForecastSG(StatesGroup):
    """
    Third level: FORECAST DATA
    """
    current_st = State()
    