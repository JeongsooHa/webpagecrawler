# parser.py
import requests
from bs4 import BeautifulSoup
import json
import os

# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('http://www.sdsaram.com/bbs/board.php?bo_table=board&sca=%EB%A0%8C%ED%8A%B8')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'li > div.wr-subject > a'
    )
#list-body > li:nth-child(1) > div.wr-subject > a

data = {}

with open(os.path.join(BASE_DIR, 'result.txt'), 'w') as f: 
    for title in my_titles:
        data[title.text] = title.get('href')
        f.write(title.text+'\n')
f.close
with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)

