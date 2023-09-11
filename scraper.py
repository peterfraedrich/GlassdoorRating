import time
import requests
from thefuzz import fuzz


class Scraper:

    @classmethod
    def get_rating(cls, *args, **kwargs) -> None:
        print('Please select a valid scraping method')
        return


class Glassdoor(Scraper):
    public_ip = None
    user_agent = None
    api_token = None
    api_key = None
    pause_seconds = 2
    headers = {}
    self_ip_uri = 'https://ident.me'
    fuzz_threshold = 75

    def __init__(self, config: dict):
        self.public_ip = self._my_ip()
        self.user_agent = config.get('user_agent')
        self.api_token = config.get('api_token')
        self.api_key = config.get('api_key')
        self.headers = self.headers.update(config.get('headers', {}))
        self.self_ip_uri = config.get('self_ip_uri', 'https://ident.me')
        self.fuzz_threshold = config.get('company_comparison_threshold', 75)
        return

    def _my_ip(self):
        if self.public_ip:
            return self.public_ip
        res = requests.get('https://ident.me')
        self.public_ip = res.text
        return self.public_ip

    def get_rating(self, company: str, url: str, query_key: str, **kwargs):
        time.sleep(self.pause_seconds)
        p = {
            'action': 'employers',
            'q': company,
            'format': 'json',
            'v': '1',
            'useragent': self.user_agent,
            't.p': self.api_token,
            't.k': self.api_key,
            'userip': self.public_ip,
        }
        h = {
            'Content-Type': 'application/json',
            'User-Agent': self.user_agent
        }
        res = requests.get(url='http://api.glassdoor.com/api/api.htm', params=p, headers=h)
        if res.status_code >= 305:
            print(f'STATUS: {res.status_code} --> {res.text}')
            return 'n/a'
        data = res.json()
        company_list = data['response'].get('employers')
        for c in company_list:
            ratio = fuzz.ratio(c.get('name').lower(), company.lower())
            if ratio >= self.fuzz_threshold:
                return c.get('overallRating', 'n/a')
        return 'n/a'


def ScraperFactory(t: str, config: dict):
    if t.lower() == 'glassdoor':
        return Glassdoor(config)
    else:
        return Scraper(config)
