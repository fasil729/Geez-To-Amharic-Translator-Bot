from aiogram.fsm.state import StatesGroup, State

class FeedbackState(StatesGroup):
    get_username = State()
    get_feedback = State()