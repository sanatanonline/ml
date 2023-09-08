import requests
import html2text
import re
from bs4 import BeautifulSoup


def get_links(url, html):
    bs = BeautifulSoup(html.text, "html.parser")
    links = set()
    for link in bs.findAll('a', attrs={'href': re.compile("^https://")}):
        lname = link.get('href')
        if "wellsfargo.com" in lname or "wf.com" in lname:
            links.add(link.get('href'))

    for link in bs.findAll('a', attrs={'href': re.compile("^/")}):
        print(url + link.get('href'))

    return links


url = "https://wellsfargo.com"

html_content = requests.get(url)
rendered_content = html2text.html2text(html_content.text)
links = get_links(url, html_content)

print(len(links))
