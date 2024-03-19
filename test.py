import requests
def main():
    return requests.get(url="https://coolmathgames.com").text
print(main())