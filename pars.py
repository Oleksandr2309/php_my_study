import requests
page = requests.get('https://www.atbmarket.com/hot/akcii/economy')

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content)

def parse():
    global resultJson
    discounts = soup.find('ul', class_ = 'promo_list').find_all('li')
    resultJson = []
    
    for fc in discounts:
        resultJson.append({
            'productname': fc.find('span', class_='promo_info_text').get_text(strip=True).replace('/', ''),
            'oldprice': fc.find('span', class_='promo_old_price').get_text(strip=True),
            'newprice': fc.find('div', class_='promo_price').get_text(strip=True), #strip забирає всі відступи
            'discounts': fc.find('div', class_='economy_price').get_text(strip=True) #отримати текст цього тега з параметром strip=True
        })
        
    return resultJson
import json
with open('skidki.json', 'w') as file:
    json.dump(resultJson, file, indent=4)
    
parse()
