import requests

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

    @classmethod
    def is_hot_in_pehuajo(cls):
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}&units=metric"

            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temperature = data['main']['temp']

                if temperature >= 28:
                    return True
                else:
                    return False
            else:
                print(f"Error getting API response: {response.status_code}")
                return False
        except Exception as e:
            print("Error", e)
            return False

print(GeoAPI.is_hot_in_pehuajo())