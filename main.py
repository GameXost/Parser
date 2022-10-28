from bs4 import BeautifulSoup as bs
import requests
import time

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.95'}
page = 1


def get_url():
    for page in range(1, 8):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={page}"
        page += 1
        resp = requests.get(url)
        soup = bs(resp.text, 'lxml')
        all_cards = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

        for card in all_cards:
            card_url = 'https://scrapingclub.com' + card.find('a').get('href')
            yield card_url


for card_url in get_url():
    resp = requests.get(card_url)
    time.sleep(2)
    soup = bs(resp.text, 'lxml')
    name = soup.find('h3', class_='card-title').text
    price = soup.find('h4').text
    txt = soup.find('p', class_='card-text').text
    url_img = soup.find('img').get('src')
    print(name, price, txt, 'https://scrapingclub.com' + url_img, sep='\n', end='\n\n')

