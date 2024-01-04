from aiogram.filters import Command
from aiogram import F, Router, types 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from ..keyboards.keyboard import ActionCallback, reply_keyboard, inline_reply, cancel_keyboard
from utils.feedbackState import FeedbackState
from aiogram.fsm.context import FSMContext 


callback_router = Router()


@callback_router.callback_query(lambda c: c.data.startswith("action_1"))
async def process_callback_respond_to_action1(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"you picked {callback_query.data}")

@callback_router.callback_query(lambda c: c.data.startswith("action_2"))
async def process_callback_respond_to_action1(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"you picked {callback_query.data}")


# @callback_router.callback_query(ActionCallback.filter(F.command=="geez_to_amharic"))
# async def geez_to_amharic_callback(callback_query: types.CallbackQuery):
#     await callback_query.answer()
#     await callback_query.message.answer("You selected Geez to Amharic. Redirecting to the Geez to Amharic web app.")
    

# @callback_router.callback_query(ActionCallback.filter(F.command=="english_to_amharic"))
# async def english_to_amharic_callback(callback_query: types.CallbackQuery):
#     await callback_query.answer()
#     await callback_query.message.answer("You selected English to Amharic. Redirecting to the English to Amharic web app.")
    

@callback_router.callback_query(ActionCallback.filter(F.command=="help"))
async def help_callback(callback_query: types.CallbackQuery):
    help_text = (
        "Here is some help information:\n\n"
        "Use the buttons below for different actions:\n"
        "➡️ Use 'Geez To Amharic' button for Geez to Amharic Translation.\n"
        "➡️ Use 'English To Amharic' button for English to Amharic Translation.\n"
        "➡️ Use 'Give Feedback' button to provide feedback on the Bot and Translation Performance."
    )
    await callback_query.message.answer(help_text, reply_markup=inline_reply)
    
    

@callback_router.callback_query(ActionCallback.filter(F.command=="give_feedback"))
async def give_feedback_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.answer("Thank you for your Willngness to give us feedback Enter your name, \
                                        you can cancel if you want to cancel", reply_markup=cancel_keyboard)
    await state.set_state(FeedbackState.get_username)

@callback_router.callback_query(ActionCallback.filter(F.command=="keyboard"))
async def switch_to_keyboard(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.answer("Use Keyboard", reply_markup=reply_keyboard)
