import tkinter as tk
from urllib import response
import requests
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Weather Forecast")
root.geometry("600x500")

# a0a49505b18a04e30c75e58d4fa79fc6
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s\nCondition: %s\nTemperature: %s'%(city, condition, temp)
    except:
        final_str='There is a problem in retrieving the information'
    return final_str

def weather_result(city):
    weather_key = 'a0a49505b18a04e30c75e58d4fa79fc6'
    url ='https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city, 'units': 'imperial'}
    response=requests.get(url,params)
    weather = response.json()

   #print(weather['name'])
    #print(weather['weather'][0]['description'])
   # print(weather['main']['temp']) 

    result['text'] = format_response(weather)
    icon_weather = ['weather'][0]['icon']
    open_name(icon_weather)

def open_name(icon_weather):
    size =int(frame_two.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+ icon +'.png').resize((size, size)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0,anchor='nw', image=img)
    weather_icon.image =img


img = Image.open('./bg.png')
img = img.resize((600,500),Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)

bg_lbl = tk.Label(root, image=img_photo)
bg_lbl.place(x=0, y=0, width =600, height =500)

head_title = tk.Label(bg_lbl, text='Earth including 200,000 cities!',fg="red", bg='sky blue', font=('times new roman', 14, 'bold'))
head_title.place(x=90, y=18 )

frame_one = tk.Frame(bg_lbl, bg ="#42c2f4", bd =5)
frame_one.place(x=80, y=50, width =450, height =50)

txt_box = tk.Entry(frame_one, font =('times new roman', 25), width =17)
txt_box.grid(row=0, column=0, sticky='w')

btn = tk.Button(frame_one, text='Get weather', fg='green', font=('times new roman', 16, 'bold'), command=lambda: weather_result(txt_box.get()))
btn.grid(row=0, column=1, padx=10)

frame_two = tk.Frame(bg_lbl, bg ="#42c2f4", bd =5)
frame_two.place(x=80, y=130, width = 450, height =300)

result = tk.Label(frame_two, font =40, bg='white', justify='left', anchor='nw')
result.place(relheight=1, relwidth=1)

weather_icon = tk.Canvas(result, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=0.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()