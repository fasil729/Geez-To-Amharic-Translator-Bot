import uuid
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext 
from datetime import datetime
from .userFormstate import UserFormState
from ..keyboards.keyboard import commands_keyboard, ActionCallback
from aiogram.filters import Command

from database.services.user_services import (
    get_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user_by_id,
)

message_router = Router()

@message_router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Welcome to the Bot! Use the commands below:", reply_markup=commands_keyboard)

@message_router.callback_query(ActionCallback.filter(F.command=="all_users"))
async def callback_all_users(callback_query: types.CallbackQuery):
    try:
        users = await get_users()
        await callback_query.message.answer(f"All Users:\n{users}",  reply_markup=commands_keyboard)
    except Exception as e:
        await callback_query.message.answer(f"Error: {e}",  reply_markup=commands_keyboard)

@message_router.callback_query(ActionCallback.filter(F.command=="add_user"))
async def callback_add_user(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter the user name:")
    await state.set_state(UserFormState.add)

@message_router.message(UserFormState.add)
async def add_user(message: types.Message, state: FSMContext):
    try:
        new_user_id = str(uuid.uuid4())
        user = await create_user(new_user_id, name=message.text, date=datetime.now())
        await message.answer(f"User added:\n{user} with ID: {new_user_id}",  reply_markup=commands_keyboard)
    except Exception as e:
        await message.answer(f"Error: {e}",  reply_markup=commands_keyboard)
    finally:
        await state.clear()

@message_router.callback_query(ActionCallback.filter(F.command=="get_user_by_id"))
async def callback_get_user_by_id(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter the user ID you want to retrieve:")
    await state.set_state(UserFormState.get)

@message_router.message(UserFormState.get)
async def retrieve_user_by_id(message: types.Message):
    try:
        user_id = message.text
        user = await get_user_by_id(user_id)
        await message.answer(f"User by ID {user_id}:\n{user}",  reply_markup=commands_keyboard)
    except ValueError:
        await message.answer("Invalid user ID. Please enter a valid numeric ID.",  reply_markup=commands_keyboard)
    except Exception as e:
        await message.answer(f"Error: {e}")

@message_router.callback_query(ActionCallback.filter(F.command=="update_user"))
async def callback_update_user(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter the user ID you want to update:")
    await state.set_state(UserFormState.update)

@message_router.message(UserFormState.update)
async def update_user_message(message: types.Message, state: FSMContext):
    try:
        user_id = message.text
        await message.answer(f"Enter new data for the user ID {user_id} in the format: key1=value1, key2=value2")
        await state.update_data(user_id=user_id)
        await state.set_state("waiting to update")
        
    except ValueError:
        await message.answer("Invalid user ID. Please enter a valid numeric ID.",  reply_markup=commands_keyboard)
        await state.clear()



@message_router.callback_query(ActionCallback.filter(F.command=="delete_user"))
async def callback_delete_user(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter the user ID you want to delete:")
    await state.set_state(UserFormState.delete)

@message_router.message(UserFormState.delete)
async def delete_user_by_id_message(message: types.Message, state: FSMContext):
    try:
        user_id = message.text
        result = await delete_user_by_id(user_id)
        if result:
            await message.answer(f"User with ID {user_id} deleted successfully.",  reply_markup=commands_keyboard)
        else:
            await message.answer(f"User with ID {user_id} not found.",  reply_markup=commands_keyboard)
    except ValueError:
        await message.answer("Invalid user ID. Please enter a valid numeric ID.",  reply_markup=commands_keyboard)
    except Exception as e:
        await message.answer(f"Error: {e}")
    finally:
        await state.clear()

@message_router.message()
async def update_user_data(message: types.Message, state: FSMContext):
    try:
        curr = await state.get_state()
        if curr == "waiting to update":
            user_id = (await state.get_data()).get("user_id")
            data = dict(item.split("=") for item in message.text.split(","))
            user = await update_user(user_id, **data)
            await message.answer(f"User updated:\n{user}",  reply_markup=commands_keyboard)
    except Exception as e:
        await message.answer(f"Error: {e}",  reply_markup=commands_keyboard)
    finally:
        await state.clear()

