# parser.py
import requests
from bs4 import BeautifulSoup
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","crawler_django.settings")

import django
django.setup()

from parsed_data.models import SDsaramData

def parse_blog():
    req = requests.get('http://www.sdsaram.com/bbs/board.php?bo_table=board&sca=%EB%A0%8C%ED%8A%B8')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'li > div.wr-subject > a'
        )
#list-body > li:nth-child(1) > div.wr-subject > a

    data = {}

    for title in my_titles:
        data[title.text] = title.get('href')
    return data


if __name__=='__main__':
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        SDsaramData(title=t).save()
