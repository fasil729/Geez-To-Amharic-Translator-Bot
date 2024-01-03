from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.types.web_app_info import WebAppInfo


# Callback data for handling inline keyboard buttons
class ActionCallback(CallbackData, prefix="action"):
    command: str


# Inline keyboard with command buttons
reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [ 
            KeyboardButton(text="Geez To Amharic", callback_data=ActionCallback(command="geez_to_amharic").pack(), web_app=WebAppInfo(url="https://https-github-com-fasil729-geez-to-amharic-translator-bot.vercel.app/")),
            KeyboardButton(text="English To Amharic", callback_data=ActionCallback(command="english_to_amharic").pack(), web_app=WebAppInfo(url="https://translate.yandex.ru/")),
        ], 
        [
            KeyboardButton(text="Help", callback_data=ActionCallback(command="help").pack()),
            KeyboardButton(text="Give Feedback", callback_data=ActionCallback(command="give_feedback").pack()),
        ],
        [
            KeyboardButton(text="Inline Buttons", callback_data=ActionCallback(command="inline").pack()),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Type here...",
    selective=True
)



# Inline keyboard with command buttons
inline_reply = InlineKeyboardMarkup(
    inline_keyboard=[
        [ 
            InlineKeyboardButton(text="Geez To Amharic", callback_data=ActionCallback(command="geez_to_amharic").pack(), web_app=WebAppInfo(url="https://https-github-com-fasil729-geez-to-amharic-translator-bot.vercel.app/")),
            InlineKeyboardButton(text="English To Amharic", callback_data=ActionCallback(command="english_to_amharic").pack(), web_app=WebAppInfo(url="https://translate.yandex.ru/")),
        ], 
        [
            InlineKeyboardButton(text="Help", callback_data=ActionCallback(command="help").pack()),
            InlineKeyboardButton(text="Give Feedback", callback_data=ActionCallback(command="give_feedback").pack()),
        ],

        [
            InlineKeyboardButton(text="KeyBoard Buttons", callback_data=ActionCallback(command="keyboard").pack()),
        ],
    ]
)

# Inline keyboard with command buttons
cancel_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [ 
            InlineKeyboardButton(text="Cancel", callback_data=ActionCallback(command="cancel").pack()),
        ]
    ]
)
