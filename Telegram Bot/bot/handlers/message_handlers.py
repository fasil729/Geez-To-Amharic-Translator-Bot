from aiogram import types
from ..keyboards.keyboard import reply_keyboard, cancel_keyboard, inline_reply
from utils.feedbackState import FeedbackState
from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext 
from aiogram.filters import Command


message_router = Router()

@message_router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Welcome to the Translation Bot! Use the commands below:", reply_markup=reply_keyboard)

@message_router.message(lambda message: message.text.lower() == "geez to amharic")
async def geez_to_amharic_command(message: types.Message):
    await message.answer("You selected Geez to Amharic. Redirecting to the Geez to Amharic web app.", reply_markup=reply_keyboard)
    # Add logic to redirect to Geez to Amharic web app

@message_router.message(lambda message: message.text.lower() == "english to amharic")
async def english_to_amharic_command(message: types.Message):
    await message.answer("You selected English to Amharic. Redirecting to the English to Amharic web app.", reply_markup=reply_keyboard)
    

@message_router.message(lambda message: message.text.lower() == "help")
async def help_command(message: types.Message):
    help_text = (
        "Here is some help information:\n\n"
        "Use the buttons below for different actions:\n"
        "➡️ Use 'Geez To Amharic' button for Geez to Amharic Translation.\n"
        "➡️ Use 'English To Amharic' button for English to Amharic Translation.\n"
        "➡️ Use 'Give Feedback' button to provide feedback on the Bot and Translation Performance."
    )
    await message.answer(help_text, reply_markup=reply_keyboard)
  

@message_router.message(lambda message: message.text.lower() == "give feedback")
async def give_feedback_command(message: types.Message, state: FSMContext):
    await message.answer("Thank you for your Willngness to give us feedback Enter your name,  you can cancel if you want to cancel", reply_markup=cancel_keyboard)
    await state.set_state(FeedbackState.get_username)

@message_router.message(lambda message: message.text.lower() == "inline buttons")
async def switch_to_inline(message: types.Message, state: FSMContext):
    await message.answer("Use inline buttons", reply_markup=inline_reply)
    await state.set_state(FeedbackState.get_username)


