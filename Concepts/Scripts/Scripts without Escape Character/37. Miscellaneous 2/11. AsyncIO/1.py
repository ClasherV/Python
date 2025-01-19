import asyncio
async def function1():
    await asyncio.sleep(1)
    print("Function 1")
async def function2():
    await asyncio.sleep(1)
    print("Function 2")
async def function3():
    await asyncio.sleep(4)
    print("Function 3")
async def main():
    task=asyncio.create_task(function1())
    await function2()
    await function3()
asyncio.run(main())

"""
O/p: Function 2
     Function 1
     Function 3
"""