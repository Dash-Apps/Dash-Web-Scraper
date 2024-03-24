import requests


def get_general_data(url):
    req = requests.get(url)
    data = {"status code":req.status_code,"cookies":req.cookies}
    print(data)
get_general_data("http://www.google.com")