from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


# Callback data for handling inline keyboard buttons
class ActionCallback(CallbackData, prefix="action"):
    command: str


# Inline keyboard with command buttons
commands_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [ 
            InlineKeyboardButton(text="All Users", callback_data=ActionCallback(command="all_users").pack()),
            InlineKeyboardButton(text="Add User", callback_data=ActionCallback(command="add_user").pack()),
        ], 
        [
            InlineKeyboardButton(text="Get User by ID", callback_data=ActionCallback(command="get_user_by_id").pack()),
            InlineKeyboardButton(text="Update User", callback_data=ActionCallback(command="update_user").pack()),
            InlineKeyboardButton(text="Delete User", callback_data=ActionCallback(command="delete_user").pack()),
        ],
    ]
)
