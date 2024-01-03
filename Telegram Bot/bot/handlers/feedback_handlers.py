import uuid
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext 
from datetime import datetime
from utils.feedbackState import FeedbackState
from ..keyboards.keyboard import reply_keyboard, ActionCallback, inline_reply, cancel_keyboard
from aiogram.filters import Command


from database.services.feedback_services import (
    get_feedbacks,
    get_feedback_by_id,
    create_feedback,
    update_feedback,
    delete_feedback_by_id,
)

feedback_router = Router()

@feedback_router.message(FeedbackState.get_username)
async def get_user_name(message: types.Message, state: FSMContext):
    name = message.text
    await message.answer(f"Enter Your feedback message: \
                        you can cancel if you need to cancel", reply_markup=cancel_keyboard)
    await state.update_data(name=name)
    await state.set_state(FeedbackState.get_feedback)

@feedback_router.message(FeedbackState.get_feedback)
async def add_feedback(message: types.Message, state: FSMContext):
    try:
        new_feedback_id = str(uuid.uuid4())
        name = (await state.get_data()).get("name")
        username = message.from_user.username
        feedback = await create_feedback(new_feedback_id, userName=username, name=name, message=message.text, date=datetime.now())
        await message.answer(f"Feedback added:\n{feedback} with ID: {new_feedback_id} \
                             Thank You for your feedback!!!",  reply_markup=reply_keyboard)
    
    except Exception as e:
        await message.answer(f"Error: {e}",  reply_markup=reply_keyboard)
    finally:
        await state.clear()

@feedback_router.callback_query(ActionCallback.filter(F.command=="cancel"))
async def callback_cancel(callback_query: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.answer("Giving feedback cancelled", reply_markup=reply_keyboard)
    