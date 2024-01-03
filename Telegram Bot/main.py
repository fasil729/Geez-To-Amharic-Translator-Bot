import asyncio 

from aiogram import Dispatcher

from bot.bot_instance import bot
from bot.handlers.message_handlers import message_router
from bot.handlers.feedback_handlers import feedback_router
from bot.callbacks.callback import callback_router


def register_routers(dp: Dispatcher) -> None:
    """Registers routers"""

    dp.include_router(message_router)

    dp.include_router(feedback_router)

    # callback routers
    dp.include_router(callback_router)





async def main() -> None:
    """The main function which will execute our event loop and start polling."""
    try:
        dp = Dispatcher()

        print('Bot Starting....')
        register_routers(dp)
        print("Polling ....")
        
        await dp.start_polling(bot)
    except:
        print("Some error occurred")
    

if __name__ == "__main__":
    asyncio.run(main())