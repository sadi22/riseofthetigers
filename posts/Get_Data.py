import urllib, json

def get_data(url):
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data["data"]


def get_commentary(url):
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data["commentary"]