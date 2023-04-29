import requests
from bs4 import BeautifulSoup as bs
# perhaps I misunderstood your Reddit question but if I didn't here is the boilerplate.
# Add all the base urls to this array.


headers = {
    'authority': 'myhttpheader.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'PHPSESSID=e22f53bf0d2170c71ac28ca933a681a0; _ga=GA1.2.1725963542.1682541085; _gid=GA1.2.1566002254.1682742812; _gat=1',
    'pragma': 'no-cache',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36', }
array = ['https://www.reddit.com/', 'https://twitter.com/']
searchQuery = 'bigman/biggerman'  # Put the search paramiter you want.
i = 0
for each in array:
    html = requests.get(f'{each}{searchQuery}', headers=headers).content
    soup = bs(html, 'html.parser')
    # Use file to refer to the file object
    with open(f'output{i}.html', 'w', encoding='utf8') as file:
        file.write(f'{soup}')
    i += 1
