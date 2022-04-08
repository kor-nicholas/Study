import csv
import json

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_html_and_save_in_file(url, number):
    ua = UserAgent()

    headers = {
        "Accept": "*/*",
        "User-Agent": ua.random
    }

    responce = requests.get(url, headers=headers)

    # была проблема с кодировками. не проверял, но могу предположить что поможет
    # такой вариант - сначала сохранить в кодировке utf-8, потом открывать либо
    # дозаписывать (a) в cp1251 кодировке
    with open(f"index{number}.html", "w", encoding='utf-8') as file:
        file.write(responce.text)

    return responce.text

def get_html_from_file(number):
    with open(f"index{number}.html", "r", encoding='cp1251') as file:
        return file.read()

def save_data_in_csv(data):
    # with open("data.csv", "w", encoding='cp1251', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(
    #         [
    #             "Название",
    #             "Категория",
    #             "Цена",
    #             "Страна/Город",
    #             "Ссылка",
    #             "Фото"
    #         ]
    #     )

    with open("data.csv", "a", encoding='cp1251', newline='') as file:
        writer = csv.writer(file)

        for card in data:
            writer.writerow(
                [
                    card['title'],
                    card['category'],
                    card['price'],
                    card['country_and_city'],
                    card['url'],
                    card['photo']
                ]
            )

def save_data_in_json(data):
    with open("data.json", "w", encoding='cp1251') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def parse(html):
    soup = BeautifulSoup(html, 'lxml')

    cards = soup.find_all('a', class_='kf-inA-612a7')

    data = []
         
    for card in cards:
        try:
            url = card['href'].strip()
            img = card.find('img', class_='kf-cfAm-0950b')
            photo = img['data-src']
            title = img['alt'].replace('\n', ' ')
            price = card.find('p', class_='kf-inAn-24154').text.strip()
            category = card.find('p', class_='kf-inJw-7fbe3 kf-inAx-c457f').text.strip()
            country_and_city = card.find('div', class_='kf-inJj-c4658').text.strip()

            data_local = {
                "title": title,
                "category": category,
                "price": price,
                "country_and_city": country_and_city,
                "url": url,
                "photo": photo
            }

            data.append(data_local)

        except:
            print("Error")
        
    return data




if __name__ == '__main__':
    html = get_html_and_save_in_file('https://www.kufar.by/l', 3)
    #html = get_html_from_file()
    data = parse(html)
    save_data_in_csv(data)
    save_data_in_json(data)


