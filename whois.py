from colorama import Fore
b = '\033[1m'+Fore.LIGHTBLUE_EX
red = '\033[1m'+Fore.LIGHTRED_EX
g = '\033[1m'+Fore.LIGHTGREEN_EX
c = '\033[1m'+Fore.LIGHTCYAN_EX
w = '\033[1m'+Fore.LIGHTWHITE_EX
import requests, argparse
from bs4 import BeautifulSoup

parse = argparse.ArgumentParser()
parse.add_argument('-d', '--domain', help='Input domain')
args = parse.parse_args()

if args.domain:
    url = f'https://who.is/whois/{args.domain}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    result = soup.find('pre').text
    print(c+result)
else:
    exit(red+'''Expected Ergument\n  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Input domain''')