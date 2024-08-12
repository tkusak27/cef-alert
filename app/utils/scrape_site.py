from bs4 import BeautifulSoup
import requests
from selenium import webdriver

def curl_page_text(url):
    return requests.get(url).text

def get_soup(page_text):
    return BeautifulSoup(page_text, features="html.parser")

def get_funds(soup):
    table = soup.find('table', {'id': 'exportable'})

    funds_data = {}

    for row in table.find('tbody').find_all('tr'):
        cells = row.find_all('td')
        fund_symbol = cells[1].text.strip()
        fund_data = {
            'Fund Name': cells[0].text.strip(),
            'Symbol': fund_symbol,
            'NAV': float(cells[2].text.strip()),
            'NAV Change': float(cells[3].text.strip()),
            'NAV YTD Return': float(cells[4].text.strip()),
            'Distribution Rate at NAV': float(cells[5].text.strip()),
            'MKT': float(cells[6].text.strip()),
            'MKT Change': float(cells[7].text.strip()),
            'MKT YTD Return': float(cells[8].text.strip()),
            'Distribution Rate at MKT': float(cells[9].text.strip()),
            'Premium/Discount': float(cells[10].text.strip())
        }

        funds_data[fund_symbol] = fund_data
    
    return funds_data