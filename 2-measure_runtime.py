#!/usr/bin/env python3
import asyncio
from typing import List

async def measure_runtime() -> float:
    start_time = asyncio.get_event_loop().time()
    
    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time

# Run the main coroutine if the script is executed
if __name__ == "__main__":
    asyncio.run(measure_runtime())
