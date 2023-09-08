import requests
import html2text
import re
from bs4 import BeautifulSoup


def get_links(html):
    bs = BeautifulSoup(html.text, features="html.parser")
    linkset = set()
    for link in bs.findAll('a', attrs={'href': re.compile("^https://")}):
        lname = link.get('href')
        if "wellsfargo.com" in lname or "wf.com" in lname:
            print("Added ", link.get('href'))
            linkset.add(link.get('href'))
    for link in bs.findAll('a', attrs={'href': re.compile("^/")}):
        print("Added ", url + link.get('href'))
        linkset.add(url + link.get('href'))
    return linkset


allurls = set()
visitedurls = set()

url = "https://wellsfargo.com"
allurls.update([url])

for level in range(3):
    temp = allurls.copy()
    for el in temp:
        if el not in visitedurls:
            visitedurls.update([el])
            html_content = requests.get(el)
            rendered_content = html2text.html2text(html_content.text)
            links = get_links(html_content)
            allurls.update(links)


urlfile = open('links.txt', 'w')
for e in allurls:
    urlfile.write(e + '\n')
