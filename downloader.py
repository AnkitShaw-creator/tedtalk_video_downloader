
import requests
from bs4 import BeautifulSoup
import re
import sys
import urllib.request


# the download is very slow, be patient


def extract_video(URL):
    r = requests.get("https://www.ted.com"+URL)
    print(URL)
    s = BeautifulSoup(r.content, features='lxml')
    result = ''
    for i in s.find_all("script"):
        #print(i)
        if re.search('__NEXT_DATA__', str(i)) is not None:
            result = str(i)
            #print(str(i))
    
    result_url = re.search(r"(?P<url>https://.[\S]+.mp4)", result) .group("url")
    #download_url = result_url.split('"')[0]
    print('Downloading the video from', result_url)
    file_name = URL.split('/')[-1] +".mp4"
    #print(file_name)

    urllib.request.urlretrieve(result_url,file_name)

    """with open(file_name, 'wb') as f:
        f.write(r.content)"""
    print("downloaded successfully")



def select_video_to_download(URL_LIST):
    print("Available videos:")
    for i, x in enumerate(URL_LIST):
        print(i,x)
    
    return int(input("Enter you choice:"))



def main():
    url = 'https://www.ted.com/talks'
    result = requests.get(url)

    soup = BeautifulSoup(result.content, features='lxml')
    
    url_lst = [ a['href'] for a in soup.find_all("a", attrs={'class':'ga-link', 'data-ga-context':'talks'})]
    #print(url_lst)
    i = select_video_to_download(url_lst)
    extract_video(url_lst[i])

if __name__ == "__main__":
    main()