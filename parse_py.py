from lxml import html
import requests
import re
import wget

def parse_py(addr, download_dir):
    page = requests.get(addr)
    tree = html.fromstring(page.content)

    py = tree.xpath('//a/@href')

    for i in py:
        match = re.search(r'(.*\.py)', i)
        if match != None:
            wget.download(match.group(0), out=download_dir)


if __name__ == '__main__':
    addr = 'http://elementsofprogramminginterviews.com/solutions/'
    download_dir = '/Users/mengjiunchiou/Desktop'
    parse_py(addr, download_dir)
