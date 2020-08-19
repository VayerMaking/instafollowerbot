
import requests
import re

uname = "_kokosaa_"

url = 'https://www.instagram.com/' + uname
r = requests.get(url).text
followers = re.search('"edge_followed_by":{"count":([0-9]+)}',r).group(1)
print(followers)
