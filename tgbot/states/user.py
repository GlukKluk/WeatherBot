from aiogram.fsm.state import State, StatesGroup


class StartSG(StatesGroup):
    start_st = State()