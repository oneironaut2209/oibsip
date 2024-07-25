import tkinter as tk
from tkinter import ttk
from weather_data import WeatherData


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.api_key = "API_KEY_HERE"
        self.weather_data = WeatherData(self.api_key)

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.temperature_unit = tk.StringVar(value="metric")

        self.setup_ui()

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)

        self.location_entry = ttk.Entry(main_frame, width=25, font=("Helvetica", 14))
        self.location_entry.grid(row=0, column=0, padx=10, pady=10)

        self.search_button = ttk.Button(
            main_frame, text="Get Weather", command=self.get_weather
        )
        self.search_button.grid(row=0, column=1, padx=10, pady=10)

        self.unit_label = ttk.Label(main_frame, text="Unit:")
        self.unit_label.grid(row=0, column=2, padx=(20, 5), pady=10)

        self.unit_combobox = ttk.Combobox(
            main_frame,
            textvariable=self.temperature_unit,
            values=["metric (°C)", "imperial (°F)"],
            state="readonly",
            width=12,
        )
        self.unit_combobox.grid(row=0, column=3, padx=(5, 20), pady=10)
        self.unit_combobox.current(0)  # Default to Celsius

        self.weather_frame = ttk.Frame(main_frame, padding="10 10 10 10")
        self.weather_frame.grid(row=1, column=0, columnspan=4, sticky=(tk.W, tk.E))

        self.weather_label = ttk.Label(
            self.weather_frame, text="Weather Info", font=("Helvetica", 16)
        )
        self.weather_label.pack(pady=(0, 10))

        self.weather_icon = ttk.Label(self.weather_frame)
        self.weather_icon.pack()

        self.weather_details = ttk.Label(
            self.weather_frame, text="", font=("Helvetica", 12)
        )
        self.weather_details.pack()

    def get_weather(self):
        location = self.location_entry.get()
        unit = self.temperature_unit.get().split()[0]
        if location:
            data = self.weather_data.fetch_weather(location, unit)
            if data and data["cod"] == 200:
                self.update_ui(data, unit)
            else:
                self.weather_details.config(text="Location not found.")
                self.weather_icon.config(image="")
        else:
            self.weather_details.config(text="Please enter a location.")

    def update_ui(self, data, unit):
        weather = data["weather"][0]
        main = data["main"]
        icon_id = weather["icon"]
        description = weather["description"]
        temp = main["temp"]
        feels_like = main["feels_like"]
        humidity = main["humidity"]
        wind_speed = data["wind"]["speed"]

        unit_symbol = "°C" if unit == "metric" else "°F"
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
        icon_img = self.weather_data.fetch_icon(icon_url)
        self.weather_icon.image = icon_img
        self.weather_icon.config(image=self.weather_icon.image)

        weather_info = (
            f"Description: {description.capitalize()}\n"
            f"Temperature: {temp}{unit_symbol}\n"
            f"Feels Like: {feels_like}{unit_symbol}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )

        self.weather_details.config(text=weather_info)


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
