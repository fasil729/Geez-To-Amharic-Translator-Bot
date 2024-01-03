from aiogram.fsm.state import StatesGroup, State

class UserFormState(StatesGroup):
    add = State()
    update = State()
    delete = State()
    get = State()

