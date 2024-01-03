from aiogram import Bot, Dispatcher
import motor.motor_asyncio
from aiogram.fsm.storage.memory import MemoryStorage

from config import MONGO_URL



cluster = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
collection = cluster.Fasika.myCollection
