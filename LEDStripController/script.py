import cmdver
import asyncio

async def execute():
    await cmdver.handle_command("off")
    await cmdver.handle_command("off")
    await cmdver.handle_command("wait")
    await cmdver.handle_command("on")
    await cmdver.handle_command("wait")
    await cmdver.handle_command("off")
    await cmdver.handle_command("wait")
    await cmdver.handle_command("on")
    await cmdver.handle_command("wait")
    await cmdver.handle_command("quit")
