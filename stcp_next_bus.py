#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import urllib.request
from bs4 import BeautifulSoup

DEFAULT_LINE = 600
DEFAULT_STOP_CODE = 'ASZ2'

def get_next_bus(line, stop_code):
    try:
        html = urllib.request.urlopen(f'https://www.stcp.pt/pt/itinerarium/soapclient.php?codigo={stop_code}&linha={line}').read()
        bs = BeautifulSoup(html, 'html.parser')
        content = bs.find_all('tr', {'class': 'even'})[0].find_all('td')[-1].text
        if content == '':
            print(f' 🚌 {line} is arriving now ')
        else:
            print(f' 🚌 {line} in {content} ')
    except BaseException as err:
        print('🚌 is nowhere to be seen 😔')
 
if __name__ == '__main__':
    line = DEFAULT_LINE
    stop_code = DEFAULT_STOP_CODE

    if len(sys.argv) == 3:
        line = sys.argv[1]
        stop_code = sys.argv[2]

    get_next_bus(line, stop_code)
 