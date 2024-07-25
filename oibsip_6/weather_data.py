import requests
from PIL import Image, ImageTk
import io

class WeatherData:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_weather(self, location, unit):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}&units={unit}"
        response = requests.get(url)
        return response.json()

    def fetch_icon(self, icon_url):
        icon_response = requests.get(icon_url)
        icon_img = Image.open(io.BytesIO(icon_response.content))
        icon_img = icon_img.resize((100, 100), Image.LANCZOS)
        return ImageTk.PhotoImage(icon_img)
