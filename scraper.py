import time
import requests
import random

PAUSE_SEC = 1

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
]


class Scraper:

    @classmethod
    def get_rating(cls, *args, **kwargs) -> None:
        print('Please select a valid scraping method')
        return


class Glassdoor(Scraper):
    public_ip = None

    def _my_ip(self):
        if self.public_ip:
            return self.public_ip
        res = requests.get('https://ident.me')
        self.public_ip = res.text
        return self.public_ip

    def get_rating(self, company: str, url: str, query_key: str, **kwargs):
        time.sleep(PAUSE_SEC)
        p = {
            'action': 'employers',
            'q': company,
            'format': 'json',
            'v': '1',
            'useragent': user_agents[0],
            't.p': "233203",
            't.k': "jrTfWk5uhyu",
            'userip': self._my_ip(),
        }
        h = {
            'Content-Type': 'application/json',
            'User-Agent': user_agents[0]
        }
        res = requests.get(url='http://api.glassdoor.com/api/api.htm', params=p, headers=h)
        if res.status_code >= 305:
            print(f'STATUS: {res.status_code} --> {res.text}')
            return 'n/a'
        data = res.json()
        company_list = data['response'].get('employers')
        for c in company_list:
            if c.get('name').lower() == company.lower():
                return c.get('overallRating', 'n/a')
        return 'n/a'


def ScraperFactory(t: str):
    if t.lower() == 'glassdoor':
        return Glassdoor()
    else:
        return Scraper()
