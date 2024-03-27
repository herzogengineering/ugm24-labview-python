import pyowm


class WeatherFetcher():
    def __init__(self, api_key):
        self.owm = pyowm.OWM(api_key=api_key)

    def get_temperature(self, place='Zurich,CH') -> float:
        weather = self.owm.weather_manager().weather_at_place(place).weather
        return weather.temperature('celsius')['temp']


def api_get_weather_fetcher(api_key='df2de9553b5b1c9422f4472f594d78ea'):
    fetcher = WeatherFetcher(api_key)
    return fetcher


def api_get_temperature(fetcher, place='Zurich,CH'):
    return fetcher.get_temperature(place)


if __name__ == "__main__":
    api_key = 'df2de9553b5b1c9422f4472f594d78ea'

    # Create an instance of the Weather class
    weather_fetcher = api_get_weather_fetcher(api_key)

    print(weather_fetcher.get_temperature('Baden,CH'))
