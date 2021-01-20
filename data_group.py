import requests
from bs4 import BeautifulSoup as BS
from pymongo import MongoClient


def get_html(link):
    r = requests.get(link)
    if r.ok:
        return r.text
    else:
        print(r.status_code)



def get_data(html):
    soup = BS(html, 'lxml')
    divs = soup.find('div', class_='news-list-block main-block').find('ul', class_='news-list').find_all('li')
    for t in divs:
        title = t.find('article').find('div', class_='news-text').find('a', class_='news-title').text
        url = t.find('article').find('a').get('href')
        data = {'post': title,
                'link': url
        }
        write_db(data)


def write_db(data):
    client = MongoClient('localhost',27017)
    m_db = client['News']
    mycollection = m_db['Soccer']
    mycollection.insert_one(data)





def main():
    link = 'https://football24.ua/ru/novosti_futbola_tag2/'
    get_data(get_html(link))





if __name__ =='__main__':
    main()