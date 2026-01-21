from dotenv import load_dotenv
import os
import requests

def main():
    load_dotenv()

    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        print("Error: Key not found")
        return
    
    while True:
        city = input("City name: ").strip().title()

        res = fetch_weather_data(api_key, city)

        if not check_status_code(res.status_code):
            print("Invalid city.")
            continue

        res_json = res.json()

        show_weather(city, res_json)
        return
    
def fetch_weather_data(api_key, city):
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")

    return res

def check_status_code(code):
    if code != 200:
        return False
    
    else:
        return True
    
def show_weather(city, weather_data):
    print(f"Currently in {city}: {weather_data["main"]["temp"]}ºC with {weather_data["weather"][0]["description"]}.")

if __name__ == "__main__":
    main()