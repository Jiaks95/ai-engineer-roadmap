import requests

def main():
    res = requests.get("https://api.github.com")

    res_code = res.status_code

    if res_code != 200:
        print("Failed")

    else:
        print("Success!")

if __name__ == "__main__":
    main()