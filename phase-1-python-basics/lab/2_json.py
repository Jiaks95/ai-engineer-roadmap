import requests

def main():
    res = requests.get("https://jsonplaceholder.typicode.com/users/1")

    res_status_code = res.status_code

    if res_status_code != 200:
        print("Failed")
        return
    
    res_json = res.json()

    name = res_json["name"]
    city = res_json["address"]["city"]

    print(f"User's name: {name}")
    print(f"User's city: {city}")

if __name__ == "__main__":
    main()