import requests

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        complete_url = f"{self.base_url}?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(complete_url)
        if response.status_code == 200:
            return response.json()
        else:
            self.handle_error(response)
            return None

    def parse_data(self, data):
        main = data['main']
        weather_info = {
            "temperature": main['temp'],
            "humidity": main['humidity'],
            "pressure": main['pressure'],
            "description": data['weather'][0]['description'],
            "wind_speed": data['wind']['speed']
        }
        return weather_info

    def display_weather(self, info):
        print(f"Temperature: {info['temperature']}°C")
        print(f"Humidity: {info['humidity']}%")
        print(f"Pressure: {info['pressure']} hPa")
        print(f"Weather: {info['description']}")
        print(f"Wind Speed: {info['wind_speed']} m/s")

    def handle_error(self, response):
        if response.status_code == 404:
            print("City not found. Please try again.")
        elif response.status_code == 401:
            print("Invalid API key. Please check your API key.")
        else:
            print("An error occurred. Please try again.")

if __name__ == "__main__":
    api_key = "a8e83a3ab54af6c3d0c8541a22390992"  # Replace with your actual API key
    app = WeatherApp(api_key)
    city = input("Enter the city name: ")
    data = app.get_weather(city)
    if data:
        weather_info = app.parse_data(data)
        app.display_weather(weather_info)
