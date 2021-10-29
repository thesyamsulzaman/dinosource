import requests
from bs4 import BeautifulSoup

URL = 'https://dinosaurpictures.org'

def extract_data(content):
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, features="html.parser")
        dino_container = soup.find('div', { 'class' : 'dino-list' })
        dino_list = dino_container.find('ul', { 'class' : 'inline-list' })
        dinosaurs = dino_list.findChildren("h4")

        result = []
        for i in range(0, len(dinosaurs)):
            result.append(dinosaurs[i].a.text)

        # will be removed later
        result.pop()
        
        return result 
    else:
        return []

def get_dinosaurs_by_period(period):
    try:
        content = requests.get(f"{URL}/{period}-dinosaurs")
    except Exception:
        raise None

    return extract_data(content)

def get_dinosaurs():
    try:
        content = requests.get(f"{URL}/")
    except Exception:
        raise None

    return extract_data(content)

if __name__ == "__main__":
    dinosaurs = get_dinosaurs_by_period("jurassic")
    print(dinosaurs)

