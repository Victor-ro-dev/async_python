import asyncio

async def say(what, when):
    print("say() called")
    await asyncio.sleep(when)
    print(f"{what}")


async def main():
    await asyncio.gather(say("hello", 1), say("world", 2))

asyncio.run(main())