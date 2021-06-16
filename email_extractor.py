import re
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import colorama
#import packages 
colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW

internal_urls = set()
external_urls = set()

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def extract_all_urls(url):
    urls = set()
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url)).content, "html.parser")

for a_tag in soup.findAll('a'):
    href  = a_tag.attrs.get('href')
    if href == '' or href is None:
        continue

    href = urljoin(url, href)
    parsed_href = urlparse(href)
    href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
    if not is_valid(href):
            continue
    if href in internal_urls:
            continue
    if domain_name not in href:
            if href not in external_urls:
                print(f"{GRAY}[!] External link: {href}{RESET}")
                external_urls.add(href)
            continue
    print(f"{GREEN}[*] Internal link: {href}{RESET}")
    urls.add(href)
    internal_urls.add(href)
    return urls

url = "https://www.insead.edu/faculty-research/research"
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
session = HTMLSession()
r = session.get(url)
r.html.render()

for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
    print(re_match.group())
