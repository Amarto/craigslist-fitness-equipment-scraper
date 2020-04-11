from datetime import datetime

def get_days_since(date_str):
    post_datetime = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
    return (datetime.now() - post_datetime).days

def parse_price(price_str):
    return int(price_str.strip().replace('$', ''))

def clean_neighborhood(hood):
    if not hood:
        return None
    return hood.text.replace('(', '').replace(')', '')