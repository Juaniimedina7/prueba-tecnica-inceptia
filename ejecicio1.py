'''
Completar el método is_hot_in_pehuajo con el siguiente objetivo:

~ Consultar la información de clima y devolver True si la temperatura actual
supera los 28 grados celsius o False caso contrario. Esto implica incluso
devolver False ante cualquier excepción http.

Información extra:
API Información de clima:

~ Link a documentacion: https://openweathermap.org/current#geo

'''

import requests

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

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