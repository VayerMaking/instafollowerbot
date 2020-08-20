# importing libraries
from bs4 import BeautifulSoup
import requests
import re

import requests
from bs4 import BeautifulSoup

uname = "_kokosaa_"

URL = 'https://www.instagram.com/' + uname
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

job_elems = soup.find('meta', {'property':'og:description'})


print(job_elems)
asdf  = str(job_elems)[15:]
sep = ' Followers'
asdf = asdf.split(sep, 1)[0]
print(asdf)
print(len(asdf))
