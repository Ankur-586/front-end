from bs4 import BeautifulSoup 
import requests

# https://www.youtube.com/watch?v=pF3KXOnxqr4
# https://proxy2.webshare.io/proxy/list?authenticationMethod=%22username_password%22&connectionMethod=%22direct%22&proxyControl=%220%22&rowsPerPage=10&page=0&order=%22asc%22&orderBy=null&searchValue=%22%22&modals=eyJ1cGdyYWRlRnJvbUZyZWVUb1JlcGxhY2VJbmRpdmlkdWFsT3BlbiI6dHJ1ZX0%253D

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
# https://gist.github.com/CodeWithHarry/14fd13acb1afce0a5991255b60aa65f5