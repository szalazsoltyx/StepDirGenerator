from machine import Pin , PWM
import time
import uasyncio as asyncio

led = Pin(15, Pin.OUT)

async def bar():
    for i in range(10):
        led(1)
        time.sleep_ms(500)
        led(0)
        time.sleep_ms(500)

async def main():
    for x in range(3):
        asyncio.create_task(bar())
    await asyncio.sleep(10)

asyncio.run(main())