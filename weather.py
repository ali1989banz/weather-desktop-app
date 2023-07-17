import requests
from tkinter import *
from tkinter import ttk


apikey="" # your api key here


window = Tk() # defined window
# window config :
screenWidth = 500
screenHeight = 500
window.geometry(f"{screenWidth}x{screenHeight}")
window.title("weather")
window.configure(bg="#845EC2")

# the form
title = Label(text="city :",bg="#845EC2",fg="#fff")
city = Entry(window,width=20)
title.pack(anchor=CENTER,pady=[20,0])
city.pack(pady=5)

def get_weather():
# request the data from api
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city.get()}&appid={apikey}'
    res=requests.get(url.format(city.get(),apikey))

    tField.config(state=NORMAL)
    tField.delete("1.0","end")
# get response
    if res:
        jsonData = res.json()
        rescity=jsonData['name']
        country=jsonData['sys']['country']
        temp=jsonData['main']['temp']
        temp_c=(temp - 273.15)
        description=jsonData['weather'][0]['description']      
        # get data to client  
        weather = f"\ncity: {rescity}\ncountry: {country}\ntemperature: {int(temp_c)}\ndescription: {description}"
    else:
        return None
    # show data on the window
    tField.insert(INSERT,weather)
    tField.config(state=DISABLED)


 
# submit request button
B = Button(window,name="get weather",text="get weather",bg="#000",fg="#fff" ,activebackground="#2C73D2",activeforeground="#fff", cursor="arrow",relief="flat", command=get_weather)
B.pack()

# data show :
tField_border = Frame(width=1,background="#845EC2")
tField = Text(window,width=40,height=10,bg="#845EC2",fg="#fff",highlightthickness=0)
tField.pack()
tField.config(state=DISABLED)

# footer
footer = Label(window,text="copyright 2023 powered by Ali Albhrany and Stone",bg="#845EC2",fg="#fff").place(x=screenWidth/2-150,y=screenHeight-20)

# update frames of window
if __name__ == "__main__":
    window.mainloop()
