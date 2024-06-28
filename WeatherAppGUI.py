import json
import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext

class Weather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.baseurl = "https://api.openweathermap.org/data/2.5/weather?"

    def get_weather_data(self, city):
        complete_url = f"{self.baseurl}q={city}&APPID={self.api_key}&units=metric"
        response = requests.get(complete_url)
        return response.json()

class WeatherData:
    def __init__(self, data):
        self.city = data['name']
        self.temperature = data['main']['temp']
        self.weather_description = data['weather'][0]['description']
        self.humidity = data['main']['humidity']
        self.wind_speed = data['wind']['speed']

    def format_display(self):
        return f"City: {self.city}\nTemperature: {self.temperature}°C\nWeather: {self.weather_description}\nHumidity: {self.humidity}%\nWind Speed: {self.wind_speed} m/s"

class WeatherAppGUI:
    def __init__(self, master, api_key):
        self.master = master
        self.master.title("Weather App")
        self.weather_api = Weather(api_key)

        self.create_widgets()
        self.load_city_data()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enter city name:")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.search_button = tk.Button(self.master, text="Search", command=self.search_weather)
        self.search_button.pack()

        self.result_text = scrolledtext.ScrolledText(self.master, width=40, height=10)
        self.result_text.pack()

        self.cities_listbox = tk.Listbox(self.master, width=40)
        self.cities_listbox.pack()

        self.search_entry = tk.Entry(self.master)
        self.search_entry.pack()

        self.search_button = tk.Button(self.master, text="Search in Cities", command=self.search_city)
        self.search_button.pack()

    def load_city_data(self):
        try:
            with open('city.list.json', encoding='utf-8') as f:
                self.cities_data = json.load(f)
                # Check if self.cities_data is a list
                if isinstance(self.cities_data, list):
                    for city in self.cities_data:
                        self.cities_listbox.insert(tk.END, city)
                else:
                    messagebox.showerror("Error", "city.list.json file is not in expected format (should be a list of city names)!")

        except FileNotFoundError:
            messagebox.showerror("Error", "city.list.json file not found!")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Error decoding city.list.json file!")

    def search_city(self):
        search_term = self.search_entry.get().strip().lower()
        self.cities_listbox.delete(0, tk.END)
        if hasattr(self, 'cities_data'):
            for city in self.cities_data:
                if search_term in city.lower():
                    self.cities_listbox.insert(tk.END, city)

    def search_weather(self):
        city = self.entry.get().strip()
        weather_data = self.weather_api.get_weather_data(city)
        if weather_data['cod'] == 200:
            data = WeatherData(weather_data)
            display_text = data.format_display()
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, display_text)
        else:
            messagebox.showerror("Error", "City not found!")

def main():
    api_key = "your_api_key_here"
    root = tk.Tk()
    app = WeatherAppGUI(root, api_key)
    root.mainloop()

if __name__ == "__main__":
    main()
