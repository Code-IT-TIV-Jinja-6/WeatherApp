from tkinter import *
import tkinter as tk
import requests
import json
import tkinter.messagebox
# import tinker as a whole and after import tkinter as tk
#added tkinter.message box for error handling display message
# adding functionality to our app

base = Tk()

# we configure our app title and dimensions and background colour
base.title("Weather App Group 6")
base.configure(bg="yellow")
base.geometry("780x480")
# configure our rows and columns
base.rowconfigure(0, minsize=50)
base.columnconfigure([0, 1, 2, 3, 4], minsize=4)


'''start our fields and labels which will be displaying
the data'''
# title labels
title_1 = Label(text="Group 6 Weather App", width=25, font=("bold", 30), bg="yellow")

title_2 = Label(text="Enter City name ", width=32, font=("italics", 15), bg="yellow")
# Search field and button in grid format
city_name = StringVar()
search_city = tk.Entry(textvariable=city_name, text="Search for city")


def search_weather():
    api_key = "14ed2a78adcbcbfe1ac9d1ffb8c5eea6"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_names = search_city.get()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_names

    # response

    response = requests.get(complete_url)
    x = response.json()

    try:
        if['cod'] != '400':
            y = x['main']
            temp_High = y['temp_max']
            temp_Low = y['temp_min']
            pressure_value = y['pressure']
            hum_value = y['humidity']

        z = x['weather']
        description_weather = z[0]['description']

        m = x['sys']
        country_detail = m['country']

        temp_high_rs.configure(text=temp_High)
        temp_low_rs.configure(text=temp_Low)
        pres_rs.configure(text=pressure_value)
        hum_rs.configure(text=hum_value)
        des_rs.configure(text=description_weather)
        coun_rs.configure(text=country_detail)

    except:   # if there errors this will be executed
        tkinter.messagebox.showinfo("Error","City not found")


button_search = tk.Button(text="Search", bg="white", command=search_weather)

##function for closing app via menu
def close_app():
    closeapp = tkinter.messagebox.askyesno("Group 6 Weather App", "Do you want to exit App?")
    if closeapp>0:
        base.destroy()
        return

##additional function for displaying credits in menu
def credits_func():
    credits_func = tkinter.messagebox.showinfo(title="Credits", message='''Made with love by Group 6 CIT TIV
***Mohammed
***Alvin
***Hassan
***Moses
***Francis

GPL V4 License 2021''')
    return


##tkinter gui formatting

##menu bars
menubar = Menu(base) 
base.configure(menu=menubar)
submenu1= Menu(menubar)
submenu2= Menu(menubar)
menubar.add_cascade(label="File", menu=submenu1)
menubar.add_cascade(label="Help", menu=submenu2)

submenu1.add_command(label="Exit", command=close_app)
submenu2.add_command(label="About", command=credits_func)

# temp output and label

temp_high = Label(text="Temp(high) :", width=20, font=("bold", 20), bg="yellow")
temp_high_rs = Label(text="", width=20, font=("bold", 20), bg="yellow")

temp_low = Label(text="Temp(low) :", width=20, font=("bold", 20), bg="yellow")
temp_low_rs = Label(text="", width=20, font=("bold", 20), bg="yellow")
# pressure label and fetched data
pres = Label(text="Pressure :", width=20, font=("bold", 20), bg="yellow")
pres_rs = Label(text="", width=20, font=("bold", 20), bg="yellow")
# humidity label and data
hum = Label(text="Humidity :", width=20, font=("bold", 20), bg="yellow")
hum_rs = Label(text="", width=20, font=("bold", 20), bg="yellow")

# description
desc = Label(text="Description :", width=20, font=("bold", 20), bg="yellow")
des_rs = Label(text="", width=20, font=("bold", 20), bg="yellow")
# country

coun = Label(text="Country :", width=20, font=("bold", 20), bg="yellow")
coun_rs = Label(text="", width=20, font=("bold", 20), bg="yellow")

# the grid lay out
title_1.grid(row=0, column=2)
title_2.grid(row=1, column=2)
search_city.grid(row=2, column=2)
button_search.grid(row=2, column=3)
temp_high.grid(row=3, column=2)
temp_high_rs.grid(row=3, column=3)
temp_low.grid(row=4, column=2)
temp_low_rs.grid(row=4, column=3)
pres.grid(row=5, column=2)
pres_rs.grid(row=5, column=3)
hum.grid(row=6, column=2)
hum_rs.grid(row=6, column=3)
desc.grid(row=7, column=2)
des_rs.grid(row=7, column=3)
coun.grid(row=8, column=2)
coun_rs.grid(row=8, column=3)
# to make the app run until its closed
base.mainloop()
