import requests
from bs4 import BeautifulSoup

def scrape(url):
    """Scrape URLs to generate previews."""
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'
        })
    r = requests.get(url, headers)
    raw_html = r.content
    soup = BeautifulSoup(raw_html, 'html.parser')
    print(soup.prettify())

scrape('https://angel.co/jobs')

def getTitle(link):
    """Attemp to get description."""
    description = ''
    if link.title.string is not None:
        title = link.title.string
    elif link.find("h1") is not None:
        title = link.find("h1")
    return title


def getDescription(link):
    """Attempt to get description"""
    description = ''
    if link.find("meta", property="og:description") is not None:
        description = link.find("meta", property="og:description").get('content')
    elif link.find("p") is not None:
        description = link.find("p").content
    return description


def getImage(link):
    """Attemp to get image."""
    image = ''
    if link.find("meta", property="og:image") is not None:
        image = link.find("meta", property="og:image").get('content')
    elif link.find("img") is not None:
        image = link.find("img").content
    return image







    elif link.find("img") is not None:
        image = link.find("img").get('href')
    return image
