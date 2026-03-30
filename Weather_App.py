import requests


API_KEY = "your_api_key_here"  # Replace with your real API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str, country: str) -> None:
    """
    Fetch and display weather data for a given city and country.

    Args:
        city (str): Name of the city.
        country (str): Country code (e.g., PK, US, UK).
    """
    query = f"{city},{country}" if country else city

    params = {
        "q": query,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)

        if response.status_code == 200:
            data = response.json()

            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            city_name = data["name"]
            country_code = data["sys"]["country"]

            print("\n🌍 Weather Details")
            print(f"City: {city_name}, {country_code}")
            print(f"Temperature: {temperature}°C")
            print(f"Feels Like: {feels_like}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {description.capitalize()}\n")

        elif response.status_code == 404:
            print("⚠️ City not found. Please check city and country code.")

        else:
            print(f"⚠️ Error: HTTP {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("⚠️ Network error. Check your internet connection.")

    except requests.exceptions.Timeout:
        print("⚠️ Request timed out. Try again later.")

    except requests.exceptions.RequestException as error:
        print(f"⚠️ Unexpected error: {error}")


def run_cli():
    """
    Run the Weather CLI application loop.
    """
    print("🌤️ Welcome to Weather CLI App")
    print("💡 Example: City = Karachi, Country = PK\n")

    while True:
        city = input("Enter city name (or 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("👋 Goodbye!")
            break

        if not city:
            print("⚠️ City cannot be empty.")
            continue

        country = input("Enter country code (optional, e.g., PK): ").strip()

        get_weather(city, country)


if __name__ == '__main__':
    run_cli()