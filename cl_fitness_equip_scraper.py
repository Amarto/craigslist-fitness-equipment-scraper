from requests import get
from bs4 import BeautifulSoup
import utils

ITEMS_OF_INTEREST = ['olympic barbell weight', 'c2 rower', 'airdyne', 'squat rack']

URL_BASE = 'https://washingtondc.craigslist.org/search/sga?query='
URL_ADDON = '&hasPic=1&availabilityMode=0' # only consider listings with photos attached
interesting_items = dict()
for item in ITEMS_OF_INTEREST:
    interesting_items[item] = {}
    interesting_items[item]['results'] = []
    # interesting_items[item]['item_stats'] = {} # TODO will keep track of avg price, avg # of days on mkt
    url_str_item_name = '+'.join(item.split(' '))
    response = get(URL_BASE + url_str_item_name + URL_ADDON)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    posts = html_soup.find_all('li', class_='result-row')

    for post in posts:
        post_title = utils.get_post_title(post)
        if utils.is_post_relevant(post_title, item):
            interesting_items[item]['results'].append(utils.process_post(post))

print(interesting_items)
