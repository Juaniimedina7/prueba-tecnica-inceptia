import requests

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

    @classmethod
    def is_hot_in_pehuajo(cls):
        try:
            params ={
                "lat": cls.LAT,
                "lon": cls.LON,
                "appid": cls.API_KEY,
                "units": "metric" 
            }
            response = requests.get(cls.WEATHER_API_URL, params=params)
            response.raise_for_status()

            data = response.json()
            temperature = data['main']['temp']

            return temperature > 28
        except requests.exceptions.RequestException:
            return False
        except Exception as e:
            print("Error", e)
            return False

print(GeoAPI.is_hot_in_pehuajo())