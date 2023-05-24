# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.
from tkinter import *
import python_weather
from tkinter import messagebox

import asyncio
import os

async def getweather(city):
 z=""
 async with python_weather.Client(unit=python_weather.METRIC) as client:
   

   weather = await client.get(city)
   z=weather.current
 return z
 


def search():
 if(city_text.get().isalpha()):
  if __name__ == '__main__':
     if os.name == 'nt':
      asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
      
  city_weather = asyncio.run(getweather(city_text.get()))
  temp_lbl["text"] = "{:.2f}*C".format(city_weather.temperature)
  weather_lbl["text"] = "{}".format(city_weather.description)
  location_lbl["text"]="{}".format(city_text.get())
 else:
  messagebox.showerror("Error","Cannot find city {}".format(city_text.get()))
 


  


app=Tk()
app.title("Weather App")
app.geometry("600x480")

city_text = StringVar()
city_entry = Entry(app,textvariable=city_text)
city_entry.pack()



search_btn = Button(app,text="Search Weather",width=12,command=search)
search_btn.pack()

location_lbl = Label(app,text="Location",font=["bold",20])
location_lbl.pack()

image = Label(app,bitmap='')
image.pack()

temp_lbl = Label(app,text="Temperature")
temp_lbl.pack()

weather_lbl = Label(app,text="Weather")
weather_lbl.pack()

if __name__ == '__main__':
  app.mainloop()
  
  



  
  