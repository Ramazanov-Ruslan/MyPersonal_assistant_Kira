from typing import List
from aiogram import Router

from . import accounting

routers_list: List[Router] = [
    accounting.router,
]