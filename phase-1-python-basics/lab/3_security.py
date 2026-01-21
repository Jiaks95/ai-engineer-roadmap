import os
from dotenv import load_dotenv

def main():
    load_dotenv()

    api_key = os.getenv("WEATHER_API_KEY")

    if api_key:
        print(f"Success! Key loaded: {api_key[:4]}*******")

    else:
        print("Error: Key not find")

if __name__ == "__main__":
    main()