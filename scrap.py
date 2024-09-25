from bs4 import BeautifulSoup 
import requests

# https://www.youtube.com/watch?v=pF3KXOnxqr4

def get_proxies():
    proxy_list = {
        "http": "38.154.227.167:5868:gcauorsz:pjrtnlhwz5i0",
        "https:" : "38.154.227.167:5868:gcauorsz:pjrtnlhwz5i0"
    }
    return proxy_list

def get_reviews(reviewUrl):
    reviews = []
    get_url = requests.get(reviewUrl, proxies=get_proxies())
    soup = BeautifulSoup(get_url, 'html.parse')
    

product_url = 'https://www.amazon.in/Samsung-Galaxy-Tab-A9-Expandable/dp/B0CXJ6F1QM/'
review_url = product_url.replace('dp', 'product-reviews')    
get_reviews(review_url)

# 38.154.227.167:5868:gcauorsz:pjrtnlhwz5i0