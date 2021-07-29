"""
Scrapes the podcast pages of No Stupid Questions and People I, Mostly, Admire
to find the latest episodes, then downloads them.
"""

from urllib.request import urlopen
import requests
import os
import sys

os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))

url_list = ['https://freakonomics.com/nsq-archive/', 'https://freakonomics.com/people-i-mostly-admire/']

def make_html(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode('utf-8')
    return html

def find_episode_url(html):
    first = html.find('green-title')+22
    second = html[first:].find('">')
    return html[first:first+second]

def find_download_link(html):
    first = html.find('wkd_player_wrapper')
    second = html[first:].find('src=')+4
    end = html[first+second:].find('></audio>')-1
    link = html[1+first+second:first+second+end]
    link += "?requestSource=Widget&utm_source=Embed&download=true"
    return link

def download(link, file_name):
    r = requests.get(link,allow_redirects=True)
    open(file_name,'wb').write(r.content)
    return

for url in url_list:
    html = make_html(url)
    episode_url = find_episode_url(html)
    episode_html = make_html(episode_url)
    file_name = episode_url[episode_url.find('podcast/')+8:len(episode_url)-1] + '.mp3'
    download_link = find_download_link(episode_html)
    download(download_link, file_name)

