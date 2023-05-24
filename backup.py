# Created on : May 16, 2023, 7:31:17 p.m.
# Author     : Phu Hoang


# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.

import python_weather

import asyncio
import os

async def getweather(city):
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  z=""
  async with python_weather.Client(unit=python_weather.METRIC) as client:
    # fetch a weather forecast from a city
    weather = await client.get(city)
    z = weather.current.description
  print(z)
    
    # returns the current day's forecast temperature (int)
    

if __name__ == '__main__':
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  
  asyncio.run(getweather("131434141244141414144"))
