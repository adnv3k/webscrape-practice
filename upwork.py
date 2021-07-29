import os
import sys
from bs4 import BeautifulSoup
import requests
import shelve

os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))

# url = 'https://www.upwork.com/search/jobs/?q=python&sort=recency'
# url = 'https://www.upwork.com/ab/jobs/search/?q=python&sort=recency&user_location_match=1'
# r = requests.get(url)
# r_json = r.content

# save resposne to shelf 
#first time delete
# f = shelve.open('delete')
# f['test'] = r_json
# f.close()

#delete later
f = shelve.open('delete')
r = f['test']
f.close()

soup = BeautifulSoup(r,'html.parser')

print(soup.select('body'))

