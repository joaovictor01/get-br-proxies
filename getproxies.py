import os
from bs4 import BeautifulSoup
import requests

def get_proxies():
    url = "https://www.freeproxy.world/?type=http&anonymity=&country=BR&speed=&port=&page=1"
    r = requests.get(url,verify=False)
    soup = BeautifulSoup(r.content,'html.parser')
    lines_ip = soup.find_all('td','show-ip-div') # get all IPs from the page
    
    open('proxies.txt','w').close() # wipe IPs already on the file
    # write proxies to a file
    with open('proxies.txt','a+') as f:
        for ip in lines_ip:
            f.write(ip.text.rstrip('\n'))

def main():
    get_proxies()

if __name__ == "__main__":
    main()



