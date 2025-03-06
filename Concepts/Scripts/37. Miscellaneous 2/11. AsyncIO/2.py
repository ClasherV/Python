import asyncio
async def function1():
    await asyncio.sleep(1)
    print("Function 1")
    return "Ada"
async def function2():
    await asyncio.sleep(1)
    print("Function 2")
async def function3():
    await asyncio.sleep(4)
    print("Function 3")
async def main():
    L=await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print(L)
asyncio.run(main())

"""
O/p: Function 1
     Function 2
     Function 3
     ['Ada', None, None]
"""