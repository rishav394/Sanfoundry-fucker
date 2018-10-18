import html
import re

import bs4
import requests


def get_questions(url):
    data = requests.get(url)

    soup = bs4.BeautifulSoup(data.text, 'html.parser')

    p = soup.findAll('p')
    tet = p[1].text

    replay = re.sub('adver.+|\n\s+[a-z].+|\n\t\n', '', tet)
    replay = re.sub('(\.)\n(\d)','\g<1>\n\n\g<2>', replay)
    return replay


def get_course():
    temp = 'https://www.sanfoundry.com/'
    data = requests.get(temp)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    p = soup.select('li a')
    for x in range(3, 21):
        print(str(x - 2) + '. ' + p[x].text)
    ch = int(input("Make your choice: "))
    ch += 2
    link = p[ch]
    return link['href']


def get_subject(link):
    data = requests.get(link)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    p = soup.select('tr td li a')
    for x in range(0, len(p)):
        print(str(x + 1) + '. ' + p[x].text)
    ch = int(input("Make yur choice: "))
    ch -= 1
    return p[ch]['href']


def get_topic(link):
    data = requests.get(link)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    p = soup.select('div div h4')
    for x in p:
        print(html.unescape(x.text))
    ch = int(input("Select the topic: "))
    ch -= 1
    p = soup.select('div article div table tr')
    my = p[ch].findAll('a')
    for x in range(0, len(my)):
        print(str(x + 1) + '. ' + my[x].text)
    ch = int(input("Select the sub-topic: "))
    link = my[ch - 1]['href']
    return link


gg = get_topic(get_subject(get_course()))
print(get_questions(gg))
