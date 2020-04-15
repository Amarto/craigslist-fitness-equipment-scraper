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

def is_post_relevant(post_title, search_str):
    search_terms = search_str.split(' ')
    search_term_hit_count = 0
    post_title_terms = post_title.split(' ') # TODO probably make a separate util for this
    post_title_terms = [term.lower() for term in post_title_terms]
    post_title = ''.join(post_title_terms)
    for term in search_terms:
        if post_title.find(term) != -1:
            search_term_hit_count += 1

    return (search_term_hit_count/len(search_terms)) >= .5

def process_post(post):

    return {
        'title': get_post_title(post),
        'days_since_posted': get_days_since(post.find('time', class_= 'result-date')['datetime']),
        'price': '$' + str(parse_price(post.find('span', class_= 'result-price').text)),
        'neighborhood': clean_neighborhood(post.find('span', class_= 'result-hood')),
    }

def get_post_title(post):
    return post.find('a', class_= 'result-title hdrlnk').text
