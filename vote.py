#!/usr/bin/env python3
import random
import sys
import time

import requests


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Linux; U; Android 4.0.4; pt-br; MZ608 Build/7.7.1-141-7-FLEM-UMTS-LA) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
    "Opera/9.80 (J2ME/MIDP; Opera Mini/4.2/28.3590; U; en) Presto/2.8.119 Version/11.10",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Mwendo/1.1.5 Safari/537.21",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 [FBAN/FBIOS;FBAV/59.0.0.51.142;FBBV/33266808;FBRV/0;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.2;FBSS/3;FBCR/Telkomsel;FBID/phone;FBLC/en_US;FBOP/5]",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "BlackBerry8520/5.0.0.592 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/168",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13F69 Safari/601.1",
    "Mozilla/5.0 (iPad; CPU OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1",
]


def clear_output():
    sys.stdout.write("\x1b[2J\x1b[H")


class Target:
    def __init__(self, name, poll, target, referer):
        self.name = name
        self.poll = poll
        self.target = target
        self.referer = referer

    def __str__(self):
        return f'{self.name}: {self.count()}'

    @property
    def header(self):
        return {
            'content-type': 'application/json',
            'accept': 'application/json',
            'origin': 'https://istoe.com.br',
            'referer': self.referer,
            'user-agent': random.choice(USER_AGENTS),
            'accept-encoding': 'gzip, deflate, br',
            'authority': 'voting.playbuzz.com',
            'accept-language': 'en-us,en;q=0.9,pt;q=0.8'
        }

    @property
    def post_url(self):
        return f'https://voting.playbuzz.com/ranking/{self.poll}/{self.target}'

    @property
    def get_url(self):
        return f'https://voting.playbuzz.com/ranking/{self.poll}'

    def count(self):
        try:
            json = requests.get(self.get_url).json()
            return json['results'][self.target]['plus']
        except Exception as err:
            print(err)
            return -1

    def vote(self):
        data = '{"isNegative":false}'
        try:
            requests.post(self.post_url, data=data, headers=self.header)
        except Exception as err:
            print(err)
        return self


TARGET_LIST = [
    Target(
        name='Thammy Gretchen',
        poll='7dcfd1a8-2261-4e5e-afff-c23e8d5bbe83',
        target='9c85d7fa-96a0-48bd-a86c-d9457992fd8b',
        referer='https://istoe.com.br/50-mais-sexy-vote-no-homem-mais-sensual-de-2018/'
    ),
    Target(
        name='Pabllo Vittar',
        poll='66ba04e6-5d23-495a-a438-2cdeb1fcb3e3',
        target='99c34317-c969-40f3-b668-af197e678db4',
        referer='https://istoe.com.br/mulheres-mais-sensuais-2018/'
    ),
]


def voting_machine():
    while True:
        clear_output()
        for target in TARGET_LIST:
            print(target.vote())
        time.sleep(30)


print("initializing")
if __name__ == '__main__':
    voting_machine()
