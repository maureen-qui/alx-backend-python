#!/usr/bin/env python3
import asyncio
from typing import List

async def async_comprehension() -> List[float]:
    return [i async for i in async_generator()]
