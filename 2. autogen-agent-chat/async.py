import asyncio
import time

async def brew_coffee():
    print("starting Brewing Coffee")
    await asyncio.sleep(3)  ##  3 minutes
    print("coffee ready") 

async def toast_bagel():
    print("Start Toasting bagel")
    await asyncio.sleep(2) # 2 minutes
    print("bagel ready") 

async def main():
    start = time.time()
    
    coffee = brew_coffee()
    # time.sleep(2)
    bagel= toast_bagel()
    
    result  = await asyncio.gather(coffee, bagel)
 
    end = time.time()
    
    print(coffee,bagel, f"time: {end - start:.2f}: minutes")
    
asyncio.run(main())
