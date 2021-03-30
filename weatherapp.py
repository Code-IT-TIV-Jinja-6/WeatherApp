from tkinter import *
# importing tkinter python gui library
import requests
# importing python http requests library
import tkinter.messagebox

# importing tkinter message box for easy dialog box creation

base = Tk()
base.title("Group 6 Weather App")


def weather_response_format(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = int(weather['main']['temp'] - 273)  # fetching the temp and converting it to celsius from kelvin

        display_str = 'City: %s \nConditions: %s \nTemperature(‎°C): %s ' % (name, desc, temp)  # formatting display string variable
    except:
        display_str = '''Sorry!
        The city could not be found, Please try again!'''  # error handling message

    return display_str


# function fetching weather

def get_weather(city):
    weather_key = '14ed2a78adcbcbfe1ac9d1ffb8c5eea6'  # api key we generated
    url = 'https://api.openweathermap.org/data/2.5/weather'  # opening url calling api
    params = {'APPID': weather_key, 'q': city}
    weather_response = requests.get(url, params=params)
    weather = weather_response.json()

    label['text'] = weather_response_format(weather)


# function for closing app via menu
def close_app():
    closeapp = tkinter.messagebox.askyesno("Group 6 Weather App", "Do you want to exit App?")
    if closeapp > 0:
        base.destroy()
        return


# additional function for displaying credits in menu
def credits_func():
    credits_func = tkinter.messagebox.showinfo(title="Credits", message='''Made with love by Group 6 CIT TIV
***Mohammed
***Alvin
***Hassan
***Moses
***Francis

GPL V4 License 2021''')
    return


# tkinter gui formatting

# basic canvas
HEIGHT, WIDTH = 600, 600
canvas = Canvas(base, height=HEIGHT, width=WIDTH)
canvas.pack()

# menu bars
menubar = Menu(base)
base.configure(menu=menubar)
submenu1 = Menu(menubar)
submenu2 = Menu(menubar)
menubar.add_cascade(label="File", menu=submenu1)
menubar.add_cascade(label="Help", menu=submenu2)

submenu1.add_command(label="Exit", command=close_app)
submenu2.add_command(label="About", command=credits_func)

# background image set
# background_image = PhotoImage(file="landscape4.png")
# background_label = Label(base, image=background_image)
# background_label.place(relwidth=1, relheight=1)

# frames
frame = Frame(base, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(frame, font=('Courier', 15))
entry.place(relwidth=0.65, relheight=1)

# search button
button = Button(frame, text="Get Weather", font=('Aria', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

# additional frame
lower_frame = Frame(base, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame, background="white", font=('Courier', 18))
label.place(relwidth=1, relheight=1)

base.mainloop()
